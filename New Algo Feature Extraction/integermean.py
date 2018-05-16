# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:42:41 2018

@author: PanDa
"""

import numpy


    
a= [[1,2,3],
    [4,5,6],
    [7,8,9]]

zero=0
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
print(A)     


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
     
       
       
       
       
       
       
       
        
        
    

 
