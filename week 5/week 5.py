# Max Min
# Given an array arr and an integer k, find the minimum difference between the maximum and minimum values in all possible subarrays of size k.
def maxMin(k, arr):
    arr.sort()
    frt = arr[:k]
    mini = max(frt) - min(frt)
    
    for i in range(1,len(arr)):
        if i+k > len(arr):
            break
        subarr = arr[i:i+k]
        num = subarr[-1] - subarr[0]
        if num < mini:
            mini = num 
    return(mini)


# Strong Password
# Determine the minimum number of characters to add to a password to make it strong.
def minimumNumber(n, arr):
    carac = "!@#$%^&*()-+."
    add = [0,0,0,0]

    for i in arr:
        if i.isdigit():
            add[0] =1
        elif i in carac:
            add[1] =1
        elif i.lower() == i:
            add[2] =1
        elif i.upper() == i:
            add[3] =1
        
    res = sum([i+1 for i in add if i ==0])

    while res+len(arr) <6:
        res+=1
    
    return(res)


# Dynamic Array
# Simulate dynamic array operations based on queries.
def dynamicArray(n, query):
    bi = [[] for _ in range(n)]
    lastans = 0
    res = []
    for i in query:
        q, x, y = map(int, i.split())
    
        if q == 1:
            idx = ((x ^ lastans)%n)
            bi[idx].append(y)
        else:
            idx = ((x ^ lastans)%n)
            lastans = bi[idx][y%len(bi[idx])]
            res.append(lastans)
    return res

# Smart Number 2
# Check if a number is a smart number.
import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val**2 == 1:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
        

# Missing Numbers
# Find missing numbers between two arrays.
from collections import Counter
def missingNumbers(arr, brr):
    prim = Counter(arr)
    segu = Counter(brr)
    res = []
    for i,j in segu.items():
        if prim[i] == segu[i]:
            continue
        else:
            res.append(i)
        
    return sorted(res)

# The Full Counting Sort
# Perform a stable sort based on the first half of integers and modify the second half to be dashes.
def countSort(arr):
    for i in arr[:len(arr)//2]:
        i[1] = "-"
        
    order = sorted(arr, key=lambda x: int(x[0]))
    res = ""
    for i in order:
        res +=" "+i[1]
    
    print(res[1:])
    
# Grid Challenge
# Determine if a grid can be rearranged to form a sorted grid.
def gridChallenge(arr):
    res = [''.join(sorted(arr[i])) for i in range(len(arr))]
    ou = 'YES'
    for i in range(len(arr[0])):
        a = ""
        for j in range(len(arr)):
            a += res[j][i]
        if a != ''.join(sorted(a)):
            ou = 'NO'

    return ou

# Sansa and XOR
# Find XOR of elements at odd positions in an array.
def sansaXor(arr):
    n = len(arr)
    if n % 2 == 0:
        return 0
    else:
        res = 0
        for i in range(0, n, 2):
            res ^= arr[i]
        return res

# Fibonacci Modified
# Generate the nth term of a modified Fibonacci sequence.
import sys
sys.set_int_max_str_digits(500000)
def fibonacciModified(t1, t2, n):
    c = [t1,t2]
    for i in range(n-2):
        t = c[i] +(c[i+1])**2
        c.append(t)
    return c[-1]
