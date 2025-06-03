# Selective Copy

import shutil, os
from pathlib import Path

def copy_files(folder, extension):
    # Copy folder contents with specific extension to another folder.

    folder = os.path.abspath(folder)
    new_folder = Path.cwd() / f"Copy of folder {Path(folder).name}"
    new_folder.mkdir(exist_ok=True)
    file_counter = 0

    # Walk the entire folder tree and copy the files to a new folder.
    for foldername, subfolders, filenames in os.walk(folder):
        if os.path.samefile(foldername, new_folder):
            continue
        print(f"Copying files in {foldername}...")

        # Copy files.
        for filename in filenames:
            if filename.lower().endswith(extension.lower()):
                print(f"Copying file: {filename}")
                src_path = os.path.join(foldername, filename)
                shutil.copy(src_path, new_folder)
                file_counter += 1
    print(f"Done, added {file_counter} files.")

copy_files(os.getcwd(), ".txt")