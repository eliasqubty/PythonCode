
"""
the script take the passwords from the user and  

input : 
Enter the number of items :
3
facebook s;adk3
google sd;afk34
youtube sadk329f
#OrderedDict([('facebook', 's;adk3'), ('google', 'sd;afk34'), ('youtube', 'sadk329f')])
#OrderedDict([('facebook', '7133c8c3a38420b887ba6846ef17124c'), ('google', '50b9a72e4f16b94c00694ef104bd46df'), ('youtube', '4bf06fb2ae9fc4030d0641c7320c4430')])
output Json file :
{'facebook': '7133c8c3a38420b887ba6846ef17124c', 'google': '50b9a72e4f16b94c00694ef104bd46df', 'youtube': '4bf06fb2ae9fc4030d0641c7320c4430'}      
  """
import json
import hashlib
from collections import OrderedDict
def hashedPass(password):
    hashTable = hashlib.md5(password.encode())
    return hashTable.hexdigest()
print("Enter the number of items :" )
n, d , HashedDict = int(input()), OrderedDict() , OrderedDict()
for _ in range(n):
    line = input().rstrip().split()   #['apple','10']
    item_name, item_pass = ' '.join(line[:-1]),  (line[-1])
    d[item_name]=item_pass
    HashedDict[item_name]=hashedPass(item_pass)
with open('resultpass.json', 'w') as json_file:
    json.dump(HashedDict, json_file)      #dump a dict to json file 
with open('resultpass.json','r') as json_file:
    Json_File=json.loads(json_file.read())  #load a json file to dict
print(Json_File)
  