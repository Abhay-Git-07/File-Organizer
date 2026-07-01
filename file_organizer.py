#                         FILE ORGANIZER
# ==============================================================
# Project 4: File Organizer
#
# Description:
# A command-line application that organizes files into categories
# such as Images, Documents, Music, Videos, Archives, and more
# based on their file extensions.
#
# Features:
# - Organize an existing folder
# - Create a new folder for organization
# - Automatically categorize files
# - Create category folders if needed
# - Move files into their respective folders
# - Handle unknown file types using an "Others" folder
#
# Author: Abhay Chauhan
# Language: Python 3
# ==============================================================

# Import the required modules
import os
import time
import shutil

# Dictionary used to identify file categories based on extensions
file_categories = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".md", ".rtf", ".odt"
    ],

    "Spreadsheets": [
        ".xls", ".xlsx", ".csv", ".ods"
    ],

    "Presentations": [
        ".ppt", ".pptx", ".odp"
    ],

    "Music": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],

    "Python": [
        ".py", ".pyw"
    ],

    "Code": [
        ".cpp", ".c", ".java", ".js", ".ts", ".html", ".css",
        ".php", ".go", ".rs", ".swift", ".kt"
    ],

    "Executables": [
        ".exe", ".msi", ".bat", ".cmd"
    ]
}

# Dictionary used to store files after categorizing them
organized_files = {
    "Images": [],
    "Documents": [],
    "Spreadsheets": [],
    "Presentations": [],
    "Music": [],
    "Videos": [],
    "Archives": [],
    "Python": [],
    "Code": [],
    "Executables": [],
    "Others": []
}

# Function to create a new folder
def create_folder():
    while True:
        # Try and except for managing the errors
        try:
            folder_name = input("Select a name for your folder : ")
            os.mkdir(folder_name)       # This creates a new folder 
            time.sleep(2)
            print("Folder created successfully..")           
            print("Copy or move all the files you want to organize into this folder.")
            print("Hint : Go to file explorer and paste the files..")
            input("Press Enter when you're ready...\n ")
            break

        except FileExistsError:
            print("This file already exists, please choose another name.")
            continue

    return folder_name

# Function to organise existing folder
def existing_folder():
    while True:
        try:
            folder_path = input("Enter the path of the folder : ")       
            os.chdir(folder_path)
            print("Working directory : ",os.getcwd())
            print("Opening your folder.....")
            time.sleep(1)
            break
            
            
        except FileNotFoundError:
            print("Enter a valid folder path")
            continue

# Function to fetch all the files in the folder
def fetch_files():
    print("Fetching files please wait..")
    time.sleep(2)
    files_in_directory = os.listdir()
    for file in files_in_directory:
        found = False
        _, extension = os.path.splitext(file)
        for category in file_categories:
            if extension in file_categories[category]:
                found = True
                organized_files[category].append(file)
                break

        if not found:
            organized_files["Others"].append(file)    

# Function to move files into their respective category folders             
def organize_files():
    print("Organizing them in the folder...")
    for category in organized_files:
        if organized_files[category]:
            os.makedirs(category, exist_ok=True)
            for file in organized_files[category]:
                shutil.move(file, category)

# Reset the organized_files dictionary before organizing another folder
def reset_organized_files():
    for value in organized_files.values():
        value.clear()

# Main function of the program
def main():
    while True:

        # Ask the user to choose an option
        print("=" * 70)
        print(" "*20 , "FILE ORGANIZER" , " "*20)
        print("=" * 70, "\n")
        print("1. Organize an existing folder")
        print("2. Create a new folder")
        print("3. Exit")
        while True:
            try:
                choice = int(input("Choose an option : "))
                break
            except ValueError:
                print("Enter your choice in numbers.")
                continue

        # Perform the selected operation
        match choice:

            case 1 :
                existing_folder()
                fetch_files()
                organize_files()             
                
            case 2 :
                created_folder = create_folder()
                os.chdir(created_folder)
                print("Working directory : ",os.getcwd())
                fetch_files()
                organize_files()
                
            case 3 :
                print("Thanks for using file organiser..")
                break

            case _:
                print("Choose a valid option(1,2 or 3)")        
                continue
        
        # Ask whether the user wants to organize another folder
        try:
            confirmation = input("Do you want to organise another folder?(y/n) ")
            if confirmation.lower() == "y":
                reset_organized_files()
                
            else:
                print("Thanks for using File Organizer...")
                break    

        except ValueError:
            print("Please type y or n")          

# Start the program
if __name__ == "__main__":
    main()

# Display the categorized files
for key,value in organized_files.items():
    if value:
        print(key)
        print("-" * 10)
        for files in value:
            print(files)
        print("-" * 10)
            
    else:
        continue

print("✔ Organization completed successfully!")

list_of_files = os.listdir()

# Display the folders created during organization
print("Folders created :")
for data in list_of_files:
    print(f"- {data}")
