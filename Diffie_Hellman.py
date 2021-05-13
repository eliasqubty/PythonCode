   #Prime Numbers
p , g = [int(x) for x in input("Prime p and g: ").split()]

#Private Key   
Alice_key , Bob_key = [int(x) for x in input("Private Key Alice and Bob  :").split()]

#compute public values
Alice , Bob = (g**Alice_key%p),(g**Bob_key%p)   

#Alice and Bob compute same value
Alice , Bob = (Bob**Alice_key%p),(Alice**Bob_key%p)

print( Alice , Bob)

#    Prime p and g: 1187 429
#    Private Key Alice and Bob  :546 358
#    730 730  