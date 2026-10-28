#30 problem statements 
# 1
s="hello world !"
'''print("lengh of string is :",len(s))'''
# 2
'''vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special) '''
#3
'''print("Reverse:", s[::-1])'''
#4
'''if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")'''
#5
'''upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)'''
#6
'''s = input("Enter a string: ")
old = input("enter character :")
new = input("Enter new character: ")

s = s.replace(old, new)

print("New string:", s)'''
#7

'''s = s.replace(" ", "")

print("String without spaces:", s)'''
#8
'''ch = input("Enter character: ")

print("Frequency:", s.count(ch))'''
#9
'''print("First character:", s[0])
print("Last character:", s[-1])'''
#11
'''print("Number of words:", len(s))'''
#12
'''s="my name is Aditi. I'm in third year Btech-CSE."
words = s.split()
longest = max(words, key=len)

print("Longest word:", longest)'''
#13
'''s="my name is Aditi. I'm in third year Btech-CSE."
words = s.split()
shortest = min(words, key=len)

print("shortest word:", shortest)'''
#14
'''print("Title case:", s.title())'''
#15
'''duplicates = ""

for ch in s:
    if s.count(ch) > 1 and ch not in duplicates:
        duplicates += ch

print("Duplicate characters:", duplicates)'''
#16
'''for ch in s:
    if s.index(ch) == s.find(ch):
        print(ch, ":", s.count(ch))'''
#17
'''s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1.lower()) == sorted(s2.lower()):
    print("Anagram")
else:
    print("Not anagram")'''
#18
'''s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)'''
#19
'''s = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in s:
    print("Substring exists")
else:
    print("Substring does not exist")'''
#20
'''word = input("Enter word: ")

print("Occurrences:", s.split().count(word))'''

#21
'''password = input("Enter password: ")
if (len(password) >= 8 and
    any(ch.isupper() for ch in password) and
    any(ch.islower() for ch in password) and
    any(ch.isdigit() for ch in password) and
    any(not ch.isalnum() for ch in password)):

    print("Valid password")
else:
    print("Invalid password")'''
#22
'''result = ""
count = 1

for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

print("Compressed:", result)'''
#23
'''result = ""
count = 1

for i in range(len(s)):
    if i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

if len(result) < len(s):
    print("Compressed:", result)
else:
    print("Original:", s)'''
#24
'''ch = max(s, key=s.count)

print("Most frequent character:", ch)
print("Frequency:", s.count(ch))'''
#25
'''freq = {}

for ch in s:
    freq[ch] = s.count(ch)

values = sorted(set(freq.values()), reverse=True)

if len(values) >= 2:
    second = values[1]

    for ch in freq:
        if freq[ch] == second:
            print("Second most frequent:", ch)
            print("Frequency:", second)
            break
else:
    print("No second most frequent character")'''
#26
'''shift = int(input("Enter shift: "))

result = ""

for ch in s:
    if ch.isalpha():
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result += ch

print("Encrypted:", result)'''
#27
'''email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid email")
else:
    print("Invalid email")'''
#28
'''s="my name is Aditi. I'm in third year Btech-CSE."
words = s.lower().split()

freq = {}

for word in words:
    freq[word] = words.count(word)

print(freq)'''
#29
'''words = s.split()

print("Reversed sentence:", " ".join(words[::-1]))'''
#30
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in s1 + s1:
    print("Yes, it is a rotation")
else:
    print("No, it is not a rotation")
    
    


