class MyNumbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    if self.a <= userInput:
      x = self.a ** 2
      self.a += 1
      return x
    else:
      raise StopIteration
userInput=int(input())
myclass = MyNumbers()
myiter = iter(myclass)
#while True:
# print(myiter.__next__())
for x in myiter:
   print(x)