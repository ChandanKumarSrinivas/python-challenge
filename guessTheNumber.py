import random

def guess(x):
    randomNumber=random.randint(1,x)
    guess=0
    while guess != randomNumber:
        guess=int(input(f"Guess a number between 1 and {x}: "))
        if guess < randomNumber:
            print("Sorry, guess again. Your guess was too low.")
        elif guess > randomNumber:
            print("Sorry, guess again. Your guess was too high.")

    print(f"Gotcha, you have guessed the number {randomNumber} corretly!!")

if __name__ =="__main__":
    guess(int(input("give a limit: ")))