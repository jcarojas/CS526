#!/usr/bin/env python
# coding: utf-8
We will take a standard input text file of size n lines.
# Function will iterate over n lines. 

# address how to handle error messages if text file is not used

# In[14]:


from pathlib import Path

def ask_for_file():
    while True:
        raw = input("Enter the full path of your text file: ").strip()
        raw = raw.strip('"').strip("'")
        path = Path(raw).expanduser()

        if path.suffix.lower() != ".txt":
            print("That's not a text file. Please try again!")
        elif not path.is_file():
            print(f"Couldn't find '{path}'.")
            print(f"Python is looking in: {Path.cwd()}")
        else:
            return path.resolve()

file_path = ask_for_file()

with open(file_path, "r") as file_object:
    for line in file_object:
        print(line.rstrip("\n"))


# The below program is used to take as an input a text file with n number of lines. The program will print each line in order. First, the program will need to know the full path of the text file. Since users may be using a mixture of Windows, Mac, and Linux, the program must be able to handle any variation of file paths. For this reason, we will use Path from the pathlib library. Path handles the differences between "/" and "\" in the file paths automatically. We define a function ask_for_file that will ask for the file path of the text file. The function will strip away an excess spaces. If the file path does not lead to a text file or if the file isn't found, an error message will be provided. If the file is simply not found, the program will print the working directory that Python is looking in, in an effort to assist the user with troubleshooting. The .expanduser() will allow the shorthand of "~" that refers to the home directory on Macs and Linux, and automatically include the path for the home directory if "~" is used. 
# 
# If the file exists and is confirmed to be a text file, the function will return its full absolute path using the .resolve method and save it under the variable file_path. This method automatically adds in the full file path specific to the user's system.
# 
# The open() function will read file_path and will name the contents file_object. Using a for loop, the program will iterate through each line of file_object and print all lines. The .strip("\n") will remove the new line character that exists at the end of each line so that a blank line will not be printed after each line. The program will automatically end once all lines in the file_object are iterated through. The with open() combination ensures that the file is closed automatically once the changes have been completed or if an error occurs.
