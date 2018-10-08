from typing import List, Tuple


def traverse(dir: str) -> List[Tuple[str, str]]:
    """Traverses a directory and returns a list of tuples of paths and files"""
    return [('', '')]