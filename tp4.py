import matplotlib.pyplot as plt
import random

def randomlist(length):
    list=[]
    for i in range(0,length):
        list.append(random.uniform(1,10))
    return list

def randomintlist(length):
    list=[]
    for i in range(0,length):
        list.append(random.randint(1,10))
    return list

if __name__=='__main__':

    plt.figure('TP4')

    plt.subplot(221)
    plt.title('data')
    list1 = randomlist(10)
    list2 = randomlist(10)
    list3 = randomlist(10)
    plt.xlabel('XLABEL')
    plt.ylabel('YLABEL')
    l1, = plt.plot(list1,label='line 1',color='red',linewidth=1)
    l2, = plt.plot(list2,label='line 2',color='blue',linewidth=2)
    l3, = plt.plot(list3,label='line 3',color='yellow',linewidth=3)
    plt.legend(loc='upper right')
    plt.annotate('value',xy=(5,list1[5]),xytext=(6,list1[5]+2),arrowprops=dict(facecolor='black', shrink=0.05))

    plt.subplot(212)
    list4 = randomintlist(50)
    plt.hist(list4)
    plt.title('histograme')
    plt.xlabel('Nomber')
    plt.ylabel('Count')

    plt.subplot(222)
    list5 = randomlist(4)
    plt.pie(list5)
    plt.title('Pie')
    plt.show()

    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D
    figure = plt.figure()
    ax = Axes3D(figure)
    X = np.arange(-10, 10, 0.25)
    Y = np.arange(-10, 10, 0.25)
    X, Y = np.meshgrid(X, Y)
    Z = 1 - X - Y
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    plt.show()
