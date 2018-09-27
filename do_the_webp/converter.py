import os
from PIL import Image


def convert(image: str, dst_path: str) -> str:
    """Takes a jpeg image and outputs a webp version of it"""
    basename = os.path.basename(image)
    output = os.path.splitext(basename)[0] + '.webp'

    Image.open(image).save(os.path.join(dst_path, output))

    return output
