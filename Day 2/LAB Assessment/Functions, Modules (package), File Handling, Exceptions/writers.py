# writers.py

#containing a function write_numbers_to_file(filename)
def write_numbers_to_file(filename):
    try:
        with open(filename, 'w') as file:
# function should write numbers 1–100 into a file
            for i in range(1, 101):
                file.write(str(i) + "\n")
        print("Numbers written successfully.")

#Handle possible exceptions such as: File not found Permission denied
    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected error:", e)
