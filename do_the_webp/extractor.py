import zipfile
import os

from typing import List

def extract(file: str, path: str=".") -> List[str]:
    names = []
    with zipfile.ZipFile(file) as zip:
        for zip_info in zip.infolist():
            if zip_info.filename[-1] == '/':
                continue
            zip_info.filename = os.path.basename(zip_info.filename)
            zip.extract(zip_info, path)

            names.append(zip_info.filename)
    return names