"""
----------------------------Procedure for implementing the triangle problem----------------------------------------------

1.   Generate n random points 

2.   Define a fuction which returns eucledian distance between two points 

3.   Finding the smallest triangle :
    
    --> Using brute force:
        
        Time Complexity O(n^3)
        
        Create three nested "for" loops which parses through each points, simultaneously calculating and updating the shorotest perimeter.
        
        For higher order values of "n", this algorithm performs very poorly.
        
    


"""

import math
import random

def distance(p1,p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_triangle():
    no_of_points=int(input("Enter the number of points --->   "))
    points=[]
    min_perim=float('inf')
    flags=[]
    for count in range(no_of_points):
        points.append((random.uniform(-100,100),random.uniform(-100,100)))
   
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            for k in range(j+1,len(points)):
                perimeter=distance(points[i],points[j])+distance(points[j],points[k])+distance(points[i],points[k])
                if perimeter < min_perim:
                    min_perim=perimeter
                    flags.clear()
                    flags.append(points[i])
                    flags.append(points[j])
                    flags.append(points[k])
    print(flags)

find_triangle()