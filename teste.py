import cv2
import copy


img = cv2.imread('Sprite/001-m.png')

img_no_blue = copy.copy(img)
img_no_blue[:,:,0] = 0

cv2.waitKey(0)
