"""pink fluffy unacorns mogel"""
import colors as c
from utils import ask



intro = c.magenta + '''
welcome to the pink fluffy unicorn quiz.
'''

def q1():
    color = ask("what color are the unicons?")
    if color == "pink":
        print("And it is such a beautiful color.")
        return True
    print("Nope.")
    return False



def q2():
    answer = ask("what are the unicons dancing on")
    if answer.startswith("rainbow"):
        print("And it is such a beautiful rainbow.")
        return True
    print("Nope.")
    return False
    

def q3():
    smiles = ask("name one word that descivs the magica fur thear made of")
    if smiles.startswith("smile"):
        print("yep.")
        return True
    print("Nope")
    return False

questions = [q1,q2,q3]
