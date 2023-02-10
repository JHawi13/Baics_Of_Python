#makin listz
numbers=[98,41,26,73,45]
#len-returns the number of values within a  list
for x in range(len(numbers)):
    print(numbers[x]) #prints the numbers in the list(numbers)
#index-Returns the index of the value within the brackets from the list mentioned
Rockbands=["Metallica","Megadeth","Gojira","Parkway Drive"]
print(Rockbands.index("Metallica"))

#append-Adds content to the end of  list
numbers.append(277)
quantityofitemsinlist=len(numbers)
indexoffinalnumber=quantityofitemsinlist-1
print(numbers[indexoffinalnumber])
#count-Returns the number of times an element occurs in a list
print(numbers.count(98))
#sum returns the sum of values within a list
print(sum(numbers))
#pop removes a value of the mentioned index from a list and returns it with the print function
print(numbers.pop(2)) #value within pop is the index of the value to be removed
#insert-inserts a number at the mentioned index
numbers.insert(2,100) #first value is the index and the second value is the actual number
print(numbers)
#sort-arranges the numbers in a list in a given order(ascending or descending)
numbers.sort()
print(numbers)
#simple way of repeating  single number within a list
fifty=[50]*50
print(fifty)
#adding the items in one list to another list
list1=[20,40,77]
list2=[80,90]
list3=list1+list2
print(list3)
#to split a list
print(list3)
list3[2:]
print(list3[1:4]) #it will not print index 4 but until the number before
#find the maximum number
print(max(list3))
print(min(numbers))
#creating empty lists and adding to them 
emptylist=[]
emptylist.append(20)
for x in range(1,10):
    emptylist.append(x)
print(emptylist)
