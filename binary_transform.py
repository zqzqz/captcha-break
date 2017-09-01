from PIL import Image, ImageFilter, ImageEnhance
import os
from pytesser3 import *
import hashlib
import time

#global variable
mydir = "D:/test/captcha-break/"
threshold = 200
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

"""
    debug: 检查图片颜色
"""
def test_color(img):
    his = img.histogram()
    values = {}

    for i in range(256):
        values[i] = his[i]

    for j, k in sorted(values.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(j, k)
    return

"""
    图片切割
"""
def segment(img):
    im2 = img.convert('L')  # 灰度处理
    im2 = im2.point(table, '1')
    inletter = False
    foundletter = False
    start = 0
    end = 0
    letters = []
    for y in range(im2.size[0]):
        for x in range(im2.size[1]):
            pix = im2.getpixel((y, x))
            if pix != 1:
                inletter = True
        if foundletter == False and inletter == True:
            foundletter = True
            start = y

        if foundletter == True and inletter == False:
            foundletter = False
            end = y
            letters.append((start, end))
        inletter = False
    count = 0
    result = []
    for letter in letters:
        m = hashlib.md5()
        im3 = im2.crop((letter[0]-1, 0, letter[1]+1, img.size[1]))
        result.append(im3)
        count += 1
    return result

"""
    图片预处理
"""
def img_tranfer(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.MedianFilter()) #中值滤波
    enhancer = ImageEnhance.Contrast(img)  #图片增强
    img= enhancer.enhance(1)
    return img

"""
    预读取源验证码列表
"""
def load_imgs(folder):
    assert os.path.exists(folder)
    assert os.path.isdir(folder)
    img_list = os.listdir(folder)
    #img_list = [os.path.abspath(item) for item in imageList if os.path.isfile(os.path.join(folder, item))]
    return img_list


def cut_img(img_name):
    img = img_tranfer(img_name)
    imgs = segment(img)
    return imgs

"""
    保存切割后的图片
"""
def save_cut(cut_imgs, pre=''):
    num = 0
    for cut_img in cut_imgs:
        cut_img.save(mydir+"filter/%s_%s.jpeg"%(pre, str(num)))
        num += 1

if __name__ == '__main__':
    img_names = load_imgs(mydir+"raw-img")
    os.chdir(mydir+"raw-img")
    for img_name in img_names:
        pass
