import sys
import os
import shutil

from do_the_webp.traverser import traverse
from do_the_webp.extractor import extract
from do_the_webp.converter import convert
from do_the_webp.compressor import compress


EXTRACT_TMP_DIR = '/tmp/do-the-webp/extract'
CONVERT_TMP_DIR = '/tmp/do-the-webp/convert'
COMPRESS_TMP_DIR = '/tmp/do-the-webp/compress'
TMP_DIR = '/tmp/do-the-webp'

if __name__ == '__main__':
    os.mkdir(TMP_DIR)

    for file in traverse(sys.argv[1]):
        os.mkdir(EXTRACT_TMP_DIR)
        os.mkdir(CONVERT_TMP_DIR)
        os.mkdir(COMPRESS_TMP_DIR)

        print("[+] Converting {0}/{1}".format(file[0], file[1]))
        for jpg in extract(os.path.join(file[0], file[1]), EXTRACT_TMP_DIR):
            webp = convert(os.path.join(EXTRACT_TMP_DIR, jpg), CONVERT_TMP_DIR)
            if webp is None:
                # Possibly not a jpeg. Maybe a xml, or even already a webp
                print("[!] File {0} not a valid format. Copying without conversion.".format(jpg))
                shutil.move(os.path.join(EXTRACT_TMP_DIR, jpg), os.path.join(COMPRESS_TMP_DIR, jpg))
        
        zipped = compress(CONVERT_TMP_DIR, TMP_DIR)

        print("[+] Converted")

        shutil.move(os.path.join(TMP_DIR, zipped), os.path.join(file[0], file[1]))

        shutil.rmtree(EXTRACT_TMP_DIR)
        shutil.rmtree(CONVERT_TMP_DIR)
        shutil.rmtree(COMPRESS_TMP_DIR)
        print("[+] Cleaned up")
        print("")
