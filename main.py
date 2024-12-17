import random
import time
number = random.randint(1,100)
if(number%2==0):
    x="even"
else:
    x="odd"
print("This is an {} number".format(x))
time.sleep(.5)
print("Guess it!")
def pick():
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(.25)
        enter = input("Guess: ")
        try:
            guess = int(enter)
            if guess<= 100 and guess>= 1:
                guessesTaken = guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                        print("Too low")
                    if guess>number:
                        print("Too high")
                    if guess != number:
                        print("Try again")
                    if guess== number:
                        break
            if guess>100 or guess<1:
                print("Out of range")
        except: 
            print('It is not the nuumber.')
    if guess == number:
        guessesTaken = str(guessesTaken)
        print("Good job")
    if guess !=  number:
        print("I did not think that!")
playagain = "Y"
while playagain == "Y"  or playagain == "y":
    pick()
    print("Do you want to play again?")
    playagain = input()


