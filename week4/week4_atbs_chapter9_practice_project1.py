# Mad Libs
# Mad Libs program that reads in text files and lets the user add \
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import re
from pathlib import Path

text_file = open(Path.cwd() / ('project1_testfile.txt'))
file_content = text_file.read()
print("Read text: " + file_content)
text_file.close()

matches = re.findall(r"\b(ADJECTIVE|NOUN|VERB|ADVERB)\b", file_content)

def replace_match(match):
    word_type = match.group(0).lower()
    if word_type == "adjective":
        prompt = "Enter an adjective: "
    elif word_type == "noun":
        prompt = "Enter a noun: "
    elif word_type == "verb":
        prompt = "Enter a verb: "
    elif word_type == "adverb":
        prompt = "Enter an adverb: "
    else:
        prompt = f"Enter a {word_type}:"
    return input(prompt)

modified_text = re.sub(r"\b(ADJECTIVE|NOUN|VERB|ADVERB)\b", replace_match, file_content)

text_file = open(Path.cwd() / ('project1_testfile.txt'), "w")
text_file.write(modified_text)
print("Modified text: " + modified_text)
text_file.close()