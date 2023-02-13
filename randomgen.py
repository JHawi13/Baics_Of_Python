#to import a function from the python library one must use the from function to state the location of the library and import to state the function to be imported
from random import randint
RandomNumberlist=[]
for x in range (10):
    num=randint(0,10)
    x=num
for num in RandomNumberlist:
    print(num)
    