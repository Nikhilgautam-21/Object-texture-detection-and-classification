# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:42:41 2018

@author: PanDa
"""

import numpy as np
import cv2

def findcenter(n1,n2,n3,n4,n5,n6,n7,n8,n9):
    temp =[[n1,n2,n3],
           [n4,n5,n6],
           [n7,n8,n9]]
    
    temp2 = [[0 for x in range(3)] for y in range(3)]
    zero=0
    ones=0
    c= []
    result =[]
    for i in range(3):
        for j in range(3):
            temp2[i][j]= '{0:08b}'.format(temp[i][j])
            c.append(temp2[i][j])
     
    c.pop(4)
    
    for j in range(0,8):
        zero=0
        ones=0
        for i in range(0,8):
            if(c[i][j]=='0'):
                zero=zero+1
            
            else:
                ones=ones+1
        print(zero,ones)
        if(zero>ones):
            result.append('0')
        else:
            result.append('1')


    print(result)

    x=''.join(result)
    s=0


    for i in range(0,8):
        s=s+int(x[i])*(2**(7-i))
        
    print(s)
    
    return s


#Read an image 
image = cv2.imread("C:\Users\PanDa\Desktop\Sir\image1.jpg",cv2.IMREAD_COLOR)

#width= np.size(image,0)
#height= np.size(image,1)

width=4
height=4

#initialize i2 array
i2= [[0 for o in range(height+2)] for p in range(width+2)]
mask= [[0 for x in range(3)] for y in range(3)] 

for i in range(0,height):
   for j in range(0,width):
       print(image[i,j][0])

#print i2 array
for i in range(0,height):
   for j in range(0,width):
      i2[i+1][j+1]= image[i,j][0]
i2=np.array(i2)
print(i2)

#Find Center Value for every i2 value
for i in range(1,height+1):
    for j in range(1,width+1):
        image[i-1,j-1]= findcenter(i2[i-1][j-1],i2[i][j-1],i2[i+1][j-1],i2[i-1][j],i2[i+1][j],i2[i][j],i2[i-1][j+1],i2[i][j+1],i2[i+1][j+1])
        
        

for i in range(0,height):
   for j in range(0,width):
       print(image[i,j][0])



        
        
        
        




    


'''zero=0
ones=0
c= []
result =[]
b = [[0 for x in range(3)] for y in range(3)]

for i in range(3):
    for j in range(3):
        b[i][j]= '{0:08b}'.format(a[i][j])
        c.append(b[i][j])

c.pop(4)
print("BINARY ARRAY")        

print(c)


print("NO. Of ZEROS AND ONES")
for j in range(0,8):
    zero=0
    ones=0    
    for i in range(0,8):
        if(c[i][j]=='0'):
            zero=zero+1
            
        else:
            ones=ones+1
    print(zero,ones)
    if(zero>ones):
        result.append('0')
    else:
        result.append('1')


print(result)

x=''.join(result)
s=0


for i in range(0,7):
    s=s+int(x[i])*(2^(7-i))

print("NEW CENTER VALUE IN DECIMAL")    
print(s)

a[1][1]=s
A= numpy.array(a)  
print(A)     '''


'''for i in range(0,3):
    for j in range(0,3):
       # print(a[0][0],a[1][0],a[2][2])
        b=a[i][j]
        for k in range(0,9):
            for l in range(8,1):
                if (b/(2**l)==1):
                    c[k][l-7]=1
                    b=b%(2**l)
                else:
                    c[k][l-7]=0;
                print("HI")'''
                    

    
#[int(i,10) for i in "100 010 110 111".split()]
     
       
       
       
       
       
       
       
        
        
    

 
