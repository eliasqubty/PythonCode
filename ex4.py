
# Here is an example of a python inbuilt iterator 
# value can be anything which can be iterate
file = open('C://Users//Admin//Desktop//python C//myfile.txt','r+')  
str = file.read()
iterable_obj = iter(str)
while True:
    try:
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        # exception will happen when iteration will over
        break
file.close()    