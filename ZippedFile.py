"""
input string :
one one two six seven six two one seven one one two six seven six two one seven one one two six seven six two one seven one one two six seven six two one seven one one two six seven six two one seven one one two six seven six two one seven one one two six seven six two one seven one one two six seven six two one seven one one two six seven six two one seven one one two six seven six two one seven one one two six seven six two one seven one one two six seven six two one seven
output:
The File size befor zip :  479
The File size after zip :  356

The file after compression :
['one','two','six','seven']  ## words without duplication 
[0,0,1,2,3,2,1,0,3,0,0 ...]  ## index each word in the file for example one=0 , two=1 ,seven=3

"""
# elias qubty
from collections import Counter
import os
with open('zippedTxt.txt','w') as zipFile:
    zipFile.write(input())

print("The File size befor zip : " ,os.path.getsize('zippedTxt.txt'))

with open('zippedTxt.txt','r') as zipFile:
    words=zipFile.read().split()
    cnt=Counter(words)
    index_=0
    WordsIndex=[0]* len(words)
    for i in cnt.keys() :
      for index,j in  enumerate(words):
          if j==i:
              WordsIndex[index]=index_
      index_+=1

with open('zippedTxt.txt','w') as zipFile:
    zipFile.write(str(list(cnt.keys())) +"\n"+str(WordsIndex)) 
 
print("The File size after zip : " , os.path.getsize('zippedTxt.txt'))
 
 


  
