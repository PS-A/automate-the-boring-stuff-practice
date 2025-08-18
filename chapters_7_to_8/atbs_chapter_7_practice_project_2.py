# Strong Password Detection

import re


# Password regex function.
def password_validation(password):
    if len(password) >= 8:
        has_digit = re.search(r"(\d.)", password)
        has_upper = re.search(r"([A-Z])", password)
        has_lower = re.search(r"([a-z])", password)
        has_symbol = re.search(r"([!@#$%^&*()])", password)
        if has_digit and has_lower and has_upper and has_symbol:
            return "Valid password."
        else:
            return "Invalid password."


# Ask for password as input and check if its a valid password.
print("Input password for validation.")
password = input()
print(password_validation(password))
