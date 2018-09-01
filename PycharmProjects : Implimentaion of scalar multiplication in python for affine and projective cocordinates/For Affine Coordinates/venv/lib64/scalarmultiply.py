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
        return x,y,0
    else :
        return x,y,1
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

def scalarmul(px,py,fl,ord,mod):
    Ax=0
    Ay=0
    fl1=1;
    while(ord>0):
        if ord%2==1:
            Ax,Ay,fl1=addition(Ax,Ay,fl1,px,py,fl,mod)
        px,py,fl=addition(px,py,fl,px,py,fl,mod)
        ord=ord//2
        # print(px,end='lo ')
        # print(py)
        # print(Ax,end='lo1 ')
        # print(Ay)
    return Ax,Ay,fl1
