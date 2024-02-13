
#Recursive digit sum
#problem: The Recursive Digit Sum problem on HackerRank is a recursive problem that asks you to find the super digit of a given integer. The super digit of an integer is defined as the sum of its digits, recursively applied until the result is a single digit.
#first idea
#For the first idea that I have, I focus on creating a function that checks if 'x' has a length of 1. If that is true, the function returns 'x'. Otherwise, the function calculates the sum of all the digits in 'x' and then saves the result in a variable 'num'. Finally, it calls the function recursively, passing the parameters 'num' and 'k' to the function. This process continues until the length of 'x' equals 1.
#My code passes 9 out of 12 tests, and the method to optimize the code doesn't work. This is because for 3 problems, the values of 'n' and 'k' are so large that the code cannot handle them.


def superDigitv1(n, k):
    num = int(n)*k
    def sum_of_arr(num,res=0):
        #verify if the length is equal to 1
        if len(num)==1:
            return(num)
        else:
            #iterate to find the sum of all the digits in 'num'.
            for i in num:
                res+=int(i)
            num = str(res)
            #Now, call the function with the new parameters.
            return sum_of_arr(num,res=0)  
    sum_of_arr(num)

#optimized and seached idea
#This code is from Hackers Realm on youtube. I included it because this code solves all the problems
def superDigitv2(n, k):
    """
    This function calculates the super digit of a number.

    Parameters:
    n (str): The number for which the super digit is to be calculated.
    k (int): The number of times 'n' is concatenated.

    Returns:
    str: The super digit of the number 'n' repeated 'k' times.

    """
    def sumOfDigits(num):
        """
        This helper function calculates the sum of digits of a number.

        Parameters:
        num (str): The number for which the sum of digits is to be calculated.

        Returns:
        str: The sum of digits if it is a single digit, else calls itself recursively.
        """
        ite = 0
        for i in num:
            ite += int(i)
        ite = str(ite)
        if len(ite) == 1:
            return ite
        else:
            return sumOfDigits(ite)
    num = str(sumOfDigits(n) * k)
    return sumOfDigits(num)
        