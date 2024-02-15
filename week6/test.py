#palindrome index
#Given a string of lowercase letters (ascii [a-z]), determine the index of a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove1.
#In other words, you need to write a function that checks if a given string is a palindrome. If it’s not, the function should determine which character can be removed from the string to make it a palindrome and return the index of that character. If the string is already a palindrome or cannot be turned into a palindrome by removing a single character, the function should return -1.
#first idea that i have
#With the examples that HackerRank provided, I created this code. This code is functional with the sample cases that HackerRank provided. However, when I tried to run this code on all test cases, it turned out to be too basic and only achieved 1 out of 15.
def palindromeIndexv1(arr):
    #This function checks if the first item is different from the last item. If it is true, it checks if any of these elements is the element that we need to find. In other cases, it returns -1.
    if arr[0] != arr[-1]:
        case1 = arr[:-1]
        case2 = arr[1:]
        if case1 == case1[::-1]:
            print(len(case1))
        elif case2 == case2[::-1]:
            print(0)
        else:
            return -1
    else:
        print(-1)
#After this fuction, I had another idea, but ultimately this function ended up doing the same as the first function. Several hours later and after 5 attempts without any significant progress, I decided to look at the solution
def palindromeIndex(s):
    # Check if the string is a palindrome
    if s == s[::-1]:
        return -1
    
    n = len(s)
    
    # Iterate over the string from both ends
    for i in range(n//2):
        # Check if the character from the left end is different from the right end
        if s[i] != s[n-1-i]:
            # If they are different, check two scenarios:
            # 1. Removing the character from the right end makes the remaining string a palindrome
            if s[i:n-1-i] == s[i:n-1-i][::-1]:
                # If so, return the index of the character from the right end
                return n-1-i
            # 2. Removing the character from the left end makes the remaining string a palindrome
            elif s[i+1:n-i] == s[i+1:n-i][::-1]:
                # If so, return the index of the character from the left end
                return i
    # If no single character can be removed to create a palindrome, return -1
    return -1

