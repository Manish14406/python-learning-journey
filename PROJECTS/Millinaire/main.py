questions = [
    ["Who is the father of nation","Gandhi","Kohli","Asad","Vignesh",1],
    ["Who is the chief minister of karnataka","Manish","asad","Siddhu","anni",3],
    ["Who is the God of cricket","Manish","Kohli","Siddhu","anni",2],
    ["What amount manish is gonna earn in 5 years",100000,1000000,10000000,100000000,3]   
]

prize = [100000,1000000,10000000,100000000,1000000000]
i = 0
for question in questions:
    print(question[0])
    print(f"{question[1]}")
    print(f"{question[2]}")
    print(f"{question[3]}")
    print(f"{question[4]}")
    

    o = int(input("Enter your option a,1 b,2 c,3 d,4\n"))
    if(question[5] == o ):
        print("Well done you are right ")
    else:
        print("Better luck next time\n")
        break
    print(f"You won {prize[i]}")
    i += 1



