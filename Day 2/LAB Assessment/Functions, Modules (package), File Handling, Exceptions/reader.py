# reader.py

#module that imports this function and reads the file content safely
from writers import write_numbers_to_file

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:\n")
            print(content)

    except FileNotFoundError:
        print("Error: File not found while reading.")

    except PermissionError:
        print("Error: Permission denied while reading.")

    except Exception as e:
        print("Unexpected error:", e)


# Main execution
filename = "numbers.txt"

write_numbers_to_file(filename)
read_file(filename)
