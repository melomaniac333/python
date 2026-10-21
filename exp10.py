#import matplotlib.pyplot as plt 
# plt.plot([1,2,3],[4,5,6])
# plt.show()

'''import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,6], color = 'red')
plt.xlim(1, 5)
plt.ylim(1, 6)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()'''

#scatter plot
'''import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
plt.scatter(x, y)
plt.show()'''

#bar plot 

'''import matplotlib.pyplot as plt
x = ["A", "B", "C"]
y = [10, 20, 15]
plt.bar(x, y)
plt.show()'''


#pie plot
'''import matplotlib.pyplot as plt
x = [30, 40, 30]
labels = ["A", "B", "C"]
plt.pie(x, labels=labels)
plt.show()'''

#histogram
'''import matplotlib.pyplot as plt
x = [10, 20, 20, 30, 30, 30, 40, 50]
plt.hist(x)
plt.show()'''


#regular expression program

#1.	Write a Python program using regular expressions to extract all digits from a given string.


import re


r'''def extract_digits(s):
    return re.findall(r'\d', s)

text = "hello 123 World 456"
digits = extract_digits(text)
print(digits)'''

# Python Programs Using Regular Expressions

### 1. Extract all digits from a given string
r'''
text = "My age is 20 and marks are 85"
result = re.findall(r'\d', text)

print("Digits:", result)
'''


# type: ignore # 2. Display all words beginning with A or a
r'''
text = "Aditi is an amazing and active student"
result = re.findall(r'\b[Aa]\w*', text)

print("Words:", result)
'''


### 3. Count occurrences of vowels in a string

'''

text = "Hello World"
result = re.findall(r'[aeiouAEIOU]', text)

print("Number of vowels:", len(result))
'''


### 4. Extract all uppercase letters

''''''
text = "Hello PYTHON World"
result = re.findall(r'[A-Z]', text)

print("Uppercase letters:", result)
''''''


### 5. Identify spaces, tabs, and newline characters


''''''
text = "Hello World\tPython\nProgramming"
result = re.findall(r'[ \t\n]', text)

print("Whitespace characters:", result)
print("Count:", len(result))
''''''

### 6. Replace multiple consecutive spaces with a single space

''''''
text = "Hello     World   Python"
result = re.sub(r' +', ' ', text)

print(result)
''''''



### 7. Display words containing exactly five characters

''''''

text = "Apple mango grape banana"
result = re.findall(r'\b\w{5}\b', text)

print("Five-letter words:", result)
''''''

### 8. Identify words ending with the letter s

''''''

text = "Cats and dogs are good pets"
result = re.findall(r'\b\w+s\b', text)

print("Words ending with s:", result)
''''''
### 9. Remove special characters while retaining letters, digits, and spaces


''''''
text = "Hello@123! Python#Programming."
result = re.sub(r'[^a-zA-Z0-9 ]', '', text)

print(result)
''''''

### 10. Count the number of words in a sentence

''''''
text = "Python is easy to learn"
result = re.findall(r'\b\w+\b', text)

print("Number of words:", len(result))
''''''

### 11. Validate a 10-digit Indian mobile number

''''''
number = input("Enter mobile number: ")

if re.fullmatch(r'[6-9]\d{9}', number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
''''''

### 12. Validate an email address

''''''

email = input("Enter email address: ")
pattern = r'^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$'

if re.fullmatch(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
''''''

### 13. Extract dates in DD-MM-YYYY format

''''''

text = "Dates are 14-10-2026 and 25-12-2025"
result = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)

print("Dates:", result)
''''''

### 14. Identify web addresses beginning with HTTP or HTTPS

''''''
text = "Visit https://google.com and http://example.com"
result = re.findall(r'https?://\S+', text)

print("Web addresses:", result)
''''''

### 15. Extract hashtags from a social media post

''''''

text = "I love #Python and #Programming"
result = re.findall(r'#[A-Za-z0-9_]+', text)

print("Hashtags:", result)
''''''

### 16. Check password strength

''''''
password = input("Enter password: ")

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'

if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")
''''''

### 17. Identify consecutive repeated words, ignoring case

''''''

text = "Python is is easy and AND useful"
result = re.findall(r'\b(\w+)\s+\1\b', text, re.IGNORECASE)

print("Repeated words:", result)
''''''

### 18. Extract six-digit Indian PIN codes

''''''
text = "My PIN is 416001 and another PIN is 400001"
result = re.findall(r'\b[1-9]\d{5}\b', text)

print("PIN codes:", result)
''''''

### 19. Validate an Indian vehicle registration number

''''''

number = input("Enter vehicle number: ")
pattern = r'^[A-Z]{2}\d{2}[A-Z]{1,3}\d{4}$'

if re.fullmatch(pattern, number):
    print("Valid vehicle number")
else:
    print("Invalid vehicle number")
''''''
### 20. Extract file extensions from filenames

''''''

text = "Files are notes.txt photo.jpg program.py"
result = re.findall(r'\.([A-Za-z0-9]+)\b', text)

print("File extensions:", result)
''''''
### 21. Remove HTML tags, extra whitespace, and punctuation

''''''

text = "<p>Hello!!!   World.</p>   Welcome, Python!"

text = re.sub(r'<[^>]*>', '', text)
text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r'\s+', ' ', text)

print(text.strip())
''''''
### 22. Extract invoice numbers, dates, and monetary amounts

''''''
text = "Invoice No: INV-1234, Date: 14-10-2026, Amount: Rs. 2500"

invoice = re.findall(r'INV-\d+', text)
date = re.findall(r'\d{2}-\d{2}-\d{4}', text)
amount = re.findall(r'Rs\.\s*\d+', text)

print("Invoice Number:", invoice)
print("Date:", date)
print("Amount:", amount)
''''''

### 23. Identify single-line comments in Python source code

''''''
text = """# This is a comment
print("Hello")
# Another comment
x = 10"""

result = re.findall(r'^\s*#.*$', text, re.MULTILINE)

print("Comments:")
for comment in result:
    print(comment.strip())

''''''
### 24. Validate product codes in ABC-1234-XY format

''''''

code = input("Enter product code: ")
pattern = r'^[A-Z]{3}-\d{4}-[A-Z]{2}$'

if re.fullmatch(pattern, code):
    print("Valid product code")
else:
    print("Invalid product code")
''''''

### 25. Extract student names, roll numbers, and marks

''''''

text = """Name: Aditi, Roll: 101, Marks: 85
Name: Rahul, Roll: 102, Marks: 90"""

pattern = r'Name:\s*(\w+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'
result = re.findall(pattern, text)

for student in result:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()
''''''
### 26. Extract DOI identifiers, publication years, email addresses, and URLs

''''''
text = """
Research paper DOI: 10.1234/abcd.2024
Published in 2024.
Email: author@gmail.com
URL: https://example.com/paper
"""

doi = re.findall(r'\b10\.\d{4,9}/[^\s,]+', text)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(r'[\w.-]+@[\w.-]+\.[A-Za-z]{2,}', text)
urls = re.findall(r'https?://\S+', text)

print("DOI:", doi)
print("Publication years:", years)
print("Email addresses:", emails)
print("URLs:", urls)


''''''