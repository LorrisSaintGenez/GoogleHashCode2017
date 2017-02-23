#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random

nbVideos = 0
nbEndPoints = 0
nbRequests = 0
nbCaches = 0
sizeEachCache = 0

bigMatrix = [] #requete video, endpoint, nbrequete
matrix2 = [] #latence / nbcache
video_list_sizes = [] #taille des video
master = [] #cache / latence

def parseFile(file):
    global nbCaches
    global matrix2
    global nbVideos
    global sizeEachCache
    process = 0
    val_parse = 0
    detail = []
    global master
    global video_list_sizes
    endpos = 0
    flag = 0
    requestMatrix = []
    global bigMatrix
    with open(file, 'r') as f:
        for (row, line) in enumerate(f):
            if row < 1:
                nbVideos = line.split()[0]
                nbEndPoints = line.split()[1]
                nbRequests = line.split()[2]
                nbCaches = line.split()[3]
                sizeEachCache = line.split()[4]
            if row == 1:
                for video in line.split(' '):
                    video_list_sizes.append(video)
            if row > 1:
                try:
                    line.split(' ')[2]
                    requestMatrix.append(line.split()[0])
                    requestMatrix.append(line.split()[1])
                    requestMatrix.append(line.split()[2])
                    bigMatrix.append(requestMatrix)
                    requestMatrix = []
                except:

                    if process == 0:
                        matrix2.append(line.split(' ')[0] + ' '
                                + line.split(' ')[1][:-1])
                        val_parse = int(line.split(' ')[1])
                        process = 1
                        endpos += 1
                        if val_parse == 0:
                            flag = 1
                    else:
                        detail.append(line.split(' ')[0] + ' '
                                + line.split(' ')[1])
                        val_parse -= 1
                        if val_parse == 0:
                            process = 0
                            master.append(detail)
                            detail = []
        return video_list_sizes, matrix2


# print(parseFile('trending_today.in'))

def Desepoire():
    print ('trop vieux pour cette merde !')


def FromContainerToString(val):
    tmp = ''
    for x in val:
        val += x + ''
    return tmp


def WriteToFile(header, val):
    f = open('test.txt', 'w+')
    i = 0
    f.write(str(header) + '\n')
    for x in val:
        f.write(str(i) + ' ')
        i += 1
        for y in x:
            f.write(str(y) + ' ')
        f.write('\n')
    f.close()


# ==============================================================================#

videos, plop = parseFile('me_at_the_zoo.in')
videos[len(videos) - 1] = (videos[len(videos) - 1])[:-1]
'''
bigMatrix = [] #requete video, endpoint, nbrequete
matrix = [] #latence / nbcache
video_list_sizes = [] #taille des video
master = [] #cache / latence
'''

print(bigMatrix)
bigMatrix.sort(key=lambda x : x[2])
bigMatrix = reversed(bigMatrix)
print(bigMatrix)   
rest = []
for x in bigMatrix:
    rest.append(int(x[1]))
print(rest)

cachenb = 0
def algo():
    global cachenb
    currentCacheSize = 0
    tabLength = len(videos)
    matrix = []

    print(nbCaches)
    if nbCaches != 0:
        #print(int(nbVideos))
        tmp = []
        for nbVideo in rest:
            #print(nbVideo)
            if (currentCacheSize + int(video_list_sizes[nbVideo]) < int(sizeEachCache)):
                #print(str(currentCacheSize + int(video_list_sizes[nbVideo])) + "!////!" + str(int(sizeEachCache)))
                currentCacheSize += int(video_list_sizes[nbVideo])
                if (nbVideo not in tmp):
                    tmp.append(nbVideo)
                #print("add video")
            else:
                #print(tmp)
                tmp = []
                currentCacheSize = 0
                matrix.append(tmp)
                #print("add")
                cachenb += 1
                if (cachenb >= int(nbCaches)):
                    return matrix
        #print(matrix)
        return matrix



var = algo()
print(cachenb)
#print(var)
WriteToFile(cachenb, var)
