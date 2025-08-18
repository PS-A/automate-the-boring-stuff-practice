import os  # Import the built-in 'os' module to interact with the file system

# Define a function that renames .txt files by adding a prefix
def rename_files(prefix):
    # Loop through all items in the current directory
    for filename in os.listdir("."):
        # Check if the item is a .txt file
        if filename.endswith(".txt") and prefix not in filename:
            # Build a new file name by prepending the prefix
            new_name = f"{prefix}_{filename}"
            # Rename the file
            os.rename(filename, new_name)


# This code runs only when you run this file directly (not when it's imported)
if __name__ == "__main__":
    # Call the function and give it the prefix "week1"
    rename_files("week1")
