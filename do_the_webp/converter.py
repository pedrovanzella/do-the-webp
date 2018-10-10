import os
from PIL import Image


VALID_FORMATS = ['jpg', 'JPG', 'jpeg', 'JPEG']


def convert(image: str, dst_path: str) -> str:
    """Takes a jpeg image and outputs a webp version of it"""
    basename = os.path.basename(image)

    if os.path.splitext(basename)[1][1:] not in VALID_FORMATS:
        return None

    output = os.path.splitext(basename)[0] + '.webp'

    Image.open(image).save(os.path.join(dst_path, output))

    return output
