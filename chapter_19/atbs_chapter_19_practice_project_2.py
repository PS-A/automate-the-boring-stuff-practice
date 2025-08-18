# Identifying Photo Folders on the Hard Drive

#! python3

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk("C:\\"):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.lower().endswith(".png") or filename.lower().endswith(".jpg")):
            numNonPhotoFiles += 1
            continue  # skip to next filename

        # Open image file using Pillow.
        path = os.path.join(foldername, filename)
        try:
            im = Image.open(path)
            width, height = im.size
        except:
            numNonPhotoFiles += 1
            continue
        # Check if width & height are larger than 500.
        if width >= 500 and height >= 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos, print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(foldername))
