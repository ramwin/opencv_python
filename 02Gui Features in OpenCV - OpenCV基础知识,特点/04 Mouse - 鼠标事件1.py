#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Xiang Wang @ ramwin@qq.com 2016-04-20 12:50:20

import numpy as np
import cv2

# 所有的事件基本都包含 'EVENT'
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('双击了')
        cv2.circle(img,(x,y),100,(255,0,0),-1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

