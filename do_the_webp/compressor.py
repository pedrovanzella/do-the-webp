import zipfile
import os


def compress(src: str, dst: str=".") -> str:
    """Compresses the contents of `dir` and outputs a cbz to `path`.
    Returns the filename"""
    basename = os.path.basename(src)
    with zipfile.ZipFile(os.path.join(dst, basename + '.cbz'), 'a') as myzip:
        for file in os.listdir(src):
            myzip.write(os.path.join(src, file))
    return basename + ".cbz"
