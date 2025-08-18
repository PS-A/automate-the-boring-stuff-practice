# Regex Version of the strip() Method

import re


def strip_or_remove(string, remove):
    if len(remove) == 0:
        return re.sub(r"^\s+|\s+$", "", string)
    elif len(string) > 0 and len(remove) > 0:
        pattern = f"^[{re.escape(remove)}]+|[{re.escape(remove)}]+$"
        return re.sub(pattern, "", string)
    else:
        return "Invalid arguments."


print("Input string.")
string = input()
print("Input string to remove.")
remove = input()
print(strip_or_remove(string, remove))
