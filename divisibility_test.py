#Modular(%) returns the remainder of a divison
print(10%2)
numbersdivisibleby2=[]
numbersnotdivisbleby2=[]
for x in range(0,100):
    if x%2 ==0 :
        numbersdivisibleby2.append(x)
    else:
        numbersnotdivisbleby2.append(x)
print(numbersdivisibleby2)
