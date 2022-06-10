print("Welcome! You're up for an incredible gaming adventure.")
print("Are you ready?")

Gaming= True
print("The Battle is On! See if you can beat the Rock, Paper, Scissors Ninja.")

while Gaming:
    import random

    user= str(input("Pick any of the Following {R, P, S}: "))
    selection= ["R", "P", "S"]
    computer = random.choice(selection)
    print( "Player (" + user + ") : CPU (" + computer + ")")
    
    if computer== "R" and user== "R":
        print("It's a tie!")
    
    elif computer=="P" and user== "P":
        print("It's a tie!")   
 
    elif computer== "S" and  user=="S":
        print("It's a tie!")
 
    elif computer=="R" and user=="S":
        print("CPU wins")
        Gaming= False
    elif computer=="S" and user=="R":
        print("Player wins")
        Gaming= False
    elif computer=="P" and user=="S":
        print("Player wins")
        Gaming= False
    elif computer=="S" and user=="P":
        print("CPU wins")
        Gaming= False
    elif computer=="P" and user=="R":
        print("CPU wins")
        Gaming= False
    elif computer=="R" and user=="P":
        print("Player wins")
        Gaming= False
    else:
        print("Wrong Move, Try Again.")
        
