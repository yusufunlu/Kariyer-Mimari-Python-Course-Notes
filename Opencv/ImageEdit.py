import cv2
import time
originalLocation = "./OriginaIimages/laptop.jpg"
destinationLocation = "./ProducedImages/"
originalImage = cv2.imread(originalLocation)

print("Fotoyu dondurmek ıcın 1 e basiniz aksi takdirde 0")
rotateResult = input()
print("Dosyaya yazdırmak icin 1 ekrana icin 0 a basiniz")
saveResult = input()

def rotate(img):
    height, width = img.shape[0:2]
    rotationMatrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, .5)
    rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))
    return rotatedImage

def imageSave(img):
    isWriteDone = cv2.imwrite(destinationLocation + 'result' + str(epochTime) + ".jpg", img)
    print(isWriteDone)
    if isWriteDone == True:
        print("Foto başarı ile kaydedilmiştir")
    else:
        print("Foto kaydedilemedi")

if int(rotateResult)==1:
    resultImage = rotate(originalImage)
else:
    resultImage = originalImage

epochTime = int(time.time())

if int(saveResult) == 1:
    imageSave(resultImage)
else:
    cv2.imshow('Result Image', resultImage)
    cv2.waitKey(0)

