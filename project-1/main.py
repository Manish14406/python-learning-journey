'''
1 = snake
-1 = water
0 = gun
'''
import random
computer = random.choice([-1,0,1])

youstr=input("Enter your choice : ").lower()


youDic = {
    "water" : 1,
    "snake" : -1,
    "gun" : 0
}

reverseDic = {
    1:"water",-1:"snake",0:"gun"
}
you = youDic.get(youstr)
print(f"You choosed {youstr} and the computer choosed {reverseDic.get(computer)}")



if(computer == you):
    print("Its a draw!")
# else:
#     if(computer == 1 and you == 0): 
#         print("You loose")
#     if(computer == 1 and you == -1): 2
#         print("You win")
#     if(computer == -1 and you == 0): -1
#         print("You win")
#     if(computer == -1 and you == 1):
#         print("You loose")
#     if(computer == 0 and you == 1):
#         print("You loose")
#     if(computer == 0 and you == -1): -1
#         print("You win")
else:   
    if((computer - you)==  -1 or (computer-you)== 2):
        print("You win!!")
    else:
        print("You loose !")

    

       