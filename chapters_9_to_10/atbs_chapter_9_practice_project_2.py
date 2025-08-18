# Regex Search

import re
from pathlib import Path

regex_input = input("Input RegEx: ")
pattern = re.compile(regex_input)

for file in list(Path.cwd().glob("*.txt")):
    with open(file, "r") as f:
        for line in f:
            if pattern.search(line):
                print(f"{file.name}: {line.strip()}")

# Previous version:
"""
import re
from pathlib import Path

regex_input = input("Input RegEx: ")
pattern = re.compile(regex_input)

for file in list(Path.cwd().glob("*.txt")):
    text_file = open(file)
    file_content = text_file.read()
    text_file.close()
    matches = re.findall(pattern, file_content)
    if len(matches) > 0:
        print("Matches found in file " + Path(file).name + ": " + (", ".join(matches)))
    else:
        print("No matches found from file: " + Path(file).name)
"""
