
import random

if __name__ == '__main__':
   # Generate a random number between 1 and 10
   n = random.randint(1, 10)
   guess = -1
   while(guess != n):
       print("Please input your guess (between 1 and 10): ")
       guess = int(input())

   print("Congratulations, you guessed it!")
