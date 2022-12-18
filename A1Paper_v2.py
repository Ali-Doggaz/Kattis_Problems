

tape = 0

def recursion(L, long_side, small_side, needed):
    global tape

    if len(L)==1:
        if L[0]>=needed:
            tape += long_side * (needed / 2)
            return tape
        else:
            return None

    #If we have more than 1 element in our list

    if L[0] >= needed:
        tape += long_side * (needed / 2)
        return tape
    else:
        tape += long_side * (needed / 2)
        needed -= L[0]
        return recursion(L[1:], small_side, long_side/2, needed*2)




if __name__ == "__main__":


    small_side = pow(2, -5 / 4)
    long_side = pow(2, -3 / 4)

    n = int(input())
    L = input().split()
    L = [int(item) for item in L]

    answer = recursion(L, long_side, small_side, 2)
    if answer is None:
        print("impossible")
    else:
        print(answer)