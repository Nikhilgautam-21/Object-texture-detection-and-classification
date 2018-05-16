# -*- coding: utf-8 -*-
"""
Created on Wed May 02 11:39:13 2018

@author: PanDa
"""

# import the necessary packages
from localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import cv2
 



# initialize the local binary patterns descriptor along with
# the data and label lists
desc = LocalBinaryPatterns(24, 8)
data = []
labels = []
# loop over the training images
for imagePath in paths.list_images("E:\set_1\test"):
	# load the image, convert it to grayscale, and describe it
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	hist = desc.describe(gray)
 
	# extract the label from the image path, then update the
	# label and data lists
	labels.append(imagePath.split(".")[-2])
       # labels.append(os.path.split(os.path.dirname(imagePath))[-1])

	data.append(hist)
 
# train a Linear SVM on the data
model = LinearSVC(C=100.0, random_state=42)
model.fit(data, labels)
# loop over the testing images
for imagePath in paths.list_images("E:\set_1\test"):
	# load the image, convert it to grayscale, describe it,
	# and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = desc.describe(gray)
    prediction = model.predict(hist.reshape(1,-1))[0]
    


	# display the image and the prediction
    cv2.putText(image, prediction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
