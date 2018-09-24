def cleanup(files):
    import os
    for file in files:
        os.remove(file)