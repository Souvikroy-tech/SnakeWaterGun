import random
'''1 for snake 
-1 for water
0 for gun'''
computer=random.choice([-1,0,1])
print("welcome to Souvik's Snake Water Gun game ")
youstr=input("enter your choice:")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]
reverseDict={1:"Snake 🐍 ",-1:"Water 💧",0:"Gun 🔫"}
you=youDict[youstr]
print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")
if(computer==you):
    print("it is a draw")

else:
     if(computer==-1 and you==1):
       print("you win")
     elif(computer==-1 and you==0):
       print("you Lose,")
       print("better luck next time")
     elif(computer==1 and you==-1):
        print("you lose ")
        print("better luck next time")
     elif(computer==1 and you==0):
       print("you win")
     elif(computer==0 and you==-1):
       print("you win ")
     elif(computer==0 and you==1):
       print("you lose")
       print("better luck next time")
     else:
        print("something went wrong")
