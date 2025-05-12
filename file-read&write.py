# File Read and Write
def modify_file(filename, new_first_line):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Modify the first line
        if lines:
            lines[0] = new_first_line + "\n"
        
        # Write back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        
        print("File modified successfully.")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except PermissionError:
        print(f"Permission denied: Unable to access the file {filename}.")
    except IsADirectoryError:
        print(f"The specified path {filename} is a directory, not a file.")
    except OSError as e:
        print(f"An OS error occurred: {e}")