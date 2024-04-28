#####################################
##
##    Name: MarkDown Manipulator
##    Author: Naveen Srivatsav
##    Date: April 2024
##    Description: This script asks the user for a folder path. 
##    It is then able to select each Markdown file in that folder, 
##    and do any sort of text manipulation on those files.
##    Any function of your choice. Pretty neat.
##
######################################

# libraries we will need
import os

## this function asks the user to input the folder path containing the markdowns to be edited
def get_folder_from_user():
    """Prompt user for folder path and return it."""
    return input("Please enter the path to the folder: ")

## this is the function you can redefine for your own usecase.
## the default you see below is a process that removes the first line of each Markdown file 
## if the first line happens to be a heading
## it will also add a horizontal line as the first line to separate the header from the body text.
def process_single_file(file_path):
    """Read file content, remove first line, prepend with horizontal bar, and write back."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove the first line if it starts with '#'
    if lines and lines[0].startswith("#"):
        lines = lines[1:]
    
    # Ensure the new first line is '---'
    if lines and not lines[0].strip() == "---":
        lines.insert(0, "---\n")
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

## this function reads each file in the folder the user has mentioned one by one
## then sends each file to be processed
## it will always print how many files it sees in the folder
## and it will print "done" after every file
def process_markdown_files(folder_path):
    """Process all markdown files in the given folder to remove the first line and prepend with horizontal bar."""
    markdown_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
    total_files = len(markdown_files)
    print(f"{total_files} files to be processed.")

    for count, filename in enumerate(markdown_files, start=1):
        file_path = os.path.join(folder_path, filename)
        process_single_file(file_path)
        print(f" File #{count} processed...")

# Main execution
if __name__ == "__main__":
    folder_path = get_folder_from_user()
    process_markdown_files(folder_path)
    print("All done!")
