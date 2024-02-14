#sum vs Xor
#problem :The Sum vs XOR problem on HackerRank involves finding all numbers less than a given number 'n' where the sum and XOR of 'n' and that number are equal.
#first idea
#The function sumXor(n) calculates the number of values less than 'n' for which the sum and XOR with 'n' are equal.
def sumXor(n):
    #The function initializes a result variable 'res' to 0. It then iterates over each number 'i' from 0 to 'n-1'. For each 'i', it calculates the sum (n+i) and the XOR (n^i) of 'n' and 'i'. If the sum and XOR are equal, it increments 'res' by 1.
    res=0
    for i in range(n):
        op1 = n+i
        op2 = n^i
        if op1 == op2:
            res+=1
    #Finally, the function returns 'res'. However, if 'n' is 0, the function returns 1. This is because 0 is the only number for which the sum and XOR with 0 are equal.
    return 1 if n ==0 else res

#If you examine the function closely, you'll notice that it may not perform well if 'n' is a large number. This is because the function has to iterate over all numbers from 0 to 'n'. This causes the function to either not work well or take a long time to execute in such cases.
#So, I decided to search for another way to solve this, but I couldn't create a correct solution for all cases. Therefore, I finally decided to search for the optimal solution.

#solution 
#The function sumXor(n) calculates the number of values less than 'n' for which the sum and XOR with 'n' are equal.

def sumXor(n):
    #This function uses an efficient approach based on the binary representation of 'n'. It initializes a variable 'result' to 1 and then enters a while loop that continues as long as 'n' is not zero.
    result =1
    while n:
    #In each iteration of the loop, the function checks the least significant bit of 'n' (obtained by 'n & 1'). If this bit is zero, it doubles the 'result'. Then, it right-shifts 'n' by one bit (equivalent to dividing 'n' by 2).
        b=n&1
        n>>=1
        if b ==0:
            result *=2
    #Finally, the function returns 'result', which is the count of numbers less than 'n' that satisfy the condition of sum equals XOR. This count is equal to 2^(number of zeros in the binary representation of 'n'
    return result