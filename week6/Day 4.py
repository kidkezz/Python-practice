#Gaming Array 1
# the problem two players, Bob and Andy, take turns to remove the maximum element in an array and all elements to its right, with the last player able to make a move being the winner.
#first idea
# Initially, I was thinking about how to find the index of the max number in arr. Then, with this index, I can reduce the original arr to arr[:max]. This eliminates every number including the max and the numbers on its right.
# When this happens, the only thing left is to iterate over that function and make a few conditions for some exercises.

def gamingArrayv1(arr):
    def max_cuter(arr,j):
        #found the index
        ini = {val: ind for ind, val in enumerate(arr)}
        if j in ini:
            i = ini[j]
        return arr[:i]
    
    bob = 1
    while len(arr) !=0:
        j = max(arr)
        if j == arr[-1]:
            arr = arr[:-1]
        else:
            #iterate the fuction
            arr = max_cuter(arr,j)
        bob = 0 if bob ==1 else 1
    res = 'BOB' if bob ==0 else'ANDY'
    return res

# This function or part of the code works very well, but this function only passes 18 out of 22 tests because it consumes a lot of time and is inefficient. So, I decided to work with AI and ask how to optimize it, but no solution passed all the tests.
# So, I decided to ask how the algorithm works. It told me that the problem works with local maximums, which means that the winner is decided by the number of local maximums and here its the optimal solution
#optimal code

def gamingArrayv2(arr):
    turn_counter = 0
    current_max = -1
    for num in arr:
        if num > current_max:
            current_max = num
            turn_counter += 1
    if turn_counter % 2 == 1:
        return 'BOB'
    else:
        return 'ANDY'

