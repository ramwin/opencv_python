#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Xiang Wang @ ramwin@qq.com 2016-04-20 11:43:20

import numpy as np
import cv2

# 创建图片
img = np.zeros((512,512,3), np.uint8)

# 画直线Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)

# 画矩形
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# 画圆
cv2.circle(img,(447,63), 63, (0,0,255), -1)

# 画椭圆
# cv2.ellipse(图片, 中心, 轴长, 顺时针偏转角, 起始角度, 终止角度, 颜色, 线的厚度)
# 注意这里椭圆的角度是和一般的圆的定义不一样, 参考:
# http://mathworld.wolfram.com/Ellipse.html
cv2.ellipse(img,(256,256),(100,50),30,0,-250,(0,255,0),10)

# 画多边形
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))     # TODO 不知道这个做什么
# True代表按顺序画线, 如果是False的画就会任意两条都画。
# pst 中间可以一次性传递多个多边形, 优于分别传递
img = cv2.polylines(img,[pts],True,(0,0,255))

# 画文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('按任意键继续', img)
k = cv2.waitKey(0) & 0xFF
