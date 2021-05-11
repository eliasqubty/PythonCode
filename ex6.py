# generator that yields recursively all files paths 
# Importing the os library
import os
 
# The path for listing items
path = '.'
 
# The list of items
files = os.listdir(path)

def getFileName(files):
   yield  files

# Loop to print each filename separately
for filename in getFileName(files):
    print(filename)


 