from math import floor, log
def BigMod(base,pwr,mod):
    ret=1
    base=(base%mod+mod)%mod
    while pwr>0:
        if pwr%2==1:
            ret=(ret*base)%mod
        pwr=pwr//2
        base=(base*base)%mod
    return ret

def validaty(x,y,fl,mod):
    if((y**2)%mod==(x**3+1)%mod):
        return x,y,fl
    else :
        return 0,0,1


def doubling(x1,y1,fl,mod):
    m = 1
    if fl == 1:
        return x1, y1, fl
    elif  y1 == ((mod - y1) % mod + mod) % mod:
        return 0, 0, 1
    else:

        m = (x1 * x1 * 3) % mod
        m = (m * BigMod(y1 * 2, mod - 2, mod)) % mod
        xx1 = ((m * m - x1 - x1) % mod + mod) % mod
        xy1 = ((m * (x1 - xx1) - y1) % mod + mod) % mod
        return validaty(xx1, xy1, 0, mod)

def addition(x1,y1,fl,x2,y2,fl1,mod):
    m=1
    if fl==1:
        return x2,y2,fl1
    elif fl1==1:
        return x1,y1,fl
    elif x1==x2 and y1==((mod-y2)%mod+mod)%mod:
        return 0,0,1
    else:
        if x1==x2 and y1==y2:
            m=(x1*x1*3)% mod
            m=(m*BigMod(y1*2,mod-2,mod))%mod

        else :
            m=((y2-y1)%mod+mod)%mod
            m=(m*BigMod(x2-x1,mod-2,mod))%mod

        # print("for m",end=' ')
        # print(m)
        xx1=((m*m-x1-x2)%mod+mod)%mod
        xy1=((m*(x1-xx1)-y1)%mod +mod )%mod
        return validaty(xx1,xy1,0,mod)

def Laddermul(px,py,f,ord,mod):
    Rx=0
    Ry=0
    fl=1
    R1x=px
    R1y=py
    fl2=f
    po=floor(log(ord,2))+1
    while(po>=0):

        if ord&(1<<po)==0:
            R1x,R1y,fl2=addition(Rx,Ry,fl,R1x,R1y,fl2,mod)
            Rx,Ry,fl=doubling(Rx,Ry,fl,mod)
        else :
            Rx, Ry, fl = addition(Rx, Ry,fl, R1x, R1y,fl2, mod)
            R1x, R1y, fl2 = doubling(R1x, R1y,fl2, mod)

        # px,py,fl=addition(px,py,px,py,mod)
        po=po-1

        # print(ord)
        # print(px,end='lo ')
        # print(py)
        # print(Ax,end='lo1 ')
        # print(Ay)
    return Rx,Ry,fl
