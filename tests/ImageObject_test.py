"""Testing the ImageObject class.

Testing functionality as described in the ImageObject diagram in the README.

NOTE: run this test from the tests directory with:
    > pytest
"""

import pytest
import numpy as np
from PIL import Image, ImageChops, UnidentifiedImageError
import os

# Add ../ path to PATH if import fails, meaning image432 package not installed
try:
    from image432.ImageObject import ImageObject
except ModuleNotFoundError:
    import sys

    sys.path.insert(0, os.path.abspath("../src"))
    sys.path.insert(0, os.path.abspath(".src"))
    print(f"Module not found, adding to path: {sys.path[0]}")
    from image432.ImageObject import ImageObject

    pass

# Tests


def test_init_no_input():
    # Test no input
    img = ImageObject()
    assert img.file_name is None
    assert img.data is None


def test_init_file_exists():
    # Test input of a file that exists
    file_name = "test_image.png"
    img = ImageObject(file_name)
    assert img.file_name == file_name
    assert type(img.data) == np.ndarray

    # Same test but now specify file_name with keyword
    img = ImageObject(file_name=file_name)
    assert img.file_name == file_name
    assert type(img.data) == np.ndarray


def test_init_file_not_exists():
    # Test input of a file that does not exist
    fake_file_name = "xcvbjytf.png"
    try:
        ImageObject(fake_file_name)
        # Should have hit an error by now, fail otherwise
        assert False
    except FileNotFoundError:
        assert True

    # Same test but now specify file_name with keyword
    try:
        ImageObject(fake_file_name)
        # Should have hit an error by now, fail otherwise
        assert False
    except FileNotFoundError:
        assert True


def test_init_file_not_image():
    # Test input of a file that exists, but is not an image
    file_name = "not_image.txt"
    try:
        ImageObject(file_name)
        # Should have hit an error by now, fail otherwise
        assert False
    except UnidentifiedImageError:
        assert True

    # Same test but now specify file_name with keyword
    try:
        ImageObject(file_name)
        # Should have hit an error by now, fail otherwise
        assert False
    except UnidentifiedImageError:
        assert True


@pytest.mark.skip(reason="Test not created yet")
def test_grayscale():
    pass


@pytest.mark.skip(reason="Test not created yet")
def test_change_brightness():
    pass


def test_save_image():
    in_file = "test_image.png"
    out_file = "test_save_image.png"

    if os.path.exists(out_file):
        os.remove(out_file)

    img = ImageObject(in_file)
    img.save_image(out_file)
    im1 = Image.open(in_file)
    im2 = Image.open(out_file)
    print(ImageChops.difference(im1, im2))
    assert ImageChops.difference(im1, im2).getbbox() is None


@pytest.mark.skip(reason="Test not created yet")
def test_convolve():
    pass


@pytest.mark.skip(reason="Test not created yet")
def test_color_shift():
    pass


@pytest.mark.skip(reason="Test not created yet")
def test_pixelate():
    pass
