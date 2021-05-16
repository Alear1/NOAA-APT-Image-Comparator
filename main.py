# This is a sample Python script.

import numpy as np
import cv2 as cv
import sys
import math

min = 10
vertical_transform = 0

def lineup(im1, im2):
    if (len(im1)-len(im2)) > 200:
        scroll(im2, im1)
    elif (len(im1) - len(im2)) < -200:
        scroll(im1, im2)
    else:
        scroll(im1, im2[int(len(im2) / 4) : int(len(im2)*3/4)])

def make_single_channel(img):
    single_channel_img = np.empty([len(img), len(img[0])])
    for row in range(0, len(img)):
        for col in range(0, len(img[0])):
            single_channel_img[row][col] = 1

    return single_channel_img

def make_multi_channel(img):
    multi_channel_img = np.empty([len(img), len(img[0]), 3])
    for row in range(len(img)):
        for col in range(0, len(img)):
            pixVal = int(img[row][col])
            multi_channel_img[row][col][0] = pixVal
            multi_channel_img[row][col][1] = pixVal
            multi_channel_img[row][col][2] = pixVal

    return multi_channel_img

def scroll(stationary, scrolling):
    h = 100 # height of little box
    H = len(stationary)
    l = 100 # width of the little box
    c_off = 150 # Distance right from edge of image. Constant
    col_start = c_off # column anchor point of the little box
    row_start = 150 # row anchor point of the little box

    maskDiff = [] # size of r_off
    currDiff = 0

    for r_off in range(0, H-h):
        for row in range(0, h):
            for col in range(0, l):
                currDiff += abs(int(stationary[r_off + row][c_off + col][0]) -
                                int(scrolling[row_start + row][col_start + col][0]))
        maskDiff.append(currDiff)
        currDiff = 0

    minimum = np.argmin(maskDiff)
    print(minimum)


img1 = cv.imread(cv.samples.findFile("NOAA_APT_19_borderless.png"))
img2 = cv.imread(cv.samples.findFile("NOAA-19-20200917-0747-NOMAP.png"))


if img1 is None:
    sys.exit("Error: image 1 is not valid")
if img2 is None:
    sys.exit("Error: image 2 is not valid")

# cv.imshow("Display Window", img1)

'''
step 1:
    Cut larger image down to size
'''

lineup(img1, img2)
#
k = cv.waitKey(0)
if k == ord("s"):
     cv.imwrite("NOAA_APT_19_borderless.png")




