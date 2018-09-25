import zipfile
import os
import rarfile
import shutil

from typing import List

def extract(file: str, path: str=".") -> List[str]:
    """Extracts a file based on the file type"""
    if zipfile.is_zipfile(file):
        return unzip(file, path)
    if rarfile.is_rarfile(file):
        return unrar(file, path)
    return []

def unzip(file: str, path: str=".") -> List[str]:
    """Unzips a file into a flat hierarchy"""
    names = []
    with zipfile.ZipFile(file) as zip:
        for zip_info in zip.infolist():
            if zip_info.filename[-1] == '/':
                continue
            zip_info.filename = os.path.basename(zip_info.filename)
            zip.extract(zip_info, path)

            names.append(zip_info.filename)
    return names

def unrar(file: str, path: str=".") -> List[str]:
    """Unrars a file into a flat hierarchy"""
    names = []
    with rarfile.RarFile(file) as rar:
        rar.extractall(path)
        for rar_info in rar.infolist():
            basename = os.path.basename(rar_info.filename)
            shutil.move(os.path.join(path, rar_info.filename), 
                        os.path.join(path, basename))
            names.append(basename)
    return names