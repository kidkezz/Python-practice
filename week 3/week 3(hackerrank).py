#Permuting Two Arrays
#This problem is about checking if there exists a permutation of two arrays such that the sum of each pair of elements is greater than or equal to a given number k.
#The function twoArrays sorts array A in ascending order and array B in descending order. It then checks if the sum of each pair of elements from the two arrays is greater than or equal to k. If all pairs satisfy this condition, it returns ‘YES’. Otherwise, it returns ‘NO’.
def twoArrays(k, A, B):
    a = sorted(A)
    b = sorted(B, reverse=True)
    res = ''

    for i in range(len(a)):
        if a[i] + b[i] >=k:
            res = 'YES'
        else:
            res = 'NO'
            break
        
    return res


#Subarray Division 2
#This problem involves finding the number of subarrays in an array that have a specific sum d and length m.
#The function birthday uses a sliding window approach to find all subarrays of length m with sum d. It maintains a running sum aco and adjusts the window size by moving the left and right boundaries until it finds a match.

def birthday(s, d, m):
    res = 0
    l,r=0,0
    ite = len(s)
    aco = 0
    while r < ite:
        aco +=s[r]
        if aco == d and r-l+1 == m:
            res +=1
        elif aco > d:
            while aco > d:
                if l == r:
                    break
                
                aco -=s[l]
                l +=1
            if aco == d and r-l+1 == m:
                res +=1
        r+=1
    return res

#XOR Strings 3
#This problem is about performing the XOR operation on two binary strings.
#The function strings_xor performs the XOR operation on each pair of corresponding characters in strings s and t. If the characters are the same, it appends ‘0’ to the result string res. If they are different, it appends ‘1’.
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))




#Sales by Match
#This problem involves finding the number of pairs of socks with the same color.
#The function sockMerchant counts the frequency of each color in the array ar and then calculates the number of pairs for each color by integer division by 2. The result is the sum of these counts.
def sockMerchant(n, ar):
    frec = {}
    res = 0
    for i in ar:
        if i in frec:
            frec[i] +=1
        else:
            frec[i] = 1
            
    for i in frec.values():
        res += i//2
        
    return res


#Migratory Birds
#This problem is about finding the smallest bird type id that has the highest frequency in an array.
#The function migratoryBirds counts the frequency of each bird type in the array arr. It then finds the bird types with the maximum frequency and returns the smallest of these types.
def migratoryBirds(arr):
    frec = {}

    for i in arr:
        if i in frec:
            frec[i] += 1
        else:
            frec[i] = 1
            
    lista = []
    maxi = max(frec.values())
    for i in frec:
        if frec[i] == maxi:
            lista.append(i)
    return min(lista)

#Maximum Perimeter Triangle
#This problem involves finding a triangle with the maximum possible perimeter from an array of stick lengths.
#The function maximumPerimeterTriangle sorts the array sticks and then checks if any three consecutive elements form a triangle (the sum of two smaller lengths is greater than the largest length). It starts from the end of the array to maximize the perimeter. If no such triangle exists, it returns [-1].

def maximumPerimeterTriangle(sticks):
    sticks.sort()
    for i in range(len(sticks) - 3, -1, -1):
        if sticks[i] + sticks[i + 1] > sticks[i + 2]:
            return [sticks[i], sticks[i + 1], sticks[i + 2]]
    return [-1]


#Zig Zag Sequence
#This problem is about rearranging an array into a zigzag sequence.
#The function findZigZagSequence sorts the array a and then rearranges it into a zigzag sequence. It swaps the middle element with the last element and then alternates elements from the middle to the end to create a zigzag pattern.
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

#Drawing Book
#This problem involves finding the minimum number of page turns to reach a specific page in a book.
#The function pageCount calculates the number of page turns from the front (frst) and from the back (fin) of the book to reach page p. It returns the minimum of these two counts.

def pageCount(n, p):
    frst = p /2
    fin = n//2 - p//2
    
    res = min(frst,fin)
    return int(res)



#Between Two Sets
#This problem is about finding the number of integers that are divisible by all numbers in one array and are divisors of all numbers in another array.
#The function getTotalX first calculates the least common multiple (LCM) of all numbers in array a and the greatest common divisor (GCD) of all numbers in array b. It then counts the multiples of the LCM that divide the GCD evenly. This count is the number of integers that satisfy the conditions of the problem.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):  
    lcm_a = 1
    for num in a:
        lcm_a = lcm(lcm_a, num)
    gcd_b = b[0]
    for num in b[1:]:
        gcd_b = gcd(gcd_b, num)
    count = 0
    multiple_lcm_a = lcm_a
    while multiple_lcm_a <= gcd_b:
        if gcd_b % multiple_lcm_a == 0:
            count += 1
        multiple_lcm_a += lcm_a
    return count
