if __name__ == '__main__':
# Problem link: https://open.kattis.com/problems/99problems
    N = input()
    N_int = int(N)
    if N_int<149:
        output = 99
    elif (N_int%100<49):
        output = (N_int-100) + (-int(N[-2:]) + 99)
    else:
        output = int(N[:-2])*100 + 99
    print(output)