from random import randint

print("Enter two numbers between which you wanna play guess the number.")
a,b=map(int,input().split())
guess_number=randint(a,b)
user_input=-1
tries=1

while guess_number!=user_input:
    print("No. of Tries: {}".format(tries))
    user_input=int(input("\n\nGuess a random number between {} and {}: ".format(a,b)))
    if user_input < guess_number:
        print("\n\nWell! Your number is less than mine, obviously!.")
    elif user_input > guess_number:
        print("\n\nOhh! You think your number would be bigger than mine?")
    else:
        print("\n\nOHH!! AMAZING GUESS, The number is {}. YOU WON in {} tries, LOSER!".format(guess_number,tries))
    tries+=1
