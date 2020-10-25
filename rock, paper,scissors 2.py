import random 
from random import randint
symbol=['ROCK','PAPER','SCISSORS']
cpu=symbol[randint(0,2)]
def play():
    player=input("enter your name")
    print("Let's Start",player)
    print("Press R,P or S on your keyboard to choose ROCK , PAPER or SCISSORS respectively.")
    #print(player,"Enter your choice")
    #choice=input()
    c=1
    while c==1:
        print(player,"enter your choice")
        choice=input()
        if(choice==cpu):
            print("tie")
        elif(cpu=="ROCK"):
            if(player=="PAPER"):
                print(player," you win")
            else:
                print("CPU wins")
        elif(cpu=="PAPER"):
            if(player=="ROCK"):
                print("CPU wins")
            else:
                print(player," wins")
        elif(cpu=="SCISSORS"):
            if(player=="ROCK"):
                print(player," wins")
            else:
                print("CPU wins")
        else:
            print("YOU ENTERED WRONG CHOICE")
            
        c=int(input("press 1 to continue and 0 to exit the game."))
        if c==0:
            print("THANK YOU", player)
        
        
            
                
        
    
    

