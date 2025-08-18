# Sandwich Maker

# 1st attempt
"""
import pyinputplus as pyip

wheat_price = 1
white_price = 2
sourdough_price = 1
chicken_price = 1
turkey_price = 1
ham_price = 2
tofu_price = 5
cheddar_price = 1
Swiss_price = 2
mozzarella_price = 3
condiment_price = 1

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', "tofu"])
cheese_type = ""
cheese = pyip.inputYesNo(prompt = "Do you want cheese?")
if cheese == "yes":
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
condiments = pyip.inputYesNo(prompt = "Do you want mayo, mustard, lettuce or tomato?")
while True:
    amount = pyip.inputInt(prompt = "How many sandwiches do you want?")
    if amount >= 1:
        break
    else:
        "Amount has to be 1 or more sandwiches."

# Calculate cost
total_cost = 0

# Bread
if bread == "wheat":
    total_cost += (wheat_price * amount)
elif bread == "white":
    total_cost += (white_price * amount)
elif bread == "sourdough":
    total_cost += (sourdough_price * amount)

# Protein
if protein == "chicken":
    total_cost += (chicken_price * amount)
elif protein == "turkey":
    total_cost += (turkey_price * amount)
elif protein == "ham":
    total_cost += (ham_price * amount)
elif protein == "tofu":
    total_cost += (tofu_price * amount)

# Cheese
if cheese_type == "cheddar":
    total_cost += (cheddar_price * amount)
elif cheese_type == "Swiss":
    total_cost += (Swiss_price * amount)
elif cheese_type == "mozzarella":
    total_cost += (mozzarella_price * amount)

# Condiments
if condiments == "yes":
    total_cost += (condiment_price * amount)

print("Your total cost is: " + str(total_cost))
"""

# 2nd attempt, made cleaner and tidier.
import pyinputplus as pyip

bread_prices = {"wheat": 1, "white": 2, "sourdough": 1}
protein_prices = {"chicken": 1, "turkey": 1, "ham": 2, "tofu": 5}
cheese_prices = {"cheddar": 1, "swiss": 2, "mozzarella": 3}
condiment_price = 1

bread = pyip.inputMenu(["wheat", "white", "sourdough"])
protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"])
cheese_type = ""
cheese = pyip.inputYesNo(prompt="Do you want cheese?")
if cheese == "yes":
    cheese_type = pyip.inputMenu(["cheddar", "swiss", "mozzarella"])
condiments = pyip.inputYesNo(prompt="Do you want mayo, mustard, lettuce or tomato?")
amount = pyip.inputInt(prompt="How many sandwiches do you want?", min=1)

# Calculate cost
total_cost = 0
total_cost += bread_prices[bread] * amount
total_cost += protein_prices[protein] * amount
total_cost += cheese_prices[cheese_type] * amount
if condiments == "yes":
    total_cost += condiment_price * amount

print(f"Your total cost is: {total_cost}")
