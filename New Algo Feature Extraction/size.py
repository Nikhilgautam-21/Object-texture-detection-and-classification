# -*- coding: utf-8 -*-
"""
Created on Tue May 15 15:04:30 2018

@author: PanDa
"""

import cv2
import numpy as np

image = cv2.imread("C:\Users\PanDa\Desktop\Sir\image1.jpg")
width= np.size(image,0)
height= np.size(image,1)



width= int(width)
height= int(height)
print(width,height)

for i in range(1,20):
    print i