"""
collections.Counter()

Exercise

Rahue is a shoe shop owner. His shop has  X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.
Your task is to compute how much money  Rahue earned.

Input Format
The first line contains X , the number of shoes.
The second line contains a space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and xi  the price of the shoe. 

Output Format
Print the amount of money earned by Rahue.

"""
from collections import Counter
print("Enter the number of shoes :" ) 
number_of_shoes=input()
dic=list()
cnt=0
temp_lst=list()
print("Enter the size of shoes :" ) 
line = input().rstrip().split()
print(Counter(line))
sizeLst=Counter(line)
print("Enter the number of customers :" ) 
number_of_customers=input()
for i in range(0,int(number_of_customers)):
    line_= input().rstrip().split()
    temp_lst=(int(line_[0]) , int(line_[-1]))
    dic.append(temp_lst)
for i in range(0,int(number_of_customers)):
     print(sizeLst)
     print(dic)
     print("i==",i)
     item=str(dic[i][0])
     print(item)
     if item in sizeLst  and sizeLst[item] > 0:
           print(item , sizeLst[item])
           print("yes")
           sizeLst[item] -=1
           cnt+=dic[i][1]
  
print(cnt)
