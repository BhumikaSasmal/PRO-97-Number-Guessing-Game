import random
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 and 9")

while chances <5:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print ("Congratulations!! YOU WON!")
        break
    
    elif guess<number:
        print("Your guess was too low. Try again!")
    
    else: 
        print("Your guess was too high. Try Again!")
    chances += 1

if not chances<5:
    print("YOU LOSE! The number is ", number)


