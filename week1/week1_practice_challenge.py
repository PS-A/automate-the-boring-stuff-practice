import os

# Step 1: Ask the user for their name
name = input("Enter your name: ")

# Step 2: Ask how many .txt files to create
try:
    num_files = int(input("How many input files to create: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# Step 3: Create that many .txt files in the week1/ folder
for i in range(1, num_files + 1):
    filename = "file" + str(i) + ".txt"
    with open(filename, 'w') as f:
        f.write("This is a test file.\n")
        +i

# Step 4: Rename each .txt file to include the user's name as a prefix
for fname in os.listdir('.'):
    if fname.endswith('.txt') and name not in fname:
        #Create new name by prepending user's name
        new_name = f"{name}_{fname}"
        os.rename(fname, new_name)

print("File creation and renaming complete.")