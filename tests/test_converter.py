from do_the_webp.converter import convert

import os
import shutil
import filecmp

DST_DIR = 'tmp'


def setup_module():
    os.mkdir(DST_DIR)


def teardown_module():
    shutil.rmtree(DST_DIR)


def test_convert():
    # make sure the output file exists
    converted = convert('samples/lenna.jpg', DST_DIR)
    assert filecmp.cmp(os.path.join(DST_DIR, converted),
                       'samples/lenna.webp'), "converted file equals reference file"
    pass
