import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
import seaborn as sns

# s1 = Series(np.random.randn(1000)) # 生成1000个点的符合正态分布的随机数
# plt.hist(s1) # 直方图，也可以通过plot(),修改里面kind参数实现
# s1.plot(kind='kde') # 密度图
# plt.show()
#
# # seaborn
# sns.distplot(s1,hist=True,kde=True,rug=True) # 前两个默认就是True,rug是在最下方显示出频率情况，默认为False
# # bins=20 表示等分为20份的效果，同样有label等等参数
# sns.kdeplot(s1,shade=True,color='r') # shade表示线下颜色为阴影,color表示颜色是红色
# sns.rugplot(s1) # 在下方画出频率情况
# plt.show()
#
# x = np.linspace(0,14,100)
# y1 = np.sin(x)
# y2 = np.sin(x+2)*1.25
# def sinplot():
#     plt.plot(x,y1)
#     plt.plot(x,y2)
#
# sinplot() # 以matplotlib显示，生成两个函数图像
# plt.show()
#
#
# # 先绘制一个图像
# def sinplot1():
#     x = np.linspace(0,14,100)
#     plt.figure(figsize=(8,6)) # 图像比较小时，通过这个函数更改大小
#     for i in range(4):
#         plt.plot(x, np.sin(x + i) * (i + 0.75), label='sin(x+%s)*(%s+0.75)' % (i, i))
#     plt.legend()
#     plt.show()
# sinplot1()



def EW探索距离与个数变化():
    xo = 150
    yo = 230
    Point1 = np.load("PPoint.data_0.26_0.16_1.npy")
    Point2=np.load("PPoint.data_0.26_0.16_1.npy")
    Point3 = np.load("PPoint.data_0.26_0.16_5.npy")
    Point4 = np.load("PPoint.data_0.26_0.16_10.npy")
    Point5 = np.load("PPoint.data_0.26_0.16_100.npy")
    Point6 = np.load("PPoint.data_0.26_0.16_300.npy")
    Point7 = np.load("PPoint.data_0.26_0.16_300.npy")
    # x =ar[:,0] 直接取xy
    # y=ar[:,1]
    darr=[]
    xarr=[]
    for i in range(len(Point1)):
        d = np.sqrt((Point1[i][0] - xo) ** 2 + (Point1[i][1] - yo) ** 2)
        darr.append(d)
        xarr.append(i)
    plt.plot(xarr, darr,label='10000 trainings')
    xarr.clear()
    darr.clear()
    # for i in range(len(Point2)):
    #     d = np.sqrt((Point2[i][0] - xo) ** 2 + (Point2[i][1] - yo) ** 2)
    #     darr.append(d)
    #     xarr.append(i)
    # plt.plot(xarr, darr,label='100000 trainings')
    # xarr.clear()
    # darr.clear()
    for i in range(len(Point3)):
        d = np.sqrt((Point3[i][0] - xo) ** 2 + (Point3[i][1] - yo) ** 2)
        darr.append(d)
        xarr.append(i)
    plt.plot(xarr, darr,label='50000 trainings')
    xarr.clear()
    darr.clear()
    for i in range(len(Point4)):
        d = np.sqrt((Point4[i][0] - xo) ** 2 + (Point4[i][1] - yo) ** 2)
        darr.append(d)
        xarr.append(i)
    plt.plot(xarr, darr,label='100000 trainings')
    xarr.clear()
    darr.clear()
    # for i in range(len(Point5)):
    #     d = np.sqrt((Point5[i][0] - xo) ** 2 + (Point5[i][1] - yo) ** 2)
    #     darr.append(d)
    #     xarr.append(i)
    # plt.plot(xarr, darr,label='1 million trainings')
    # xarr.clear()
    # darr.clear()
    # for i in range(len(Point6)):
    #     d = np.sqrt((Point6[i][0] - xo) ** 2 + (Point6[i][1] - yo) ** 2)
    #     darr.append(d)
    #     xarr.append(i)
    # plt.plot(xarr, darr,label='3 million trainings')
    # xarr.clear()
    # darr.clear()
    # for i in range(len(Point7)):
    #     d = np.sqrt((Point7[i][0] - xo) ** 2 + (Point7[i][1] - yo) ** 2)
    #     darr.append(d)
    #     xarr.append(i)
    # plt.plot(xarr, darr,label='5 million trainings')
    plt.legend()
    plt.title('Training effect of different times', fontsize=12, verticalalignment='bottom')
    plt.ylabel('Distance', fontsize=10, alpha=0.7)
    plt.xlabel('Step Number', fontsize=10, alpha=0.7)
    plt.show()
EW探索距离与个数变化()
