# import argv from system

from sys import argv

# argument vector variables
script, filename = argv

# variable open filename(ex15_sample.txt)
txt = open(filename)

# print formatted string with name of file and open file contents
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

# ask to put in filename again to once again open file contents
# this line is runs after previously having opened file contents
print("Type the filename again:")
file_again = input("> ")

# this variable is determined by whatever the has input when previously prompted
txt_again = open(file_again)

# prints file contents of what filename was input by user.
print(txt_again.read())
txt_again.close()
