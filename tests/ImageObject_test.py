"""Testing the ImageObject class.

Testing functionality as described in the ImageObject diagram in the README.

NOTE: run this test from the tests directory with:
    > pytest
"""

import pytest
import numpy as np
from PIL import UnidentifiedImageError

# Add ../ path to PATH if import fails, meaning image432 package not installed
try:
    from image432.ImageObject import ImageObject
except ModuleNotFoundError:
    import sys
    import os
    sys.path.insert(0, os.path.abspath('../'))
    sys.path.insert(0, os.path.abspath('.'))
    print(f'Module not found, adding to path: {sys.path[0]}')
    from image432.ImageObject import ImageObject

def test_init_no_input():
    # Test no input
    img = ImageObject()
    assert img.file_name == None
    assert img.data == None

def test_init_file_exists():
    # Test input of a file that exists
    file_name = 'test_image.jpg'
    img = ImageObject(file_name)
    assert img.file_name == file_name
    assert type(img.data) == np.ndarray

    # Same test but now specify file_name with keyword
    img = ImageObject(file_name=file_name)
    assert img.file_name == file_name
    assert type(img.data) == np.ndarray

def test_init_file_not_exists():
    # Test input of a file that does not exist
    fake_file_name = 'xcvbjytf.jpg'
    try:
        img = ImageObject(fake_file_name)
        # Should have hit an error by now, fail otherwise
        assert False
    except FileNotFoundError:
        assert True
    
    # Same test but now specify file_name with keyword
    try:
        img = ImageObject(fake_file_name)
        # Should have hit an error by now, fail otherwise
        assert False
    except FileNotFoundError:
        assert True

def test_init_file_not_image():
    # Test input of a file that exists, but is not an image
    file_name = 'not_image.txt'
    try:
        img = ImageObject(file_name)
        # Should have hit an error by now, fail otherwise
        assert False
    except UnidentifiedImageError:
        assert True
    
    # Same test but now specify file_name with keyword
    try:
        img = ImageObject(file_name)
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
    pass

@pytest.mark.skip(reason="Test not created yet")
def test_convolve():
    pass

@pytest.mark.skip(reason="Test not created yet")
def test_color_shift():
    pass

def test_pixelate():
    pass

