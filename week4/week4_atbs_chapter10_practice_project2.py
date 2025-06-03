# Deleting Unneeded Files

import send2trash, os
from pathlib import Path

def delete_files(folder, file_size):
    # Delete unneeded big files from given folder path.

    folder = os.path.abspath(folder)
    file_counter = 0

    # Walk the entire folder tree and delete unnecessarily big files.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Checking for huge files in {foldername}...")

        # Del files.
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                size_in_bytes = os.path.getsize(file_path)
            except Exception as e:
                print(f"Could not access {file_path}: {e}")
                continue

            size_in_mb = size_in_bytes / (1024 * 1024) # Convert from bytes to MB
            print(f"Checking file: {file_path}, size: {round(size_in_mb, 2)} MB")
            if size_in_mb > file_size:
                print(f"Deleting file: {file_path}")
                #send2trash.send2trash(os.path.join(foldername, filename))
                file_counter += 1
    print(f"Done, deleted {file_counter} files.")

delete_files(os.getcwd(), 0.01)