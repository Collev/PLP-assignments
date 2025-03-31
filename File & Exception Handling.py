def read_and_modify_file():
    try:
        input_file = input("Enter the filename to read: ")


        with open(input_file, 'r') as file:
            content = file.read()


        modified_content = content.upper()


        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"File successfully modified and saved as {output_file}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read the file. Please check file permissions.")
    except Exception as e:
        print(f"Unexpected error: {e}")

read_and_modify_file()
