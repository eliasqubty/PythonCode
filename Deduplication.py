
# 1. Deduplication: implement a python script that loads files from a given folder path to
# memory for faster access time, if two files share the same SHA1 hash, store only one
# copy.

#file = open('C://Users//Admin//Desktop//python C//myfile.txt//CSV_files//','r+') 
#print(file.read())   
import os
import pathlib
import hashlib
path_lst=list()
dict_txt_hex=dict()
for path in pathlib.Path("C:/Users/Admin/Desktop/python C/CSV_files/").iterdir():
    if path.is_file() and not (path in path_lst) :
        current_file = open(path, "r")
        #print(path)
        file_content= current_file.read() 
        if not file_content in dict_txt_hex.keys():
          t = hashlib.sha256()
          t.update(current_file.read().encode())
          #print(t.hexdigest())
          dict_txt_hex[file_content]=t.hexdigest()
          path_lst.append(path)
        else :
          print("same content") 
        current_file.close()
    else :
        print("same dir")   
#print(dict_txt_hex)
#print(path_lst)