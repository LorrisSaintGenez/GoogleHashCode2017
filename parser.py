import sys

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
		if endpos < nbEndPoints and flag == 0:	
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
		else:
			requestMatrix.append(line.split()[0])
			requestMatrix.append(line.split()[1])
			requestMatrix.append(line.split()[2])
			bigMatrix.append(requestMatrix)
			requestMatrix = []

			
            '''else :
                for column, char in enumerate(line):
                    if column < int(intel_list[1]) :
                        matrix[row - 1][column] = char

    return matrix, intel_list[2], intel_list[3]
'''	
    return master

print(parseFile('trending_today.in'))



def Desepoire():
    print('trop vieux pour cette merde !')

def FromContainerToString(val):
    tmp = ""
    for x in val:
        val += x + ""
    return tmp

def WriteToFile(val):
    f = open('test.txt', 'a+')
    f.write(val)
    f.close()

#==============================================================================#
