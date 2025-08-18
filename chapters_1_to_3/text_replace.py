import os  # Use the 'os' module to work with files in the current directory


# This function replaces a word in all .txt files in the current folder
def replace_in_files(old, new):
    # Loop through every file in the current folder
    for fname in os.listdir("."):
        # Only look at files that end with .txt
        if fname.endswith(".txt"):
            # Open the file and read all its contents into a variable
            with open(fname, "r") as f:
                text = f.read()

            # Replace every occurrence of 'old' with 'new'
            updated = text.replace(old, new)

            # Write the updated text back into the same file
            with open(fname, "w") as f:
                f.write(updated)


# Run the function with test inputs: replace "foo" with "bar"
if __name__ == "__main__":
    replace_in_files("foo", "bar")
