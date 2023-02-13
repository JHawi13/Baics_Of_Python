#FIND LCM
num1=eval(input('Enter the first number'))
num2=eval(input("Enter the second number"))
num3=1
for x in range(1,100,1):
    if num1/x==int and num2/x==int:
        num3=num3*x
        x=1
    else:
        if num1/x==int or num2/x==int:
            num3=num3*x
            x=1   
print(num3)