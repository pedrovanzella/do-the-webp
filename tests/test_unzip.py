from tests.test_helper import cleanup
from do_the_webp.extractor import extract

def test_unzip_cbz():
    file = "samples/simple.cbz"
    extracted_files = extract(file)
    assert extracted_files == ['a', 'b'], "extracts a simple zip"
    cleanup(extracted_files)