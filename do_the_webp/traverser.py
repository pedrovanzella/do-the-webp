import glob
import os


def traverse(dir: str):
    """Traverses a directory and returns a list of tuples of paths and files"""
    for filename in glob.iglob(dir + '/**/*', recursive=True):
        if os.path.isfile(filename):
            dir = os.path.dirname(filename)
            name = os.path.basename(filename)
            yield (dir, name)
