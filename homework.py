#Question 1
UserListOfNumbers=[] #creates an empty list
FrequencyofNumbers=eval(input("How many numbers are you going to input?")) #Determines the total frequency of numbers to be entered
Indexoffinalnumber=FrequencyofNumbers-1 #Determines the index of the final umber by subtracting 1 from the Frequency of numbers
print("Enter a single number at anytime")
for x in range(FrequencyofNumbers):
    InputNumber=eval(input("Enter number")) #Accepts user input for the number they wish to add to the empty list
    UserListOfNumbers.append(InputNumber) #Adds the user input to the empty list
print("The following are the numbers you have entered to the new list")
for x in range(FrequencyofNumbers):
    print(UserListOfNumbers[x]) #Prints the numbers which have been entered into the list
print("The last number in the list is ",UserListOfNumbers[Indexoffinalnumber]) #Prints the last number in the list
for x in range(Indexoffinalnumber,-1,-1):
    print(UserListOfNumbers[x]) #prints the numbers in reverse order of input
Frequencyof5=UserListOfNumbers.count(5) #counts the frequeny of 5 within the list
if Frequencyof5>0: #checks the frequency of 5 to be greaater than 0
    print("Yes the list containes the number ", 5 )
else:
    print("No the number 5 is absent from the list")
print("The list UserListOfNumbers has", UserListOfNumbers.count(5),"sets of fives") #prints the frequency of 5
print("The first number",UserListOfNumbers.pop(0),"has been removed","The final number",UserListOfNumbers.pop(Indexoffinalnumber-1),"has been removed")
UserListOfNumbers.sort #sorts the numbers in ascending order
print("The numbers have been arranged in ascending order")
for x in range(len(UserListOfNumbers)):
    print(UserListOfNumbers[x]) #prints the numbers 
