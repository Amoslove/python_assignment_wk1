#File Read & Write Challenge 🖋️: Create a program that reads a file and writes
#  a modified version to a new file.
#Error Handling Lab 🧪: Ask the user for a filename 
# and handle errors if it doesn’t exist or can’t be read.


def read_and_write_file():
    try:
        # Ask the user for a filename to read from
        input_filename = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Ask for a new filename to write the modified content
        output_filename = input("Enter the name of the new file to write to: ")

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: An I/O error occurred while reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
