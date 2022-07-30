import math
import random


A = int(input("enter the lower bound :- "))
B = int(input("enter the upper bound :- "))

X = random.randint(A,B)
s = abs(A - B + 1)

print("\n YOU HAVE THE CHANCE",math.log2(s))

count = 0

while count < math.log2(s):
      count += 1
      Guess = int(input(" Guess the number :-"))
              
      if X == Guess:
         print("congratulation you did it",count,"try again")
         break

      elif X < Guess:
         print("try again , your guess is to high")
      elif X > Guess:
         print("try again , your guess is to small")
  

if count >= math.log2(s):
     print("\n Finally number is %d"%X)
     print("\t Better Luck Next time !!!")
