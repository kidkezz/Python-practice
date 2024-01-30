# Picking Numbers
# Problem: Given an array of integers, find the maximum number of integers you can select from the array such that the absolute difference of any two of the chosen integers is less than or equal to 1.
# Function: This function sorts the input list and then counts the maximum number of elements that have an absolute difference of 1 or less.
def pickingNumbers(a):
    a.sort()
    a.append(max(a)+2)
    l = 0
    r = 1
    res= []
    con =1
    while r != len(a):
        if a[l]-a[r] >=-1:
            r+=1
            con+=1
        else:
            res.append(con)
            l +=con
            r+=1
            con =1
    return max(res)

# Left Rotation
# Problem: A left rotation operation on an array shifts each of the array's elements to the left. Given an array 'a' of 'n' integers and a number, 'd', perform 'd' left rotations on the array.
# Function: This function performs a left rotation on a list. It moves each element of the list 'd' positions to the left.
def rotateLeft(d, a):
    n = len(a)
    d = d % n  
    return a[d:] + a[:d]

# Number Line Jumps
# Problem: You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction. Determine if they land at the same location at the same time.
# Function: This function simulates the movement of two kangaroos on a number line. It determines if the two kangaroos can land at the same location at the same time.
def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 > v2:
        n = x2 - x1
        for _ in range(n):
            x1 +=v1
            x2 +=v2
            if x1>x2:
                return 'NO'
                break
            elif x1 == x2:
                return 'YES'
                break
    elif x2 < x1 and v2>v1:
        n = x1-x2
        for _ in range(n):
            x1 +=v1
            x2 +=v2
            if x2>x1:        
                return 'NO'
            elif x2 == x1:
                return 'YES'
    else:
        return 'NO'

# Separate the Numbers
# Problem: A numeric string, 's', is beautiful if it can be split into a sequence of two or more positive integers satisfying certain conditions. Determine whether a string is beautiful and, if so, identify the initial element of the sequence.
# Function: This function checks if a numeric string is beautiful. A string is beautiful if it can be split into a sequence of two or more positive integers.
def separateNumbers(s):
    length = len(s)
    for i in range(1, length // 2 + 1):
        num_str = s[:i]
        num = int(num_str)
        while len(num_str) < length:
            num += 1
            num_str += str(num)
        if num_str == s:
            print("YES", s[:i])
            return
    print("NO")

# Closest Numbers
# Problem: Given a list of unsorted integers, find the pair of elements that have the smallest absolute difference between them.
# Function: This function finds the pair of elements in a list that have the smallest absolute difference.
def closestNumbers(a):
    a.sort()
    mini = [abs(a[i]-(a[i+1])) for i in range(len(a)-1)]
    pairs = []
    diff = min(mini)
    for i in range(len(a)-1):
        if abs((a[i])-(a[i+1])) == diff:        
            pairs.append(a[i])
            pairs.append(a[i+1])
    return pairs

# Tower Breakers
# Problem: Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally. Determine which player will be the winner.
# Function: This function simulates a game of Tower Breakers. It determines which player will win the game based on the game rules.
def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1

# Minimum Absolute Difference in an Array
# Problem: Given an array of integers, find the minimum absolute difference between any two elements in the array.
# Function: This function finds the minimum absolute difference between any pair of elements in a list.
def minimumAbsoluteDifference(a):
    a.sort()
    return min(abs(a[i] - a[i+1]) for i in range(len(a) - 1))

# Caesar Cipher
# Problem: Julius Caesar protected his confidential information by encrypting it using a cipher. Given a string and a number, shift each letter in the string by the number of places down the alphabet.
# Function: This function encrypts a text string using the Caesar cipher. Each letter in the string is shifted 'p' positions down the alphabet.
def caesarCipher(arr, p):
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    abc = {letra: indice for indice, letra in enumerate(abecedario)}
    res = ''
    for char in arr:
        if char.lower() not in abc.keys():
            res += char
        else:
            n = (abc[char.lower()] + p) % 26
            if char.isupper():
                res += abecedario[n].upper()
            else:
                res += abecedario[n]
    return res

# Anagram
# Problem: Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Determine the minimum number of character deletions required to make the two strings anagrams.
# Function: This function determines the minimum number of character deletions required to make two strings anagrams.
from collections import Counter
def anagram(tex):
    tex1 = ''.join(sorted(tex[:len(tex)//2]))
    tex2 = ''.join(sorted(tex[len(tex)//2:]))
    if len(tex)%2 !=0:
        print(-1)
    else:
        res1= Counter(tex1)
        res2 = Counter(tex2)
        com = Counter(tex)
        res3 = 0
        for i,j in com.items():
            if i in res1 and i in res2:
                res3 += abs(res2[i]-res1[i])
            else:
                res3 +=j
        print(res3//2)
