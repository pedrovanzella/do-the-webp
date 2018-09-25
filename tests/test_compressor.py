from do_the_webp.compressor import compress

import shutil
import os

COMPRESS_TO_DIR='tmp'

def setup_module():
    os.mkdir(COMPRESS_TO_DIR)
    # copy samples/dir

def teardown_module():
    shutil.rmtree(COMPRESS_TO_DIR)

def test_compress_dir():
    # call compress passing a dir
    # make sure the zip contains the files in dir
    # the return value should be a list of files
    # all files that exist on the dir should be the ones in the zip
    # no extras
    # no missing
    pass