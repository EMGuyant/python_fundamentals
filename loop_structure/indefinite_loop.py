#Programming Exercise #8
#   This programs implements a game of mentally summing 
#   two random numbers between 1-100.

import random

def main() :
    # Generate two random numbers between 1 and 100
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)

    # Ask the answer
    print("What is the sum:",n1,"+",n2)
    attempt = 1
    answer = int(input("Answer: "))

   # complete the rest
   #correct Answer variable used for determination of whether user answer is correct and break indefinite loop
    correctAnswer = False
    
    while correctAnswer == False:
        if answer == (n1+n2):
            correctAnswer = True
            print("Yes! " + str(answer) +" is the correct answer. \nYou got it in " + str(attempt) + " attempts.")
        elif answer < (n1+n2):
            print("Wrong! The correct answer is greater than " + str(answer))
            attempt += 1
            
            answer = int(input("Answer: "))

        elif answer > (n1+n2):
            print("Wrong! The correct answer is less than " + str(answer))
            attempt += 1
            
            answer = int(input("Answer: "))
  
main()
