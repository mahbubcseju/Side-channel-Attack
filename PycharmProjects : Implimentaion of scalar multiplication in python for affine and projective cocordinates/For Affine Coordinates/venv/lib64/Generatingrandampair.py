
import random
from stonelli import tonelli
def my(mod):


    x=random.randint(0,mod-1)
   # y=random.randint(0,mod-1)
    return x



def generate_pair(mod):


    while(1):
        x = my(mod)
        y2=x**3+1
        y2=y2%mod
        y=tonelli(y2,mod)

        if y!=-1 :
            break


    # So We got Pair here
    return x,y