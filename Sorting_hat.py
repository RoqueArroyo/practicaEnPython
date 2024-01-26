Gryffindor = 0
Ravenclaw = 0 
Hufflepuff = 0
Slytherin = 0

print("Q1) Do you like Dawn or Dusk? (response with the number of your selection)\n")
Q1 = int(input("1)Dawn      \n2)Dusk\n"))
if Q1 == 1: 
    Gryffindor = Gryffindor + 1 
    Ravenclaw = Ravenclaw + 1
elif Q1 == 2: 
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1 
else: 
    print('Wrong input you sucker')

print("Q2) When I’m dead, I want people to remember me as:\n")
Q2 = int(input("1) The Good     \n2) The Great      \n3) The Wise    \n4) The Bold\n"))
if Q2 == 1: 
    Hufflepuff = Hufflepuff + 2
elif Q2 == 2: 
    Slytherin = Slytherin + 2
elif Q2 == 3:
    Ravenclaw = Ravenclaw + 2
elif Q2 == 4: 
    Gryffindor = Gryffindor + 2 
else: 
    print('Wrong input you sucker')    

print("Q3) Which kind of instrument most pleases your ear?\n")
Q3 = int(input("1) The violin    \n2) The trumpet    \n3) The piano    \n4) The drum\n"))
if Q3 == 1: 
    Slytherin = Slytherin + 4
elif Q3 == 2: 
    Hufflepuff = Hufflepuff + 4
elif Q3 == 3:
    Ravenclaw = Ravenclaw + 4
elif Q3 == 4: 
    Gryffindor = Gryffindor + 4 
else: 
    print('Wrong input you sucker') 

choosenhouse = max(Ravenclaw,Slytherin,Hufflepuff,Gryffindor)

if  choosenhouse == Ravenclaw: 
    print("you're in Ravenclaw\n")
elif    choosenhouse == Gryffindor: 
    print("you're in Gryffindor\n") 
elif    choosenhouse == Hufflepuff: 
    print("you're in Hufflepuff\n")
else:
    print("you filthy Slytherin\n")