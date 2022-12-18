
L = [45]

def calculate_L(i):
    # L[0] sum of digits of number from 0..9
    # L[1] sum of digits of number from 10..99
    global L
    temp_sum = 0
    for k in range(0, i):
        temp_sum += L[k]
    L.append( (L[0] * pow(10, i)) + (temp_sum * 10) )
    return L[i]


if __name__ == "__main__":
    print(calculate_L(1))
    print(calculate_L(2))
    print(L[0] + L[1] + L[2])
    line = input().split()
    L = int(line[0])
    R = int(line[1])






