# Sherlock and Array
# This function tries to find a number where the sum of the numbers to the left of it is equal to the sum of the numbers to the right of it.
# To do this, I initially wrote a piece of code that made this possible, but the function took a long time to run with large arrays.
# So, I decided to change the way to solve the problem.

def balancedSums(arr):
    res = 'NO'
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            res = "YES"
            break
    return res

# This is how I rewrote the code. I calculate the sum of all numbers in the list until i and j are almost equal.
# If i and j are equal, that means that I will return "YES". In any other case, I will return "NO".

def balancedSums(arr):
    i, j = 0, len(arr) - 1
    sum_left, sum_right = arr[i], arr[j]
    
    while i != j:
        if sum_left < sum_right:
            i += 1
            sum_left += arr[i]
        else:
            j -= 1
            sum_right += arr[j]
    
    return "YES" if sum_left == sum_right else "NO"


