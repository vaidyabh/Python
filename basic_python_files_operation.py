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
