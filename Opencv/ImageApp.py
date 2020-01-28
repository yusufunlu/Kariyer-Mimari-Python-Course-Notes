import cv2
image = cv2.imread("watch.jpg")

def rotate(self,img):
    height, width = img.shape[0:2]
    rotationMatrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, .5)
    rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))
