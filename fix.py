import os
from pytesser3 import *

#change RGB imgs to black_and_white ones

#global variable
mydir = "D:/test/captcha-break/category/"
threshold = 190
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

route = chr(ord('a')-1)
for i in range(26):
    route = chr(ord(route) + 1)
    img_list = os.listdir(mydir+route+'/')
    for img_name in img_list:
        img = Image.open(mydir+route+'/'+img_name)
        im2 = img.convert('L')  # 灰度处理
        im2 = im2.point(table, '1')
        im2.save(mydir+route+'/'+img_name)

