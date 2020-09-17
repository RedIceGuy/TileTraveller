# Github repository:
# https://github.com/RedIceGuy/TileTraveller

# Algorithm
# 1. Skapa reitina (1,1; 1,2...) 
# 2. Slá inn átt
# 3. Gá hvort það sé veggur
# 4. Halda áfram ef enginn veggur
# 5. Reyna aftur ef það er veggur

def direction():
    direction = input("Direction: ")
    return direction

def Reitur_1_1():
    print("You can travel: (N)orth.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        return direction
    else:
        print("Not a valid direction!")
        return False

def Reitur_1_2():
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        return direction

    elif direction == "e" or direction == "E":
        return direction

    elif direction == "s" or direction == "S":
        return direction
    
    else:
        print("Invalid direction")
        Reitur_1_2()


def Reitur_1_3():
    print("You can move (E)ast or (S)outh.")
    direction = input("Direction: ")
    if direction == "E" or direction == "e":
        return direction
    
    elif direction == "S" or direction == "s":
        return direction

    else:
        print("Not a valid direction!")
        Reitur_1_3()

def Reitur_2_1():

    direction = direction()

def Reitur_2_2():

    direction = direction()

def Reitur_2_3():

    direction = direction()

def Reitur_3_1():
    # Victory
    print("Victory!")

def Reitur_3_2(direction):

    direction = direction()
    if direction == "n" or direction == "N":


def Reitur_3_3(direction):

    direction = direction()
"""
def move(func):
    func
    while not func:
        func

"""
win = False

if not Reitur_1_1():
    Reitur_1_1()

if Reitur_1_2() == "n" or Reitur_1_2() == "N":
    Reitur_1_3

