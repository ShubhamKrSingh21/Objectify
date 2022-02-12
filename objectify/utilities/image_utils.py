import numpy as np
import cv2
def saveImg(filename, img, cvtColor=True):
    if cvtColor:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite(filename, img)
    return True