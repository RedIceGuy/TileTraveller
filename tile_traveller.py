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

def Reitur_1_1(dir_str):
    print("You can travel: (N)orth.")
    direction = dir_str
    if direction == "n" or direction == "N":
        return True
    else:
        print("Not a valid direction!")
        return False
"""
def Reitur_1_2():

    direction = direction()

def Reitur_1_3():

    direction = direction()

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


move(Reitur_1_1(direction()))