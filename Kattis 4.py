
import random


def solve():
    n = int(input())
    output = "4"
    output_value = 4

    if (n == 0):
        return "4 * 4 - 4 * 4" + " = " + str(n)
    # First iteration
    if output_value * 4 <= n + 1:
        output += " * 4"
        output_value *= 4
    elif output_value + 4 <= n + 1:
        output += " + 4"
        output_value += 4
    else:
        return "no solution"

    # Second iteration

    if output_value == n:
        output += " + 4 - 4"
        return output + " = " + str(n)
    elif output_value == n - 1:
        output += " + 4 / 4"
        return output + " = " + str(n)
    elif output_value == n + 1:
        output += " - 4 / 4"
        return output + " = " + str(n)
    elif output_value*4 <= n:
        output += " * 4"
        output_value *= 4
    elif output_value+16 < n:
        return "no solution"
    elif output_value + 16 ==n:
        return output + " + 4 * 4" + " = " + str(n)
    elif output_value + 8 == n:
        return output + " + 4 + 4" + " = " + str(n)
    else:
        return "no solution"

    # Third iteration
    if output_value + 4 == n:
        return output + " + 4" + " = " + str(n)
    elif output_value - 4 == n:
        return output + " - 4" + " = " + str(n)
    elif output_value * 4 == n:
        return output + " * 4" + " = " + str(n)
    else:
        return "no solution"





if __name__ == '__main__':
    # https://open.kattis.com/problems/4thought
    m = input()
    i = 0
    while i<m:
        print(solve())
        i+=1


