"""ImageObject holds file name, image data, and has methods for changing the image.

Intended use is something like:

    >>> img = ImageObject('image.jpg')
    >>> img.pixelate(3)
    >>> img.save_image('new_image.jpg')
    'C:\\Users\\bob\\Desktop\\new_image.jpg'

This example shows loading an image from a file, pixelating it into 3x3 pixel squares, and saving it as a new file.
"""

from PIL import Image, UnidentifiedImageError
import numpy as np
import os
import errno


class ImageObject:
    """ImageObject holds file name and image data with methods to change the image.

    Attributes
    ----------
    file_name : str
        Name of the file associated with the ImageObject.
    data : np.ndarray
        RGB data for the image.
    """

    def __init__(self, file_name=None):
        self.file_name = file_name

        if self.file_name is not None:
            if os.path.isfile(self.file_name):
                # File specified and exists
                try:
                    im = Image.open(file_name)
                except UnidentifiedImageError:
                    raise UnidentifiedImageError("This file is probably not an image")

                # At this point the image has opened or an error has been raised
                self.data = np.array(im).T
            else:
                raise FileNotFoundError(
                    errno.ENOENT, os.strerror(errno.ENOENT), file_name
                )
        else:
            self.data = None

    def pixelate(self, square_size):
        """Pixelate the image

        Pixelation is done by setting a square of pixels of length square_size to the average r, g, and b values of the pixels in that square.

        Parameters
        ----------
        square_size : int
            Length of the square of pixels (in pixels) to average.
        """

        r, g, b = self.data

        for c in [r, g, b]:
            [rows, cols] = c.shape
            for i in range(0, rows, square_size):
                for j in range(0, cols, square_size):
                    c[i : i + square_size, j : j + square_size] = np.mean(
                        c[i : i + square_size, j : j + square_size]
                    )

        self.data = np.stack((r, g, b))

    def save_image(self, output_file=None):
        """Save the image to a file.

        Parameters
        ----------
        output_file : str
            Path to save the image file at. Defaults to self.file_name if left as None.
        """

        if output_file is None:
            output_file = self.file_name

        r, g, b = self.data
        im = Image.fromarray(np.dstack([item.T for item in (r, g, b)]))
        im.save(output_file)
