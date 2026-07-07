from pathlib import Path

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))

    for i, item in enumerate(items):
        print(f"{i + 1} -> {item}")


def createFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file: ").strip()
        path = Path(name)

        if not path.exists():
            with open(path, "w") as fs:
                data = input("Enter the data to be written to the file: ").strip()
                fs.write(data)
            print(f"File '{name}' created successfully.")
        else:
            print(f"File '{name}' already exists.")
    except Exception as err:
        print(f"Error: {err}")

def readFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file to be read: ").strip()
        path = Path(name)
        if path.exists() and path.is_file():
            with open(path, "r") as fs:
                data = fs.read()
                print(f"\n{data}")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as err:
        print(f"Error: {err}")

def updateFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file to be updated: ").strip()
        path = Path(name)
        if path.exists() and path.is_file():
            print("Press 1 for change the name of your file\nPress 2 for overwriting the data of your file\nPress 3 for appending the data of your file\n")
            option = int(input("Enter your option: ").strip())

            if option == 1:
                new_name = input("Enter the new name of the file: ").strip()
                path.rename(new_name)
                print(f"File '{name}' renamed to '{new_name}' successfully.")

            elif option == 2:
                with open(path, "w") as fs:
                    data = input("Enter the data to be written to the file: ").strip()
                    fs.write(data)
                print(f"File '{name}' data overwritten successfully.")

            elif option == 3:
                with open(path, "a") as fs:
                    data = input("Enter the data to be appended to the file: ").strip()
                    fs.write(data+"\n")
                print(f"File '{name}' data appended successfully.")

            else:
                print(f"Option '{option}' does not exist.")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as err:
        print(f"Error: {err}")

def deleteFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file to be deleted: ").strip()
        path = Path(name)
        if path.exists() and path.is_file():
            path.unlink()
            print(f"File '{name}' deleted successfully.")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as err:
        print(f"Error: {err}")

            
    


def main():
    print("Welcome to the File Handling CRUD Operations!")
    readFileAndFolder()
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")

    check = int(input("Please enter your response :- "))

    if check == 1:
        createFile()
        
    if check == 2:
        readFile()
        
    if check == 3:
        updateFile()
        
    if check == 4:
        deleteFile()


if __name__ == '__main__':
    main()