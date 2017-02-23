#!/usr/bin/env python3

import sys
import random

nbVideos = 0
nbEndPoints = 0
nbRequests = 0
nbCaches = 0
sizeEachCache = 0


def parseFile(file):
    matrix = []
    process = 0
    val_parse = 0
    detail = []
    master = []
    video_list_sizes = []
    endpos = 0
    flag = 0
    requestMatrix = []
    bigMatrix = []
    with open(file, 'r') as f:
        for row, line in enumerate(f):
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
				matrix.append(line.split(' ')[0] + ' ' + line.split(' ')[1])
				val_parse = int(line.split(' ')[1])
				process = 1
				endpos += 1
				if val_parse == 0:
					flag = 1
			else:	
				detail.append(line.split(' ')[0] + ' ' + line.split(' ')[1])
				val_parse -= 1
				if val_parse == 0:
					process = 0
					master.append(detail)
					detail = []
	return video_list_sizes

#print(parseFile('trending_today.in'))



def Desepoire():
    print('trop vieux pour cette merde !')

def FromContainerToString(val):
    tmp = ""
    for x in val:
        val += x + ""
    return tmp

def WriteToFile(header, val):
    f = open('test.txt', 'a+')
    f.write(str(header) + '\n')
    for x in val:
        for y in x:
            f.write(y + '\n')
        f.write('\n')
    f.close()

a = "500" + '\n'
for i in range(0, 500):
    a += str(i) +' '+ str(random.randint(0,500)) + '\n'
f = open('test.txt', 'w')
f.write(a)
f.close()

#==============================================================================#

videos = parseFile('trending_today.in')
videos[len(videos) - 1] = str(329)
#print("====" + videos[len(videos) - 1] + "====")

def algo():
    tabLength = len(videos)
    matrix = []
    if (nbCaches != 0):
        split = tabLength // nbCaches
        matrix = [[0 for x in range(split)] for y in range(nbCaches)]
        for i in range(nbCaches):
            for j in range(split):
                matrix[i][j] = videos[i * split + j]
    return matrix

#print(algo())
WriteToFile(nbCaches, algo())
