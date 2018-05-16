# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:23:12 2018

@author: PanDa
"""

import cv2
import numpy as np 

image = cv2.imread('C:\Users\PanDa\Desktop\Sir\image1.jpg', cv2.IMREAD_COLOR)

print(image[122,215][0])
        #print(pixel)