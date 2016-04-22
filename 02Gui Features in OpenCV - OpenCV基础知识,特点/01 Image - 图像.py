#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Xiang Wang @ ramwin@qq.com 2016-04-20 11:22:20

import numpy as np
import cv2
import time
from matplotlib import pyplot as plt
# Load an color image in grayscale
img = cv2.imread('../img/messi5.jpg',0)
cv2.imshow('使用 imshow 来展示图片, 按 Esc 继续, 按s保存',img)
k = cv2.waitKey(0) & 0xFF   # 获取按键的数值
if k == 27:
    print('退出')
elif k ==  ord('s'):
    print('保存图片')
    cv2.imwrite('../img/messigray.png', img)
cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # 去除 x, y 轴的坐标
plt.show()
