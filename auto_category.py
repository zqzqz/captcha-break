from binary_transform import *
import sys
sys.path.append('C:/Program Files (x86)/Tesseract-ORC')
sys.path.append('D:\Python3\Lib\site-packages\pytesser')
from pytesser3 import *
from pytesseract import *
from PIL import Image
import os
import shutil

# ocr图像识别
def ocr(img):
    try:
        img = Image.open(img)
        rs = image_to_string(img)
    except:
        return 'none'
    if rs == "":
        return 'none'
    return rs


# 使用ocr进行训练的预分类
def category(originfile, dirs, filename):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    print(dirs)
    shutil.copyfile(originfile, dirs + filename)


if __name__ == '__main__':
    dirs = u'D:/test/captcha-break/'
    os.chdir(mydir + "raw-img")

    # 将ocr识别的文件按照数组编号存放在相应的文件夹中
    for fr in os.listdir(dirs+'raw-img'):
        num = 0
        f = dirs + 'raw-img/'+ fr
        if f.rfind(u'.DS_Store') == -1:
            rs = ocr(f).split(' ')

            #切割验证码
            imgs = cut_img(fr)
            #存储切割后的验证码
            save_cut(imgs, fr.split('.')[0])

            for one_chr in rs:
                if len(one_chr)!=1:
                    continue
                if '|' not in one_chr and '*' not in one_chr and '?' not in one_chr and '<' not in one_chr and '>' not in rs:
                    try:
                        tmp_name = '%s_%s.jpeg'%(fr.split('.')[0], str(num))
                        num += 1
                        #分类切割后的验证码
                        category(dirs+'filter/'+tmp_name, dirs+'/category/%s/' % one_chr, tmp_name)
                    except:
                        break

