#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-04-01 14:25:08

import cv2
img = cv2.imread('./png.png')


def handle(dot):
    '''dot*x+y'''
    x = 1.3
    y = 0
    return list(map(lambda v: x*v+y if v*x + y<255 else 255,  dot))


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i, j] = handle(img[i,j])


cv2.imwrite("png2_1.3.png", img)
