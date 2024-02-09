#day 3
#problem: misere nim 
#Given the value of n and the number of stones in each pile, we need to determine whether the person who wins the game is the first or the second person to move. If the first player to move wins, print ‘First’ on a new line; otherwise, print ‘Second’. we Assume that both players move optimally
# At first glance, this problem looks difficult and without optimal thinking, we could lose a lot of time. For that reason, I decided to understand how the game works. After that, I had a clear idea of how to solve it in an efficient way.
def misereNim(s):
#If the maximum in the array is 1, then the winner is determined by the parity of the size of the array. If the size of the array is even, then the first player wins. Otherwise, the second player wins.
    if max(s) == 1:
        if len(s) % 2 == 0:
            return 'First'
        else:
            return 'Second'
    else:
#If the maximum in the array is greater than 1, then the program calculate the Nim sum of the stones in the piles (this is done using the XOR operation). If the Nim sum is 0, then the second player wins. Otherwise, the first player wins.
        nim_sum = 0
        for pile in s:
            nim_sum ^= pile
        if nim_sum == 0:
            return 'Second'
        else:
            return 'First'


