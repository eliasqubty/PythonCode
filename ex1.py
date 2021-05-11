"""
collections.OrderedDict
Exercise
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day. Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format
The first line contains the number of items, .
The next  lines contain the item's name and price, separated by a space.

Constraints
N <= 100
Output Format
Print the item_name and net_price in order of its first occurrence.

"""
from collections import OrderedDict
print("Enter the number of items :" )
n, d = int(input()), OrderedDict()
for _ in range(n):
    line = input().rstrip().split()   #['apple','10']
    item_name, net_price = ' '.join(line[:-1]), int(line[-1]) #item_name=apple , net_price=10
    if item_name in d: d[item_name] += net_price
    else: d[item_name] = net_price
# for example --->  d = OrderedDict([('aaa', 200), ('bbb', 600)])
for item in d:
   print(item, d[item])
#for item in sorted(sorted(d, key=lambda t: t[0])):
#   print(item, d[item])

