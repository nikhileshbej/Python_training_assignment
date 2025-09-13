# Assignment 1: List All .txt Files and Check for a Word using glob + re.search
 
# Write a script to:
# - Find all .txt files in a folder.
# - Check if any file contains the word "Python".
# - Print the file name if the word is found
 
import glob
import re

print("Asasignment 1 ==========================")
files = glob.glob("D://Mindteck_Trainings//Python//Assignments//Hello//Pattern//dir_search//*.txt")
for item in files:
    #print(item)
    with open(item) as f:
        content = f.read()
        #print(content)
        found = re.search(r"python|Python", content)
        #print(found)
        if (found is not None):
            print("The word python is present in the file: ", item)


# Assignment 2: Match File Names Using re.match
# List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".
print("Asasignment 2 ==========================")
files = glob.glob("D://Mindteck_Trainings//Python//Assignments//Hello//Pattern//dir_search//*.*")
for item in files:
    #print(item)
    match = re.match(r"data_", item)
    #print(match)
    csv_file = re.search("csv$", item)
    #print(csv_file)
    if (match is not None and csv_file is not None):
        print(item)



# Assignment 3: Validate Phone Numbers with re.match
# Given a list of phone numbers, print only the ones that match this format:
# (123) 456-7890

print("Asasignment 3 ==========================")
phone_numbers = list["((123) 456-7890)", "((122) 456-7890)", "((123) 456-7890)", "((125) 456-7890)"]

for item in phone_numbers:
    #print(item)
    match_num = re.search(r"*123*", item)
    if(match_num is not None):
        print(item)





        