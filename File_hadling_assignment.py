import os
import shutil
# Write Operation:
# Create a file named students.txt.
with open('D:/Mindteck_Trainings/Python/Assignments/Hello/File_Handling/stidents.txt','w') as f_write:
    f_write.write("=============== STUDENT RECORS ========\n")
    f_write.write("\n")
   


# Write details of students (Name, Roll Number, Marks) into the file.
    while 1:
        name = input("Enter student name: ")
        roll_no = int(input("Enter roll number: "))
        marks = int(input("Enter marks: "))
        f_write.write(f"Name : {name}\n")
        f_write.write(f'Roll No : {roll_no}\n')
        f_write.write(f'Marks : {marks}\n')
        f_write.write("**************************\n")
        choice = input("Would you like to continue (Y/N):")
        if choice == "No" or choice == "N":
            break

# Read Operation:
# Read the content of students.txt and display it on the screen.
with open('D:/Mindteck_Trainings/Python/Assignments/Hello/File_Handling/stidents.txt','r') as f_read:
     while 1:
        record = f_read.readline()
        if not record:
            break
        print(record)


# Rename Operation:
# Rename the file from students.txt to student_records.txt.
os.rename('D:/Mindteck_Trainings/Python/Assignments/Hello/File_Handling/stidents.txt', 'D:/Mindteck_Trainings/Python/Assignments/Hello/File_Handling/stident_records.txt')

# Directory Operations:
# Create a directory called SchoolData.
os.mkdir('D:/Mindteck_Trainings/Python/Assignments/Hello/File_Handling/SchoolData')

# Move the renamed file student_records.txt into this directory.
shutil.move('D:/Mindteck_Trainings/Python/Assignments/Hello/File_Handling/stident_records.txt', 
            'D:/Mindteck_Trainings/Python/Assignments/Hello/File_Handling/SchoolData/stident_records.txt')

# List all files present in SchoolData to confirm the file is inside.
for file in os.listdir('D:/Mindteck_Trainings/Python/Assignments/Hello/File_Handling/SchoolData'):
    print(file)
    # Rwemove file
    os.remove('D:/Mindteck_Trainings/Python/Assignments/Hello/File_Handling/SchoolData/' + file)

# Delete Operation:
# Delete the file student_records.txt from inside the directory.

os.rmdir('D:/Mindteck_Trainings/Python/Assignments/Hello/File_Handling/SchoolData')