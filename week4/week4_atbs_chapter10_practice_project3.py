# Filling in the Gaps

import shutil, os, re
from pathlib import Path

def fill_gaps(folder, prefix):
    # Rename files if a gap is found between files.

    folder = folder.resolve()
    pattern = re.compile(rf"{prefix}(\d+)\.txt$", re.IGNORECASE)
    matches = []

    # Walk the entire folder tree and rename files after gap.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Checking gaps in {foldername}...")

        for filename in filenames:
            match = pattern.match(filename)
            if match:
                number = int(match.group(1))
                matches.append((number, filename))
    
    matches.sort()  # Sort by number

    expected_number = 1
    for actual_number, filename in matches:
        if actual_number != expected_number:
            print(f"Would rename {filename} to {prefix}{str(expected_number).zfill(3)}.txt")
        expected_number += 1

fill_gaps(Path.cwd(), "gaptest")