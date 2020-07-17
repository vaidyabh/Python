import os
# print the absolute directory path of the file
code_dir = os.path.dirname(os.path.realpath(__file__))

# Printing the current directory
os.getcwd()

# Pattern matching to list files
import glob
print(glob.glob("/home/adam/*.txt"))


# List files in the diretory
print(os.listdir(conf_dir))

# Adding a list with serial number same as the length of the list

new_list = []
list_data = [11,22,33,44]

for index_value in range(1, len(list_data) + 1):
    new_list.append(index_value)
    
print(new_list)

''' Output
        [1,2,3,4]
'''
