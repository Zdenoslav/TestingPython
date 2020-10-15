import names
import io
import random
import argparse

# code for a help method
parser = argparse.ArgumentParser(description='This is my help')
args = parser.parse_args()


first_names = []
for i in range(10):
    first_names.append(names.get_first_name())

last_names = []
for i in range(10):
    last_names.append(names.get_last_name())

ids = []
for i in range(10):
    ids.append(random.randint(1111, 9999))

departments = ["Sales", "Legal", "Defence", "Development"]
chosenDepartments = []
for i in range(10):
    chosenDepartments.append(random.choice(departments))

    # Generating names part
    # print(names.get_full_name())

# Creating of the files part
f = io.open("input_file1.txt", mode="w", encoding="utf-8")
for i in range(10):
    f.write(str(ids[i]) + ":" + first_names[i] + ":" +
            last_names[i] + ":" + chosenDepartments[i] + "\n")

f = io.open("input_file2.txt", mode="w", encoding="utf-8")
f.write((str(ids[i]) + ":" + first_names[i] + ":" +
         last_names[i] + ":" + chosenDepartments[i] + "\n")*2)

# an empty file
f = io.open("input_file3.txt", mode="w", encoding="utf-8")

f.close()

file1 = io.open("input_file3.txt", "r")
file2 = io.open("output_file.txt", "w", encoding="utf-8")

# a list to store the usernames and check if the username already exists
usedUsernames = []

for line in file1:

    line1 = line.split(':')

    fname = line1[1]
    lname = line1[2]

    username = fname[0] + lname

    if username in usedUsernames:
        username += str(random.randint(0, 9))
    usedUsernames.append(username)
    # print(username)

    file2.write(line1[0] + ":" + username.lower() + ":" +
                line1[1] + ":" + line1[2] + ":" + line1[3])

file1.close()
file2.close()


# Create a program to generate a list of usernames.
# The input data is stored in one or more text files with encoding utf-8.
# Each line in the input file is a record about one user and includes: ID, forename, middle
# name (optional), surname and department. Items in the line are separated by colons.
# import requests


# There is only one output file with all records together.

# Each line in the output file is a record about one user and includes:
# ID, generated username, forename, middle name (optional), surname and department.
