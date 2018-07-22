print("A program to Troubleshoot Computer Power failure.\n")
answer='Y'
print("________________________\n")
question="Is Power cord connected to power socket"
print("Type Y for Yes, N for no\n")

while True:
    g=(input(question))
    if(g==answer):
        print("Press the ON SWITCH, TYPE Y for POWERED ON or N for OFF\n")
        question1="IS THE COMPUTER POWERED UP"
        g1=input(question1)
        if(g1==answer):
            print("HURRAY THE COMPUTER SWITCHED ON")
            print("_________________________________\n")
            break;
        elif(g1!=answer):
            print("The COMPUTER NEEDS REPAIR")
            print("__________________________\n")
            break;

    else:
        print("Get COMPUTER REPAIRED")
        print("__________________________\n")
        break;         