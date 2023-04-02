# A simple game of stone, paper and secsior
import random

def result(comp,user):
    if((comp==0 and user==0) or (comp==1 and user==1) or (comp==2 and user==2)):
        print("DRAW")
        
    elif((comp==0 and user==1) or (comp==1 and user==2) or (comp==2 and user==0)):
        print("you won")    
        
    else:
        print("you lose")    
            

user = int(input("Enter 0 for stone , Enter 1 for paper , Enter 2 for secsior\n"))
comp = random.randint(0,2)

print("You choose",user)
print("Computer generate",comp)

result(comp,user)
