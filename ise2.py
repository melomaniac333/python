#create a function that accepts a list and return number of even , odd, positive , negative elements
'''def count_elements(lst):
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0
    
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
            
    return {
        "even": even_count,
        "odd": odd_count,
        "positive": positive_count,
        "negative": negative_count
    }   
result = count_elements([1, 2, 3, -4, -5, 6, 7, -8, 9, 10])
print("Even numbers:", result["even"])
print("Odd numbers:", result["odd"])    
print("Positive numbers:", result["positive"])
print("Negative numbers:", result["negative"])'''

#accepts marks in 5 sunjects and calculate total and percentage 
'''def calc(marks):
    total = sum(marks)

    percentage = (total / (len(marks)*100)) * 100
    return total, percentage
calculate = calc([85, 90, 78, 92, 88])
print(calculate)'''

