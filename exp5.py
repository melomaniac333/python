#factorial 
'''def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
n = int(input("Enter a number: "))
print("Factorial =", factorial(n))'''

#check_even_odd(n) 
'''def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
n=int(input("enter no.: "))    
print("The number is", even_odd(n))'''
#returns the greater number.
'''def greater(a,b):
    if a >b:
        return a
    else:
        return b
a= int(input("enter no.: "))    
b= int(input("enter no.: "))    
print("The greater number is", greater(a, b))'''
#calculate simple interest.
'''def simple_interest(p, r, t):
    SI = (p * r * t) / 100
    return SI
p= int(input("enter principal amount: "))    
r= int(input("enter rate of interest: "))    
t= int(input("enter time: "))    
print("The simple interest is", simple_interest(p, r, t))'''
#returns True if a number is prime; otherwise, returns False.
'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False    
    return True
n= int(input("enter no.: "))
print("Is the number prime?", is_prime(n))'''
#to calculate the area of a circle 
'''def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area
radius = float(input("Enter the radius of the circle: "))
print("The area of the circle is", area_of_circle(radius))'''
#returns the sum of the first n natural numbers.
'''def sum_of_natural_numbers(n):
    return n * (n + 1) // 2
n = int(input("Enter a number: "))
print("The sum of the first", n, "natural numbers is", sum_of_natural_numbers(n))'''
#function power(base, exponent) to calculate the value of base raised to exponent.
'''def power(base,expoent):
    return base ** exponent
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: ")) 
print("The result of", base, "raised to the power of", exponent, "is", power(base, exponent))'''
#that accepts a list of numbers and returns the largest element 
'''def largest_number(num):
    largest = num[0]
    for n in num:
        if n > largest:
            largest = n
    return largest
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
print("The largest number in the list is", largest_number(numbers))'''
#accepts a string and returns the number of vowels present 
'''def vowels( string):
    count = 0
    for char in string:
        if char.lower() in 'aeiou':
            count += 1
    return count
string = input("Enter a string: ")
print("The number of vowels in the string is", vowels(string))'''
#a string and returns its reverse
'''def reverse_string(string):
    return string[::-1] 
string = input("Enter a string: ")
print("The reverse of the string is", reverse_string(string))'''
#a given string or number is a palindrome
'''def is_palindrome(s):
    s = str(s)  # Convert to string if it's a number
    return s == s[::-1]
s = input("Enter a string or number: ")
print("Is it a palindrome?", is_palindrome(s))'''
#a list of numbers and returns their average.
''' average(num):
    return sum(num) / len(num)
numbers = [int(x) for x in input("Enter a list of num: ").split()]
print("The average is", average(numbers))'''
#that accepts n and returns the first n Fibonacci numbers.
'''fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print("The first", n, "Fibonacci numbers are:", fibonacci(n))'''
#marks in five subjects and returns the student's percentage and grade.
'''student_grade(marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100  # Assuming each subject is out of 100
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return percentage, grade
a=int(input("Enter marks for subject 1: "))
b=int(input("Enter marks for subject 2: "))
c=int(input("Enter marks for subject 3: "))
d=int(input("Enter marks for subject 4: "))
e=int(input("Enter marks for subject 5: "))
marks = [a, b, c, d, e]
percentage, grade = student_grade(marks)
print("The student's percentage is", percentage)
print("The student's grade is", grade)'''
#accepts the number of units consumed and calculates the electricity bill according to predefined slabs.
'''def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    elif units <= 300:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    else:
        bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 15)
    return bill


bill = electricity_bill(int(input("Enter the number of units consumed: ")))
print("The electricity bill is:", bill)'''

#accepts a list of numbers and returns the minimum, maximum, sum, and average.
'''def list_numbers(num):
    minimum = min(num)
    maximum = max(num)
    total_sum = sum(num)
    average = total_sum / len(num)
    return minimum, maximum, total_sum, average
a = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
minimum, maximum, total_sum, average = list_numbers(a)
print("The minimum is", minimum)
print("The maximum is", maximum)
print("The sum is", total_sum)
print("The average is", average)'''
#
