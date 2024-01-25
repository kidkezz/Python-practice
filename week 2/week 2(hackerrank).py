# Lonely Integer
# Given an array of integers, where all elements but one occur twice, find the unique element.
def lonelyinteger(a):
    # Initialize a dictionary to count the occurrences of each number
    numeros = {}
    for i in range(0, max(a)+1):
        numeros[i] = 0
    
    # Count the occurrences of each number
    for i in a:
        numeros[i] += 1
    
    # Find the number that occurs only once
    for i in a:
        if numeros[i] == 1:
            return i

# Grading Students
# HackerLand University has the following grading policy:
# Every student receives a grade in the inclusive range from 0 to 100. Any grade less than 40 is a failing grade. 
# Sam is a professor at the university and likes to round each student's grade according to these rules:
# If the difference between the grade and the next multiple of 5 is less than 3, round the grade up to the next multiple of 5.
# If the value of the grade is less than 38, no rounding occurs as the result will still be a failing grade.
def gradingStudents(grades):
    # Initialize a list of multiples of 5
    mul = [i for i in range(5,101) if i%5==0]
    res= []
    num = 0

    # Round the grades according to the rules
    for i in grades:    
        if i >37:
            for j in mul:
                if j >= i:
                    num = j
                    break
            if (num-i) < 3:
                res.append(num)
            else:
                res.append(i)
        else:
            res.append(i)
        
    return(res)

# Flipping bits
# You will be given a list of 32 bit unsigned integers. Flip all the bits (1->0 and 0->1) and return the result as an unsigned integer.
def flippingBits(n):
    # Convert the number to binary and flip the bits
    bina = f"{n:032b}"
    res = ''

    for i in bina:
        if i =='1':
            res+='0'
        else:
            res +='1'
        
    # Convert the result back to an integer
    return(int(res,2))

# Diagonal Difference
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
def diagonalDifference(arr):
    sum1 = 0
    sum2=0
    tem = len(arr)-1
    # Calculate the sums of the diagonals
    for i in range(len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[i][tem]
        tem += -1
    # Return the absolute difference between the sums
    return abs((sum1-sum2))

# Counting Sort 1
# Comparison Sorting
# Quicksort usually has a running time of n x log(n), but is there an algorithm that can sort even faster? 
# In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just 
# by comparing the elements to one another. A comparison sort algorithm cannot beat n x log(n) (worst-case) 
# running time, since n x log(n) represents the minimum number of comparisons needed to know where to place 
# each element. For more details, you can see these notes (PDF).
# Alternative Sorting
# Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array 
# whose index range covers the entire range of values in your array to sort. Each time a value occurs in the 
# original array, you increment the counter at that index. At the end, run through your counting array, printing 
# the value of each non-zero valued index that number of times.
def countingSort(arr):
    # Initialize a list to count the occurrences of each number
    arc = [0 for i in range(0,100)]

    # Count the occurrences of each number
    for j in arr:
        arc[j] += 1
    
    return arc

# Counting Valleys
# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps, for every 
# step it was noted if it was an uphill, U or a downhill, D step. Hikes always start and end at sea level, and 
# each step up or down represents a unit change in altitude. We define the following terms:
# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending 
# with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending 
# with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through. 
def countingValleys(steps, path):
    # Initialize variables to keep track of the altitude and the number of valleys
    altitude = 0
    valleys = 0
    # Count the number of valleys
    for step in path:
        if step == 'U':
            altitude += 1
            if altitude == 0:
                valleys += 1
        else:
            altitude -= 1
    return valleys



# Pangrams
# Roy quiere mejorar su velocidad de escritura en máquina para concursos de programación. Su amigo le dijo 
# que escribiera la oración "The quick brown fox jumps over the lazy dog" repetidamente porque es un pangrama. 
# (pangramas son oraciones construidas usando todas las letras del alfabeto, por lo menos una vez.)
# Después de escribir la oración muchas veces, Roy se aburrió. Entonces comenzó a buscar otros pangramas.
# Dada una oración s, dile a Roy si es un pangrama o no.
def pangrams(s):
    # Initialize a list of all lowercase letters
    alfa = [chr(i) for i in range(97, 123)]
    # Convert the string to lowercase and remove duplicates
    low =s.lower()
    uni = ''.join(sorted(set(low), key=low.index))
    res = 0
    # Count the number of unique letters in the string
    for i in uni:
        if i in alfa:
            res+=1
    # If the string contains all 26 letters, it is a pangram
    if res == 26:
        return('pangram') 
    else:
        return('not pangram')

# Mars Exploration
# A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help. Letters in 
# some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by 
# Earth as a string, determine how many letters of the SOS message have been changed by radiation.
def marsExploration(s):
    # Initialize variables to keep track of the current position in the string and the number of altered letters
    it = [i for i in range(3, len(s) + 1) if i % 3 == 0]
    au = 0
    res = 0
    # Check each group of three letters for alterations
    for i in it:
        fr = s[0 + au]
        sc = s[1 + au]
        au += 3
        # Count the number of altered letters
        if fr == 'S' and sc == 'O' and s[i - 1] == 'S':
            continue
        elif (fr == 'S' and sc == 'O') or (sc == 'O' and s[i - 1] == 'S') or (fr == 'S' and s[i - 1] == 'S'):
            res += 1
        elif fr == 'S' or sc == 'O' or s[i - 1] == 'S':
            res += 2
        else:
            res += 3
    return res
