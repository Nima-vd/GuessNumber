import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
         guess = input('Guess a number between 1 and {x}')
         if guess < random_number: 
          print("sorry,guess again.Too low")
         if guess > random_number:
            print("Sorrry,guess again.Too high")

    print(f'Yay,Congrats.You have guessed the number correct')

def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != 'c':
        if low != high:
         guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'is {guess} too high (H), too low (L), or corret (c)??').lower()
        if feedback == 'h':
             high = guess - 1
        elif feedback == 'l':
             low = guess + 1

    print(f'Yay!The computer guessed your number,{guess},correctly')

computer_guess(1000)  