import numpy as np
import cv2

template = cv2.resize(cv2.imread('template.jpeg'), (0, 0), fx=1.5, fy=1.5)
h, w, _ = template.shape


def img1():
    img1 = cv2.resize(cv2.imread("base1.jpeg"), (0, 0), fx=1.5, fy=1.5)
    method = cv2.TM_SQDIFF
    result = cv2.matchTemplate(img1, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if True:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img1, location, bottom_right, 255, 5)
    return img1

def img4():
    img2 = cv2.resize(cv2.imread("base4.png"), (0, 0), fx=2, fy=2)
    method = cv2.TM_SQDIFF
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if True:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    return img2


cv2.imshow("Template", template)
cv2.moveWindow("Template", 100, 100)
cv2.waitKey(0)
cv2.imshow('Match', img1())
cv2.moveWindow("Match", 600, 0)
cv2.waitKey(0)
cv2.imshow('Match', img4())
cv2.moveWindow("Match", 600, 300)
cv2.waitKey(0)
cv2.destroyAllWindows()
