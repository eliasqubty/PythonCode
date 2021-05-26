import os 
import shutil  
import pathlib
#get the current directory of the file 
current_dir = os.path.dirname(os.path.realpath(__file__))
 
for path in pathlib.Path(current_dir).iterdir():
    if path.is_file() :
       # get file name from the path , example : C:\Users\Admin\Desktop\reorder\bb.txt ---> filename=bb.txt
       filename = str(path).split("\\")[-1]
       #example : filename = 'xyz.of.tt.txt'
       #file_name = 'xyz.of.tt' (get the part from the beginning to the last point)   , end = 'txt' (get the part from the last point to the end ) 
       lst = filename.split(".")
       file_name = (".").join(lst[:-1])  
       end = str(lst[-1])
       if not pathlib.Path(current_dir+"\\"+end).exists() :
           os.mkdir(pathlib.Path(current_dir+"\\"+end))    # create a new folder if not exists
       shutil.copy(path,pathlib.Path(current_dir+"\\"+end)) # copy file to the new folder
       if filename !=  'ReorderFiles.py':        #to protect the code file from directory changing  
          os.remove(path)
      

 