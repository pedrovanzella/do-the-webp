import zipfile

def extract(file):
    zipped = zipfile.ZipFile(file)
    zipped.extractall('.')

    names = zipped.namelist()
    zipped.close()

    return names