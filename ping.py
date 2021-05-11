import os
import multiprocessing
def work(event):
 hostname = "www.panet.co.il"
 response = os.system("ping -n 1 " + hostname)
 if response == 0:
    pingstatus = "Network Active"
 else:
    pingstatus = "Network Error" 

if __name__ == '__main__':
    m = multiprocessing.Manager()
    e = m.Event()
    while True:
     with multiprocessing.Pool(processes = 1) as pool:
        results = pool.map(work, [e] * 1)
     
    print(results)