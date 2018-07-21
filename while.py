answer=25
q="what no. am I thinking?"
print("lets play a game")
while True:
    guess=int(input(q))
    if(guess<answer):
        print("A little higher")
    elif(guess>answer):
        print("A little lower")
    else:
       print("You got it!")
       break;