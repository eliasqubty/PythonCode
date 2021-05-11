#elias qubty
"""
Brute force attack to Md5 
example 
output:
0a57258559de00695ffb0f1d46bba388 eli
[None, None, None, None, 'eli']
"""
import random
import hashlib
from xeger import Xeger
from collections import Counter
import json
import multiprocessing
myDicPass = {
  "1": "eli",
  "2": "qub",
  "3": "pow"
}
 
t_value = hashlib.md5()  
PassDict =dict()
for key,value in myDicPass.items():  
 t_value.update(value.encode())
 PassDict.update(({key:t_value.hexdigest()}))
valuesLst =list(PassDict.values())
with open('c:/Users/Admin/Desktop/result1.json', 'w') as fp:
    json.dump(PassDict, fp)
 
def work(event):
      while not event.is_set():
        x = Xeger(limit = 3)
        t = hashlib.md5()
        pass_try = x.xeger("([0-9a-z]+)")
        t.update(pass_try.encode())
        if (t.hexdigest() == PassDict["1"]):
            print(t.hexdigest() , pass_try)
            event.set()
            return pass_try
        
if __name__ == '__main__':
    m = multiprocessing.Manager()
    e = m.Event()
    
    with multiprocessing.Pool(processes = 5) as pool:
        results = pool.map(work, [e] * 5)
     
    print(results)