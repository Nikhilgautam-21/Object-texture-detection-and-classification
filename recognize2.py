# import the necessary packages
from localbinarypatterns import LocalBinaryPatterns
from sklearn.svm import LinearSVC
from imutils import paths
import argparse
import cv2
import time
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True,
	help="path to the training images")
#ap.add_argument("-e", "--testing", required=True, 
	#help="path to the tesitng images")
args = vars(ap.parse_args())
 

# Capturing the input image from Camera
capture = cv2.VideoCapture(0)
while(True):
    ret, frame = capture.read()
    cv2.putText(frame,"Press Q", (300,450), cv2.FONT_HERSHEY_SIMPLEX, 1, 158)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)


    cv2.imshow('frame', rgb)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite('capture.jpg', frame)
        
        break

capture.release()
img= cv2.imread('capture.jpg',0)
time.sleep(3)
cv2.destroyAllWindows()


# initialize the local binary patterns descriptor along with the data and label lists
desc = LocalBinaryPatterns(24, 8)
data = []
labels = []
# loop over the training images
for imagePath in paths.list_images(args["training"]):
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



gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
hist = desc.describe(gray)
prediction = model.predict(hist.reshape(1,-1))[0]
 
	# display the image and the prediction
cv2.putText(frame, prediction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 0, 255), 3)
cv2.imshow("Image", frame)
cv2.waitKey(0)
