from do_the_webp.compressor import compress

import shutil
import os
import zipfile

COMPRESS_TO_DIR = 'tmp'
SOURCE_DIR = 'samples/to_be_compressed'


def setup_module():
    os.mkdir(COMPRESS_TO_DIR)


def teardown_module():
    shutil.rmtree(COMPRESS_TO_DIR)


def test_compress_dir():
    zipped = compress(SOURCE_DIR, COMPRESS_TO_DIR)
    assert zipped == 'to_be_compressed.cbz', "file is properly named"
    compressed_files = []
    with zipfile.ZipFile(os.path.join(COMPRESS_TO_DIR, zipped), 'r') as z:
        compressed_files = [os.path.basename(x) for x in z.namelist()]
    assert os.listdir(SOURCE_DIR) == compressed_files, "all files in the source dir were zipped"
