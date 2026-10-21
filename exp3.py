#1.	Write a Python program to create a tuple of five integers and display it.
'''t = (1,2,3,4,5)
print(type(t))
print(t)'''
#2. Create a tuple containing five city names
'''t = ("kolhapur","mumbai","solapur","thane","nashik")
print(t[0])
print(t[2])
print(t[4])'''
#3. Create a tuple of student names and display the total number of students using the len() function.
'''students=("aditi","srushti","arya","harshu","saee")
print(len(students))
'''
#4. Create a tuple of colors. Check whether a given color exists in the tuple
'''color =("red","orange","yellow","blue")
print('''
#5. Create a tuple of fruits and display each fruit using a loop.
'''fruits=("mango","pineapple","apple","watermelon")
for i in fruits:
  print(i)'''
#6. Create a tuple with repeated numbers and count how many times a particular number appears.
'''num =(1,2,2,3,4,4,5,5,6)
print(num.count(2))'''
#7. Create a tuple of employee IDs and find the index of a given ID.
'''id = (1,2,3,4,5,6)
print(id.index(3))'''
#8. Create two tuples of numbers and concatenate them into a single tuple
'''a=(1,2,3,4,5)
b=("aditi","harshuu","saee")
print(a+b)'''
#9.	Create a tuple containing three elements and repeat it four times.
''' num =("aditi ","harshu ","saee ")
 for i in num:
    print(i*4)'''
#1010.	Create a tuple of 10 numbers and display:
# 	First five elements 
# Last five elements 
# 	Middle four elements 
# 	Alternate elements 
# 	Reverse tuple
'''num =(1,2,3,4,5,6,7,8,9,10)
print("First five elements:",num[0:5])
print("Last five elements:",num[5:10])
print("Middle four elements:",num[3:7])
print("Alternate elements:",num[0:10:2])
print("Reverse tuple:",num[::-1])'''
#11.	Convert a tuple into a list and add a new element.
'''a = (1,2,3,4,5)
b = list(a)
b.append(6)
print(b)'''
#12.	Accept five numbers from the user, store them in a list, and convert the list into a tuple
'''a=input("Enter five numbers: ")
b=a.split(",")
c=tuple(b)
print(c)'''
#13.	Modify a tuple by converting it into a list and then back into a tuple.
'''a=(1,2,3,4,5)
b=list(a)
b.append(6)
c=tuple(b)
print(c)'''
#14.	Create a tuple and delete it completely.
'''a=(1,2,3,4,5)
del a'''
#15	Store ten numbers in a tuple and calculate their sum.
'''num=(1,2,3,4,5,6,7,8,9,10)
print(sum(num))'''
#16.	Find the largest and smallest number in a tuple without using max() and min().
'''num=(1,2,3,4,5)
largest = num[0]
smallest = num[0]
for i in num:
    if i > largest:
        largest = i
    else:
       i < smallest
       smallest = i
print("Largest number:", largest)
print("Smallest number:", smallest)'''
#17	Calculate the average of elements stored in a tuple
'''num=(1,2,3,4,5)
print(sum(num)/len(num))'''
#18.	Store 15 integers in a tuple and count:
	# Even numbers 
	# Odd numbers
'''num=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
for i in num:
    if i % 2 == 0:
        print("Even numbers:", i)
    else:
        print("Odd numbers:", i)'''
#1921.	Store student details in a tuple:

# 21.	Store student details in a tuple:
# •	Roll Number 
# •	Name 
# •	Department 
# •	Marks 
student =(26,"aditi","CSE",100)


