from tests.test_helper import cleanup
from do_the_webp.extractor import extract

import os
import shutil

EXTRACT_TO_DIR='tmp'

def setup_module():
    os.mkdir(EXTRACT_TO_DIR)

def teardown_module():
    shutil.rmtree(EXTRACT_TO_DIR)

def test_unzip_simple_cbz():
    file = "samples/simple.cbz"
    extracted_files = extract(file, EXTRACT_TO_DIR)
    assert extracted_files == ['a', 'b'], "extracts a simple zip"
    assert os.path.isfile(os.path.join(EXTRACT_TO_DIR, 'a'))
    assert os.path.isfile(os.path.join(EXTRACT_TO_DIR, 'b'))

def test_unzip_nested_cbz():
    file = "samples/nested.cbz"
    extracted_files = extract(file, EXTRACT_TO_DIR)
    assert extracted_files == ['a', 'b'], "extracts a nested zip into a flat hierarchy"
    assert os.path.isfile(os.path.join(EXTRACT_TO_DIR, 'a'))
    assert os.path.isfile(os.path.join(EXTRACT_TO_DIR, 'b'))

def test_unrar_simple_cbr():
    file = "samples/simple.cbr"
    extracted_files = extract(file, EXTRACT_TO_DIR)
    assert extracted_files == ['a', 'b'], "extracts a simple cbr"
    assert os.path.isfile(os.path.join(EXTRACT_TO_DIR, 'a'))
    assert os.path.isfile(os.path.join(EXTRACT_TO_DIR, 'b'))

def test_unrar_nested_cbr():
    file = "samples/nested.cbr"
    extracted_files = extract(file, EXTRACT_TO_DIR)
    assert extracted_files == ['a', 'b'], "extracts a nested cbr into a flat hierarchy"
    assert os.path.isfile(os.path.join(EXTRACT_TO_DIR, 'a'))
    assert os.path.isfile(os.path.join(EXTRACT_TO_DIR, 'b'))