import _thread
import numpy as np
import random
import matplotlib.pyplot as plt
import time

class Ant(object):

    def __init__(self,x,y,direction,CR,CV,CB,SR,SV,SB,Pg,Pd,Pt,Ps,type):
        # position x,y
        self.x = x
        self.y = y
        self.list_path_x = []
        self.list_path_y = []
        # direction
        #   8 1 5
        #   4 0 2
        #   7 3 6
        self.direction = direction
        # la couleur deposee (CR,CV,CB)
        self.CR = CR
        self.CV = CV
        self.CB = CB
        # la couleur suivie (SR,SV,SB)
        self.SR = SR
        self.SV = SV
        self.SB = SB
        # les probas (Pg,Pd,Pt)
        self.Pg = Pg
        self.Pd = Pd
        self.Pt = Pt
        # la probas de suivre la couleur Ps
        self.Ps = Ps
        # le type de mouvement oblique(Do):1  droit(Dd):2
        self.type = type

class Point(object):
    def __init__(self,x,y,CR,CV,CB):
        # position x,y
        self.x = x
        self.y = y
        # couleurs
        self.CR = CR
        self.CV = CV
        self.CB = CB
    def ReplaceColor(self,New_CR,New_CV,New_CB):
        self.CR = New_CR
        self.CV = New_CV
        self.CB = New_CB


def Cal_luminance(R,G,B):
    return 0.2426*R + 0.7152*G + 0.0722*B

def Cal_diff_luminance(ant,point):
    return abs(Cal_luminance(ant.SR, ant.SV, ant.SB) - Cal_luminance(point.CR, point.CV, point.CB))

def Choose_dir_to_move(ant,threshold,neighbor):
    if(ant.type == 1):
        pass
    elif(ant.type == 2):
        up = Cal_diff_luminance(ant, neighbor[0][1])
        dir = 1
        tmpDiff = up
        newPoint = neighbor[0][1]

        down = Cal_diff_luminance(ant, neighbor[2][1])
        if (tmpDiff < down):
            dir = 3
            tmpDiff = down
            newPoint = neighbor[2][1]

        left = Cal_diff_luminance(ant, neighbor[1][0])
        if (tmpDiff < left):
            dir = 4
            tmpDiff = left
            newPoint = neighbor[1][0]

        right = Cal_diff_luminance(ant, neighbor[1][2])
        if (tmpDiff < right):
            dir = 2
            tmpDiff = right
            newPoint = neighbor[1][2]

        if ((tmpDiff < threshold) & (random.random() < ant.Ps)):
            MoveToPoint(ant,newPoint,dir)
        else:
            dir = ant.direction
            rd = random.random()
            if (rd < ant.Pg): #turn left
                dir = dir - 1
                if(dir < 1):
                    dir = dir + 4
            elif (rd > (ant.Pg+ant.Pt)): #turn right
                dir = dir + 1
                if(dir > 4):
                    dir = dir - 4
            else:
                dir = ant.direction #go straight

            if (dir==1):
                newPoint = neighbor[0][1]
            elif(dir==2):
                newPoint = neighbor[1][2]
            elif(dir==3):
                newPoint = neighbor[2][1]
            elif(dir==4):
                newPoint = neighbor[1][0]
            MoveToPoint(ant,newPoint,dir)
        ant.list_path_x.append(newPoint.x)
        ant.list_path_y.append(newPoint.y)

    return newPoint


def MoveToPoint(ant, point, dir):
    ant.x = point.x
    ant.y = point.y
    point.ReplaceColor(ant.CR, ant.CV, ant.CB)
    ant.direction = dir

def Select_neighbor(ant,map):
    lists = [[] for i in range(3)]
    for i in range(3):
        for j in range(3):
            x = ant.x - 1 + j
            y = ant.y + 1 - i
            if(x >= 800):
                x = x - 800
            if(y >= 800):
                y = y - 800
            if(x < 0):
                x = x + 800
            if(y < 0):
                y = y + 800
            lists[i].append(map[y][x])
    return lists

def Run(ant,map,iteration,threshold):
    for i in range(iteration):
        neighbor = Select_neighbor(ant,map)
        newPoint = Choose_dir_to_move(ant,threshold,neighbor)

def Format(list_x,list_y):
    lists_x = []
    lists_y = []
    stop = 0
    for i in range(len(list_x)-1):
        if(abs(list_x[i]-list_x[i+1]) > 1 or abs(list_y[i]-list_y[i+1]) > 1):
            lists_x.append(list_x[stop:i+1])
            lists_y.append(list_y[stop:i+1])
            stop = i + 1
    lists_x.append(list_x[stop:len(list_x)])
    lists_y.append(list_y[stop:len(list_y)])
    list = []
    list.append(lists_x)
    list.append(lists_y)
    return lists_x,lists_y


if __name__ == '__main__':
    # taille de la toile
    width = 800
    height = 800
    # nb de fourmis
    nb_ant = 2
    # nb d'iteration
    iteration = 100000
    threshold = 40

    ant1 = Ant(32,21,1,34,67,60,33,65,32,0.4,0.3,0.3,0.8,2)
    ant2 = Ant(47,44,1,34,43,80,33,51,77,0.3,0.4,0.3,0.9,2)

    map = [[] for i in range(width)]
    for i in range(height):
        for j in range(width):
            init_point = Point(j,i,0,0,0)
            map[i].append(init_point)

    _thread.start_new_thread(Run, (ant1,map,iteration,threshold, ))
    _thread.start_new_thread(Run, (ant2,map,iteration,threshold, ))
    time.sleep(5)

    ant1_list_x, ant1_list_y = Format(ant1.list_path_x, ant1.list_path_y)
    ant2_list_x, ant2_list_y = Format(ant2.list_path_x, ant2.list_path_y)

    plt.figure()
    for i in range(len(ant1_list_x)):
        plt.plot(ant1_list_x[i],ant1_list_y[i],'b-')
    for i in range(len(ant2_list_x)):
        plt.plot(ant2_list_x[i],ant2_list_y[i],'r-')
    plt.show()
