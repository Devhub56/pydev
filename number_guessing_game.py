import random

def guess_number (x):
    number = random.randint(1,x)
    user_guess = 0
    
    while user_guess != number :
        user_guess = int(input("Enter a number between 1 and 100")) # modify to suit your upper limit argument when calling the function
        if user_guess > number :
            print (f"You entered {user_guess} , which is higher than the number, please try again with a smaller number")
        if user_guess < number :
             print (f"You entered {user_guess} , which is lower than the number, please try again with a bigger number")
    print (f"Yay, you guessed {number} correctly..")
    
guess_number(100)

### Now time for the computer to guess the user's secret  number :

print ("Now Think of a number Between 1 and 30 and let let the computer guess your number")#can be modified to meet any limit arguments when calling the function below
def computer_guess (y):
    low = 1
    high = y
    user_feedback = ""
    while user_feedback != "c":
        random_number = random.randint(low,high)
        user_feedback =input(f'Is {random_number} high (H),Low (L) or Correct (C)?').lower() # takes care of any upper case entry
        if user_feedback == 'h':
            high = random_number-1
        if user_feedback == 'l':
             low = random_number + 1
    print(f'Yay! The computer correctly guessed {random_number}.Which was your secret number!')
computer_guess (30)
    
