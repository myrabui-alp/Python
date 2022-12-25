# Check file is empty or not
import os
file_name = input("Enter file name: ")
f = os.stat(file_name).st_size
if f == 0:
    print('The file is empty')
