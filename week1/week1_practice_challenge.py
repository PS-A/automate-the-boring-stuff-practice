import os

# Step 1: Ask the user for their name
name = input("Enter your name: ")

# Step 2: Ask how many .txt files to create
# (Hint: Use input() + int() to get a number)
# num_files = ...

# Step 3: Create that many .txt files in the week1/ folder
# for i in range(...):
#     filename = f"{...}.txt"   # Something like file_1.txt, file_2.txt
#     with open(filename, 'w') as f:
#         f.write("This is a test file.\n")

# Step 4: Rename each .txt file to include the user's name as a prefix
# for fname in os.listdir('.'):
#     if fname.endswith('.txt'):
#         # Create new name by prepending user's name
#         new_name = f"{...}_{fname}"
#         os.rename(fname, new_name)

print("File creation and renaming complete.")