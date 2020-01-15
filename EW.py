import sys

import numpy as np
import random

xr = 120
yr = 300
xj = 700
yj = 300
points = []

Pj = 0
# Km
d = 0
# Mhz
f = 1000
# dBm
pg =70 #10000w
#Pj = pg - (32.45 + 20 * np.log10(d) + 20 * np.log10(f))

NewPj = 10 ** Pj
pt = 400000# w
Gt = 10 ** 4  # b
Lmd = ((f * 1000000)/300000000)
s = 1
R = 0  # km
r=0

X=0
Y=0
xo=0
yo=0
reward=0
w, h = 4, 480000;
Q = [[0 for x in range(w)] for y in range(h)]
Points=[]
Action=[0,1,2,3]
def ReStart():
    X=random.choice(np.arange(800))
    Y=random.choice(np.arange(600))
    return X,Y
def DoAction(act,X,Y,xo,yo):
    distance = np.sqrt((X - xo) ** 2 + (Y - yo) ** 2)
    reward = 0
    #num = random.random()
    # # if (num < 0.1):
    #
    if(act==0):
        Y=Y-1
    elif(act==1):
        Y=Y+1
    elif (act == 2):
        X =X-1
    elif (act == 3):
        X =X+1
    distance2=np.sqrt((X-xo)**2+(Y-yo)**2)

    r = np.sqrt((X - xr) ** 2 + (Y - yr) ** 2)
    d = np.sqrt((xr - xj) ** 2 + (yr - yj) ** 2)
    KH = 0
    if (r > 0):
        if (np.abs(Y - yj) <= 100 and X > xr):
            Pj = (pg * (np.cos(np.abs((Y - yj) / 100.0) * (3.1415926 / 2))) - (
                    32.45 + 20 * np.log10(d) + 20 * np.log10(f)) + 40 * (
                      np.cos(np.abs((Y - yj) / 100.0) * (3.1415926 / 2))))
        else:
            Pj = -8000
        Pr = 10 * np.log10((pt * (Gt ** 2) * (Lmd ** 2) * 1) / (((4 * 3.1415926) ** 3) * ((r * 1000) ** 4))) + 30

        if Pr > -70 and Pr > Pj:
            KH = 1
    if (distance2 < distance and KH==1):
        reward = -30
    elif (distance2 >= distance and KH==1):
        reward = -1.8
    elif(distance2<distance):
        reward=-1
    else:
        reward=-2
    return X,Y,reward

def TestAction(X,Y,a):
    index = ReturnMaxIndex(a)
    B=(0,0,0,0)
    if random.random()<0.26:
        index = random.choice((0, 1, 2, 3))
    else:
        if (a == B):
            index = random.choice((0, 1, 2, 3))
        elif (a[0] == a[3] and index == 0):
            index = random.choice((0, 3))
        elif (a[1] == a[2] and index == 1):
            index = random.choice((1, 2))
    if (index == 0):
        Y=Y-1
    elif (index == 1):
        Y=Y+1
    elif (index == 2):
        X =X-1
    elif (index == 3):
        X =X+1
    return X,Y
def ReturnMaxIndex(a):
    return np.argmax(a)

# dddd=TestAction(100,100,[0,10,20,3])
# print(dddd)
print(ReStart())
print(ReStart())
print(ReStart())

# 这是一个简单的递归函数
def demo(n=0):
    try:
        demo(n+1)
    except:
        print(n)

demo()

group=[[1,2],[2,3],[3,4]]
#numpy转化
ar=np.array(group)
print(ar[:,1])
#Out:[2 3 4]