# Counter game
# Counter Game: Given a number, players take turns to subtract a power of 2. 
# If it's a power of 2, they halve it. The player who reduces the number to 1 wins.
# First idea
# I start by creating a function that can find the power of 2 that is lower or equal to the number passed as an argument. 
# After that, I iterate with the rules until the number is equal to 1.

# This function finds the greatest power of 2 that is less than or equal to the given number
def found_square(num,ite =1):
    while num > (2**ite):
        ite+=1
        if num == (2**ite):
            break
    return ite

# The game continues until the number is reduced to 2
turn = 0
while num !=2:
    # Now, call the function to find the power of 2 that is lower or equal to the number that the function passed to us
    res = found_square(num)
    # If the power of 2 is equal to the number, we divide the number by 2
    if num == (2**res):
        num = num //2
    # In other cases, we subtract the power of 2 from the number
    else:
        num -= (2**(res-1))
    # Change the turn using XOR operation
    turn ^=1


#first idea optimizated
#The first function works well but takes a long time to execute big queries. For that reason, I decided to optimize the function.
# This function finds the greatest power of 2 that is less than or equal to the given number
def found_square(num, ite=1):
    while num > (1 << ite):  # Shifts 1 by ite bits to the left, effectively calculating 2^ite
        ite += 1
    return ite

turn = 0
while num != 2:
    # Call the function to find the power of 2 that is lower or equal to the number
    res = found_square(num)
    # If num is a power of 2, we divide the number by 2
    if num & (num - 1) == 0:  
        num = num // 2
    # In other cases, we subtract the power of 2 from the number
    else:
        num -= (1 << (res - 1))
    # Change the turn using XOR operation
    turn ^= 1



#solution
#The optimized function also takes a long time to execute some queries. For that reason, I searched for a solution and have included it here.
# This function plays the Counter Game and returns the winner
def counterGame(n):
    turn = 0
    while n != 1:
        # If n is a power of 2, we divide the number by 2
        if n & (n - 1) == 0:
            n = n // 2
        # In other cases, we subtract the greatest power of 2 less than n from the number
        else:
            n -= 2 ** (n.bit_length() - 1)
        # Change the turn using XOR operation
        turn ^= 1
    # Return the winner of the game
    return 'Louise' if turn else 'Richard'


