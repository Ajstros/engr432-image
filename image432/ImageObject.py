"""
ImageObject
===========
ImageObject holds file name, image data, and has methods for changing the image. Intended use is something like:

    >>> img = ImageObject('image.jpg')
    >>> img.pixelate(3)
    >>> img.save_image('new_image.jpg')
    'C:\\Users\\bob\\Desktop\\new_image.jpg'

This example shows loading an image from a file, pixelating it into 3x3 pixel squares, and saving it as a new file.
"""

from PIL import Image, UnidentifiedImageError
import numpy as np
import os


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

        if self.file_name is not None and os.path.isfile(self.file_name):
            # File specified and exists
            try:
                im = Image.open(file_name)
            except UnidentifiedImageError:
                raise UnidentifiedImageError('This file is probably not an image')

            # At this point the image has opened or an error has been raised
            self.data = np.array(im).T
