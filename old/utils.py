"""use this!!!!!!!!!!!"""

import colors as c


def ask(question):
    print(question)
    answer = input('-->').lower().strip()
    return answer



if __name__== '__main__':
   print(c.clear)
   name = ask("what is your name?")
