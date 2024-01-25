# Plus Minus
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
# though answers with absolute error of up to  are acceptable.
def plusMinus(arr):
    # Initialize counters for positive, negative and zero elements
    my=0
    mn=0
    zr=0

    # Iterate over the array and update counters
    for i in arr:
        if i>0:
            my+=1
        elif i <0:
            mn+=1
        else:
            zr+=1

    # Print the ratios to 6 decimal places
    print(f"{my/len(arr):.6f}") 
    print(f"{mn/len(arr):.6f}")   
    print(f"{zr/len(arr):.6f}")  

# Mini-Max Sum
# Given five positive integers, find the minimum and maximum values that can be calculated by summing 
# exactly four of the five integers. Then print the respective minimum and maximum values as a single 
# line of two space-separated long integers.
def miniMaxSum(arr):
    # Calculate the sum of the array and subtract the min and max elements to get the min and max sums
    print(f"{sum(arr)-max(arr)} {sum(arr)-min(arr)}")

# Time Conversion
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
def timeConversion(s):
    # Check the last two characters of the string to determine if the time is AM or PM
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:8]
    elif s[-2:] == "AM":
        return s[:8]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:8]
    else:
        return str(int(s[:2]) + 12) + s[2:8]

# Breaking the Records    
# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
# She tabulates the number of times she breaks her season record for most points and least points in a game. 
# Points scored in the first game establish her record for the season, and she begins counting from there.
def breakingRecords(scores):
    # Initialize variables to hold the highest and lowest scores
    vary = scores[0]
    varn = scores[0]        
    my=0
    mn=0

    # Iterate over the scores and update the highest and lowest scores
    for i in scores:
        if i >vary:
            my+=1
            vary = i
        elif i<varn:
            varn = i
            mn+=1

    # Return the number of times the highest and lowest scores were broken
    return([my, mn]) 


# Camel Case 4
# Camel Case is a naming style common in many programming languages. In Java, method and variable names 
# typically start with a lowercase letter, with all subsequent words starting with a capital letter 
# (example: startThread). Names of classes follow the same pattern, except that they start with a capital 
# letter (example: BlueCar).
# Your task is to write a program that creates or splits Camel Case variable, method, and class names.
while True:
    try:
        q=input().rstrip()
    except EOFError:
        break
    
    var = q
    res= var[4:]

    # Create Camel Case variable, method, and class names
    if var[0] == 'C':
        res = res.split()
        if var[2] == 'V':
            if len(res) >= 1:
                res[0] = res[0].lower()
            for i in range(1, len(res)):
                res[i] = res[i].title()
            print(''.join(res)) 
        
        if var[2] == 'C':
            res = [palabra.title() for palabra in res]
            print(''.join(res)) 
        
        if var[2] == 'M':
            if len(res) >= 1:
                res[0] = res[0].lower()
            for i in range(1, len(res)):
                res[i] = res[i].title()
            print(''.join(res)+'()') 
            
    # Split Camel Case variable, method, and class names
    elif var[0] == 'S':
        tem = res[0]
        if var[2] == 'V':
            for i in res[1:]:
                if i.isupper():
                    tem +=' '
                tem+= i
            print(tem.lower()) 
        
        if var[2] == 'C':
            for i in res[1:]:
                if i.isupper():
                    tem +=' '
                tem+= i
            print(tem.lower())
        
        if var[2] == 'M':
            for i in res[1:-2]:
                if i.isupper():
                    tem +=' '
                tem+= i
            print(tem.lower())

# Divisible Sum Pairs
# Given an array of integers and a positive integer k, determine the number of(i,j)  pairs where i<j  and 
# ar[i] + ar[j] is divisible by k.
def divisibleSumPairs(n, k, ar):
    res = 0
    
    # Iterate over the array and check if the sum of each pair is divisible by k
    for j in range(n-1):
        tem = ar[j]
        for i in ar[j+1:]:
            if (tem+i)%k==0 :
                res+=1    
    return res

# Sparse Arrays
# There is a collection of input strings and a collection of query strings. For each query string, 
# determine how many times it occurs in the list of input strings. Return an array of the results.
def matchingStrings(strings, queries):
    res = []
    # Iterate over the queries and count how many times each one occurs in the list of strings
    for i in queries:
        tem = 0
        for j in strings:
            if i == j:
                tem+=1
        res.append(tem)
    
    return res
