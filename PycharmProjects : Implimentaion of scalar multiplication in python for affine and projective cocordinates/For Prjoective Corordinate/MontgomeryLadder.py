from math import floor, log
def bigmod(base,pwr,mod):
    ret=1
    base=(base%mod+mod)%mod
    while pwr>0:
        if pwr%2==1:
            ret=(ret*base)%mod
        pwr=pwr//2
        base=(base*base)%mod
    return ret


def checking_similiarity(fx,mod):
    return bigmod(fx,mod-2,mod)

def validity(x,y,z,fl,mod):
    if(fl==1):
        return 0,0,1,1
    le=z*(y*y)%mod
    le=le%mod
    ri=(bigmod(x,3,mod)+bigmod(z,3,mod))%mod

    if(le==ri):
        return x,y,z,0
    else :
        return 0,0,1,1


def doubling(x1,y1,z1,fl,mod):
    if fl==1:
        return 0,0,1,1
    if y1==0:
        return 0,0,1,1
    t=(x1*x1*3)%mod
    u=(y1*z1*2)%mod
    v=(u*x1)%mod*y1*2
    v%=mod
    w=t*t-v*2
    w=(w%mod+mod)%mod
    xa=(u*w)%mod
    ya=t*(v-w)-(u*u)%mod*(y1*y1)%mod*2
    ya=(ya%mod+mod)%mod
    za=bigmod(u,3,mod)
    #
    # w=(3*x1*x1)%mod
    # s=(y1*z1)%mod
    # b=((x1*y1)%mod*s)%mod
    # h=(w*w-8*b)%mod
    # h=(h+mod)%mod
    # xa=(2*h*s)%mod
    # ya=w*(4*b-h)-8*((y1*y1)%mod)*((s*s)%mod)
    # ya=(ya%mod+ya)%mod
    # za=8*s*((s*s)%mod)
    # za=za%mod
    return validity(xa,ya,za,0,mod)

def addition(x1,y1,z1,f1,x2,y2,z2,f2,mod):

    if f1==1:
        return x2,y2,z2,f2
    if f2==1:
        return x1,y1,z1,f1

    u1=(y2*z1)%mod
    u2=(y1*z2)%mod
    v1=(x2*z1)%mod
    v2=(x1*z2)%mod
    if v1==v2:
        if(u1!=u2):
            return 0,0,0,1
        else:
            return doubling(x1,y1,z1,f1,mod)

    u=(u1-u2)
    u=(u%mod+mod)%mod
    v = (v1 - v2)
    v= (v % mod + mod) % mod
    w=(z1*z2)%mod
    A=((u*u)%mod)*w-bigmod(v,3,mod)-2*((v*v)%mod)*(v2%mod)
    A=(A%mod+mod)%mod
    x3=(v*A)%mod
    y3=u*(((v*v)%mod)*v2-A)-(bigmod(v,3,mod)*u2)%mod
    y3=(y3+mod)%mod
    z3=(bigmod(v,3,mod)*w)%mod
    return validity(x3,y3,z3,0,mod)

def Laddermul(px,py,pz,f,ord,mod):
    Rx=0
    Ry=0
    Rz=1
    fl=1
    R1x=px
    R1y=py
    R1z=pz
    fl2=f
    po=floor(log(ord,2))+1
    while(po>=0):

        if ord&(1<<po)==0:
            R1x,R1y,R1z,fl2=addition(Rx,Ry,Rz,fl,R1x,R1y,R1z,fl2,mod)
            Rx,Ry,Rz,fl=doubling(Rx,Ry,Rz,fl,mod)
        else :
            Rx, Ry,Rz,fl = addition(Rx, Ry,Rz,fl, R1x, R1y,R1z,fl2, mod)
            R1x, R1y,R1z,fl2 = doubling(R1x, R1y,R1z,fl2, mod)

        # px,py,fl=addition(px,py,px,py,mod)
        po=po-1

        # print(ord)
        # print(px,end='lo ')
        # print(py)
        # print(Ax,end='lo1 ')
        # print(Ay)
        mdi=checking_similiarity(Rz,mod)
        Rx=(Rx*mdi)%mod
        Ry=(Ry*mdi)%mod
        Rz=(Rz*mdi)%mod
    return Rx,Ry,Rz,fl
