# Github repository:
# https://github.com/RedIceGuy/TileTraveller

# Algorithm
# 1. Skapa reitina (1.1; 1.2...) 
# 2. Slá inn átt
# 3. Gá hvort það sé veggur
# 4. Halda áfram ef enginn veggur
# 5. Reyna aftur ef það er veggur
# 6. Stoppa þegar leikmaður kemst í reit 3_1

def Reitur_1_1():
    print("You can travel: (N)orth.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        Reitur_1_2()

    else:
        print("Not a valid direction!")
        Reitur_1_1()

def Reitur_1_2():
    # N, S, E
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        Reitur_1_3()

    elif direction == "e" or direction == "E":
        Reitur_2_2()

    elif direction == "s" or direction == "S":
        Reitur_1_1()
    
    else:
        print("Not a valid direction!")
        Reitur_1_2()


def Reitur_1_3():
    # S, E
    print("You can move (E)ast or (S)outh.")
    direction = input("Direction: ")
    if direction == "E" or direction == "e":
        Reitur_2_3()
    
    elif direction == "S" or direction == "s":
        Reitur_1_2()

    else:
        print("Not a valid direction!")

def Reitur_2_1():
    print("You can move (N)orth.")
    # N
    direction = input("Direction: ")
    if direction == "N" or direction == "n":
        Reitur_2_2()
    
    else:
        print("Not a valid direction!")
        Reitur_2_1()


def Reitur_2_2():
    print("You can move (S)outh or (W)est.")
    # S, W
    direction = input("Direction: ")
    if direction == "S" or direction == "s":
        Reitur_2_1()
    
    elif direction == "W" or direction == "w":
        Reitur_1_2()
    
    else:
        print("Not a valid direction!")
        Reitur_2_2()

def Reitur_2_3():
    print("You can move (E)ast or (W)est")
    # W, E
    direction = input("Direction: ")
    if direction == "W" or direction == "w":
        Reitur_1_3()
    
    elif direction == "E" or direction == "e":
        Reitur_3_3()

    else:
        print("Not a valid direction!")
        Reitur_2_3()

def Reitur_3_1():
    # Victory
    print("Victory!")

def Reitur_3_2():
    print("You can move (N)orth or (S)outh.")
    # N, S
    direction = input("Direction: ")
    if direction == "N" or direction == "n":
        Reitur_3_3()
    
    elif direction == "S" or direction == "s":
        Reitur_3_1()
    
    else:
        print("Not a valid direction!")
        Reitur_3_2()

def Reitur_3_3():
    print("You can move (S)outh or (W)est.")
    # W, S
    direction = input("Direction: ")
    if direction == "W" or direction == "w":
        Reitur_2_3()
    
    elif direction == "S" or direction == "s":
        Reitur_3_2()
    
    else:
        print("Not a valid direction!")
        Reitur_3_3()

Reitur_1_1()
