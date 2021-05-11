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

