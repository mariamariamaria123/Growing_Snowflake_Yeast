
#coordinates = [(0,0)]
#distances = []
#radius = 10
#def setup():
#    #size(1200,1200)
#    #background(255)
#    xcoord = random.randint(0,1200) #25
#    ycoord = random.randint(600,1200) #35
#    coordinates.append((xcoord,ycoord))
#    #fill(234,58,8)
#    #ellipse(xcoord,ycoord,radius,radius)
#    numcells = 1
#    #for x in range(0,200):
#    while numcells < 100:
#        xcoord = random.randint(0,1200) #25
#        ycoord = random.randint(700,1200) #35
#        # print(ycoord)
#        # for tup in coordinates:
#        #     xdist = (tup[0] - xcoord)**2
#        #     print('this is xdist ' +str(xdist))
#        #     ydist = (tup[1] - ycoord)**2
        #     print('this is ydist ' +str(ydist))
        #     centerDistance = math.sqrt(xdist + ydist)
        #     print('this is the centerdistance ' +str(centerDistance))
#        #     numcells +=1
#        #     distances.append(centerDistance)
#        # distanceLen = len(distances)
#        # for distance in distances:
#        coord = (xcoord,ycoord) #(25,35)
#        for x in coordinates:
#            xdist = (x[0] - xcoord)*(x[0] - xcoord)
#            ydist = (x[1] - ycoord)*(x[1] - ycoord)
#            distance = math.sqrt(xdist+ydist)
#            print(distance)
#            distances.append(distance)
#        distlen = len(distances)
#        count = 0# pronblem
#        for distance in distances:
#            if distance > radius:
#                count += 1
#                print('distance greater than radius')
#            else:
#                j = 0
#        if count == distlen:
#            print('equals')
#            #ellipseMode = (CENTER)
#            #fill(123,65,3)
#            #ellipse(xcoord,ycoord,radius,radius)
#            coordinates.append(coord)
#            numcells +=1
#            print(numcells)
#        else:
#            j = 0
#    # else:
#    #     fill(234,5,8)
#    #     ellipse(xcoord,ycoord,radius,radius)
#    #     numcells +=1
#    #     print(numcells)
#    #     coordinates.append(coord)
#setup()

import math
import random
def setup():
    size(1200,1200)
    background(255)
    radius = 15
    centerCoord = (random.randint(0,1200),random.randint(600,1200))
    fill(30,137,136)
    ellipseMode = (CENTER)
    ellipse(centerCoord[0],centerCoord[1],radius,radius)
    Coordinates = [centerCoord]
    numCells = 1
    Overlap = False
    numCells = 1
    while numCells < 1000:
        print('this is the num cells at the beginning of the loop ' +str(numCells))
        xcoord = random.randint(0,1200)
        ycoord = random.randint(600,1200)
        Distances = []
        for coordinate in Coordinates:
            xd = (coordinate[0]-xcoord)*(coordinate[0]-xcoord)
            yd = (coordinate[1]-ycoord)*(coordinate[1]-ycoord)
            distance = math.sqrt(xd + yd)
            if distance > (radius*4):
                print('distance that SHOULD be greater than radius*4 '+str(distance))
                Distances.append(distance)
                Overlap == False
            else:
                print('distance that didnt work '+str(distance))
                Overlap == True
                break
            break
        count = 0
        #for distance in Distances:
           # if distance > radius*4:
          #      print('h')
              #  return False # stops overlap, but also ends the for loop
        #print(len(validDistances))
        #print(len(Coordinates))
        #if len(validDistances) == (len(Coordinates)-1):
        if Overlap == False:
            Coordinates.append((xcoord,ycoord))
            numCells += 1
            fill(12,133,145,67)
            ellipse(xcoord,ycoord,radius,radius)
            print('number of cells at end '+str(numCells))
            print(Coordinates)

                
