from typing import List, Tuple
import glob
import os


def traverse(dir: str) -> List[Tuple[str, str]]:
    """Traverses a directory and returns a list of tuples of paths and files"""
    files = []
    for filename in glob.iglob(dir + '/**/*', recursive=True):
        if os.path.isfile(filename):
            dir = os.path.dirname(filename)
            name = os.path.basename(filename)
            files.append((dir, name))
    return files
