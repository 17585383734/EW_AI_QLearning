# _*_coding:utf-8_*_
import sys

import numpy as np
import pygame
from pygame.locals import *
from sys import exit
import EW
import random
SCREEN_SIZE = (800, 600)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | RESIZABLE, 32)
pygame.mixer.init()
pygame.mixer.music.load("二胡.mp3")
#sound=pygame.mixer.Sound('') 播放音效
#pygame.mixer.music.play(True,0)
background_image = 'back.png'
background = pygame.image.load(background_image).convert()
ShowName=False


xo = 150
yo = 230
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
ShowJamSingle=True
#Pr = (pt * Gt ** 2 * Lmd ** 2 * 1) / ((4 * 3.1415926) ** 3 * (R * 1000) ** 4)

for x in range(800):
    for y in range(600):
        r = np.sqrt((x - xr) ** 2 + (y - yr) ** 2)
        d = np.sqrt((xr - xj) ** 2 + (yr - yj) ** 2)

        if(r>0 ):
            if(np.abs(y-yj)<=100 and x>xr):
                Pj = (pg * (np.cos(np.abs((y - yj) / 100.0) * (3.1415926 / 2))) - (
                            32.45 + 20 * np.log10(d) + 20 * np.log10(f)) + 40 * (
                          np.cos(np.abs((y - yj) / 100.0) * (3.1415926 / 2))))
            else:
                Pj =-8000
            Pr = 10*np.log10((pt * (Gt ** 2) * (Lmd ** 2) * 1) / (((4 * 3.1415926) ** 3)*((r * 1000) ** 4)))+30

            if ShowJamSingle == True:
                if Pr > -70 and Pr > Pj:
                    points.append((x, y))

            else:
                if Pr > -70:
                    points.append((x, y))

            #if(np.abs(y-yj)<100):


def GetQ(x,y,reward):
    nX = 0
    nY = 0

    if(x<0 or x>800 or y<0 or y>600):
        return
    nx0, ny0, reward0 = EW.DoAction(0,x, y , EW.xo, EW.yo)
    nextRe0 = max(EW.DoAction(0, nx0, ny0, EW.xo, EW.yo)[2], EW.DoAction(1, nx0, ny0, EW.xo, EW.yo)[2],
                 EW.DoAction(2, nx0, ny0, EW.xo, EW.yo)[2], EW.DoAction(3, nx0, ny0, EW.xo, EW.yo)[2])
    EW.Q[x + y * 800][0] = reward0 + 0.9 * nextRe0
    nx1, ny1, reward1 = EW.DoAction(1, x, y, EW.xo, EW.yo)
    nextRe1 = max(EW.DoAction(0, nx1, ny1, EW.xo, EW.yo)[2], EW.DoAction(1, nx1, ny1, EW.xo, EW.yo)[2],
                 EW.DoAction(2, nx1, ny1, EW.xo, EW.yo)[2], EW.DoAction(3, nx1, ny1, EW.xo, EW.yo)[2])
    EW.Q[x + y * 800][1] = reward1 + 0.9 * nextRe1

    nx2, ny2, reward2 = EW.DoAction(2, x, y, EW.xo, EW.yo)
    nextRe2 = max(EW.DoAction(0, nx2, ny2, EW.xo, EW.yo)[2], EW.DoAction(1, nx2, ny2, EW.xo, EW.yo)[2],
                 EW.DoAction(2, nx2, ny2, EW.xo, EW.yo)[2], EW.DoAction(3, nx2, ny2, EW.xo, EW.yo)[2])
    EW.Q[x + y * 800][2] = reward2 + 0.9 * nextRe2

    nx3, ny3, reward3 = EW.DoAction(3, x, y, EW.xo, EW.yo)
    nextRe3 = max(EW.DoAction(0, nx3, ny3, EW.xo, EW.yo)[2], EW.DoAction(1, nx3, ny3, EW.xo, EW.yo)[2],
                 EW.DoAction(2, nx3, ny3, EW.xo, EW.yo)[2], EW.DoAction(3, nx3, ny3, EW.xo, EW.yo)[2])
    EW.Q[x + y * 800][3] = reward3 + 0.9 * nextRe3

    mr=max(reward0,reward1,reward2,reward3)


    if random.random()<0.16:
        return random.choice(((nx0,ny0,reward0),(nx1,ny1,reward1),(nx2,ny2,reward2),(nx3,ny3,reward3)))
    else:
        if (mr == reward0):
            return nx0, ny0, mr
        elif (mr == reward1):
            return nx1, ny1, mr
        elif (mr == reward2):
            return nx2, ny2, mr
        elif (mr == reward3):
            return nx3, ny3, mr

