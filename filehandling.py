# File Read & Write Challenge with Error Handling

# Ask the user for the input filename
input_filename = input("Enter the name of the file to read: ")

try:
    # Try opening and reading the file
    with open(input_filename, "r") as infile:
        content = infile.read()

    # Modify the content (Example: make it uppercase)
    modified_content = content.upper()

    # Create output filename
    output_filename = "modified_" + input_filename

    # Write modified content to a new file
    with open(output_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ Successfully created '{output_filename}' with modified content.")

except FileNotFoundError:
    print("The file you specified does not exist.")
except PermissionError:
    print("You do not have permission to read this file.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
