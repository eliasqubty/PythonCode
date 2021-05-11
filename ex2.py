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
