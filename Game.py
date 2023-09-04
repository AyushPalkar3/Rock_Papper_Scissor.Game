#Lets do it !
import random 

u=0
m=0
def score(m,u):
    print("Your Score is",u)
    print("Macine score is",m)
    print("------------------------------------------")
    
options= ["rock","paper","scissor"]
while(True):
    usr=input("Enter your option Rock/Papper/Scissor or q to quit ").lower()
    if (usr=="q"):
        break
    elif usr not in options:
        continue 
    
    comp=random.randint(0,2)
    computer=options[comp]
    print("******************************************")
    print("Computer choosed",computer)
    print("******************************************")
    if computer==usr:
        print("Its Tie")
        score(m,u)
    elif computer=="rock"and usr=="scissor":
        m+=1
        score(m,u)
    elif computer=="scissor"and usr=="paper":
        m+=1
        score(m,u)
    elif computer=="paper"and usr=="rock":
        m+=1
        score(m,u)
    else:
        u+=1
        score(m,u)
    
score(m,u)
if m>u:
        print("Machine Wins")
elif m<u:
        print("You are Winner")
else: print("Its a Tie")