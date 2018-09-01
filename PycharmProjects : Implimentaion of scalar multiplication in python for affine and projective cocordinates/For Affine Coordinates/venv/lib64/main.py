from Generatingrandampair import generate_pair
from scalarmultiply import scalarmul
from MontgomeryLadder import Laddermul
from MontgomeryLadder import addition
from math import floor, log
#
# x=2584540251645844119023635113483687168443344497143065558751856691718414629056
# y=8375321931858534703418566108223069725829582564511224108129331797144837349125
# mod=17063482187052379080552723004438836893372321876860205224769132319301969934533
#
# lg=floor(log(mod,2))
#
# print(lg)
#
# kop=pow(2,lg+1)-mod
# print(kop)
# #
# x=38047054882076
# y=3677697189453
# mod=47652104678677
#


# for i in range(1,17):
#     xq, yq, fl = Laddermul(x, y, 0, i, mod)
#     print(xq, i,yq)
# xq,yq,fl=scalarmul(x,y,0,4,mod)

# x3,y3,fl=Laddermul(x,y,0,4,mod)
#
# print(x3,y3,fl)
#
# xf,yf,ff=Laddermul(x,y,0,3,mod)
# x3,y3,f3=addition(xf,yf,ff,x,y,0,mod)
#
#
# print(x3,y3,f3)


# print(xq,yq)
# print(yq)

# x=3940227118348513269
# y=5731219420740105197
mod = 9229441602667391461
mod=15814258796624810360418844203185563659026808661
X=-1739
X = 60167461
t = X + 1

NumberofE = mod + 1 - t

Orderby4 = NumberofE // 4
# fi,sc,fl=scalarmul(x,y,Orderby4,mod);
# fi1,sc1,fl1=scalarmul(fi,sc,4,mod);
#
# print(fi);
# print(sc);
# print(fi);
# print(sc);
cnt=0;
while(1):
    cnt=cnt+1
    x,y=generate_pair(mod)
    x1,y1,fl=Laddermul(x,y,0,Orderby4,mod)

    xq,yq,fl=Laddermul(x1,y1,0,4,mod)
    # print(cnt)
    if fl==1:
        print(x,end=' ')
        print("lol ",end=' ')
        print(y)
        break
print("First qx1")
print(x)

print("first qy1")
print(y)


print("Flag")

print(fl)

#checking point is ok or not
print((x**3+1)%mod)
print((y**2)%mod)