def DIGUI(x,y,reward):
    try:
        return DIGUI(GetQ(x, y, 0))
    except:
        pass
number=5
knum=0
Num=0
EW.Points = points
EW.xo = xo
EW.yo = yo
while Num<number:
    knum=0
    print(Num)
    while knum < 10000:
        knum = knum + 1
        EW.X, EW.Y = EW.ReStart()
        DIGUI(EW.X, EW.Y, 0)
    Num = Num + 1
print("OK")
xf=700
yf=100
PPionts=[]
KKO=0
while xf>=0 and xf<800 and yf>=0 and yf<600 :
    distance = np.sqrt((xf - xo) ** 2 + (yf - yo) ** 2)
    if distance < 80 or KKO > 1000000:
        break
    AC = (EW.Q[xf + yf * 800][0], EW.Q[xf + yf * 800][1], EW.Q[xf + yf * 800][2], EW.Q[xf + yf * 800][3])
    xf, yf = EW.TestAction(xf, yf, AC)
    PPionts.append((xf, yf))
    KKO = KKO + 1
    # print(xf,yf)
    # print(AC)
font = pygame.font.SysFont("arial", 16)
Agent1 = "Rader"
Agent2 = "Object"
Agent3 = "Su27"
Agent4 = "GJ"
# #Q-Learning 算法
#
name="PPoint.data"
np.save("PPoint.data_0.26_0.16_"+str(number),PPionts)
#PPionts=np.load("PPoint.data30.npy")
def playgame(num):
    for i in range(num):
        pygame.draw.circle(screen, (255, 0, 0), (PPionts[i][0],PPionts[i][1]), 1)
frame=0
while True:
    screen.fill((255, 255, 255))
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == KEYDOWN:
        if event.key == K_a:
            if ShowName == True:
                ShowName = False
            else:
                ShowName = True
    if event.type == VIDEORESIZE:

        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | RESIZABLE, 32)
        pygame.display.set_caption("EW仿真器" + str(event.size))

    screen_width, screen_height = SCREEN_SIZE

    pygame.draw.circle(screen, (200, 200, 90), (xo, yo), 8)
    pygame.draw.circle(screen, (0, 0, 236), (xr, yr), 8)

    pygame.draw.circle(screen, (100, 59, 200), (xj, yj), 8)

    # if(frame>=len(PPionts)):
    #     frame=0
    # else:
    #     playgame(frame)
    #     frame+=1
    for IO in PPionts:
        pygame.draw.circle(screen, (255, 0, 0), IO, 1)
    if ShowName==True :
        #font = pygame.font.SysFont("arial", 16)
        screen.blit(font.render(Agent1, True, (0, 0, 0)), (xo, yo))
        screen.blit(font.render(Agent2, True, (0, 0, 0)), (xr, yr))

        screen.blit(font.render(Agent4, True, (0, 0, 0)), (xj, yj))
    for p in points:
        # 在点击的位置画一个小圆，p是坐标，3是半径
        num = random.random()
        if (num < 0.03):
            pygame.draw.circle(screen, (255, 105, 105), p, 1)
        # pygame.draw.lines(screen, (155, 155, 0), False, points, 2)
    # MAX=max(Q)
    # MIN=min(Q)
    # EE=MAX-MIN
    # for y in range(600):
    #     for x in range(800):
    #         num = random.random()
    #         MB= max(EW.Q[x + y * 800][0], EW.Q[x + y * 800][1], EW.Q[x + y * 800][2], EW.Q[x + y * 800][3])
    #         if (MB!=0):
    #             pygame.draw.circle(screen, (205, 205,205 ), (x, y), 1)

    #贪婪算法

    pygame.display.update()
