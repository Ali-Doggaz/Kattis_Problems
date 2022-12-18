

tape = 0

def recursion(L, long_side, small_side):
    global tape
    if len(L)==1:
        if L[0]>=2:
            tape += long_side
            return [L[0] - 2]
        else:
            return None

    if L[0] >= 2:
        tape += long_side
        L[0] = L[0] - 2
        return L

    temp_list = recursion(L[1:], small_side, long_side / 2)
    if temp_list == None:
        return None

    if L[0] == 1:
        tape += long_side
        L[0] = 0
        L[1:] = [elem for elem in temp_list]
        return L

    elif L[0] == 0:
        tape += long_side

        L[1:] = [elem for elem in temp_list]
        temp = recursion(L[1:], small_side, long_side / 2)
        if temp == None:
            return None
        else:
            L[0] = 0
            L[1:] = [elem for elem in temp]
            return L


if __name__ == "__main__":


    small_side = pow(2, -5 / 4)
    long_side = pow(2, -3 / 4)

    n = int(input())
    L = input().split()
    L = [int(item) for item in L]

    if L[0] >= 2:
        tape += long_side
        print(tape)
    elif L[0] == 1:
        temp = recursion(L[1:], small_side, long_side / 2)
        if temp == None:
            print("impossible")
        else:
            tape += long_side
            print(tape)
    else:
        temp = recursion(L[1:], small_side, long_side / 2)

        if temp == None:
            print("impossible")
        else:
            L[1:] = temp
            temp = recursion(L[1:], small_side, long_side / 2)
            if temp == None:
                print("impossible")
            else:
                tape += long_side
                print(tape)