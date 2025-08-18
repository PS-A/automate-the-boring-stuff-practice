# Date Detection

import re

# Date regex syntax.
date_regex = re.compile(
    r"""(
    ([0-9]{2})/               # day
    ([0-9]{2})/               # month
    ([0-9]{4})                # year
    )""",
    re.VERBOSE,
)

# Test text.
text = "Testing a date 27/05/2025 and something. Another date for testing 10/15/2010"

# Logic to check if valid valid date.
matches = []
for groups in date_regex.findall(text):
    print(groups)
    day = int(groups[1])
    month = groups[2]
    year = int(groups[3])
    if (
        day in range(1, 30)
        and month in ("04, 06, 09, 11")
        and year in range(1000, 3000)
    ):
        print("Valid date.")
    elif day in range(1, 28) and month == "02" and year in range(1000, 3000):
        print("Valid date.")
    elif (
        day in range(1, 29)
        and year in range(1000, 3000)
        and (year % 4 == 0 and (year % 100 != 0 and not year % 400 == 0))
    ):
        print("Valid date.")
    elif day in range(1, 31) and year in range(1000, 3000):
        print("Valid date.")
    else:
        print("Invalid date.")
