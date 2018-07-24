print("A program to Troubleshoot Computer Power failure.\n")
answer='Y'
print("________________________\n")
question="Is Power cord connected to power socket:   "
print("Type Y for Yes, N for no\n")

while True:
    g=(input(question))
    if(g==answer):
        print("Press the ON SWITCH, TYPE Y for POWERED ON or N for OFF\n")
        question1="IS THE COMPUTER POWERED UP:   "
        g1=input(question1)
        if(g1==answer):
            print("HURRAY THE COMPUTER SWITCHED ON")
            print("_________________________________\n")
            break;
        elif(g1!=answer):
            print("The COMPUTER NEEDS REPAIR")
            print("__________________________\n")
            break;

    elif(g!=answer):
        print("Plug the Computer into the Power Socket")
        print("Does the Computer Power Up:   ")
        question2="Press ON/OFF Switch:    "
        
        g2=input(question2)
        if(g2==answer):
            print("CONGRATULATIONS Computer Fixed")
            print("__________________________\n")
            break;
        else:
            print("COMPUTER Needs REPAIR")
            print("__________________________\n")
            break;         

