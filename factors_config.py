from PIL import Image
import numpy as np
import os

"""
    特征提取，获取图像二值化数学值  
    ps: 如果采集样本时已经二值化，此处可以省略，直接转数组形式即可
"""
def getBinaryPix(im, max_bias=-1):
    img = np.array(im)
    #print(img)
    rows, cols = img.shape

    for i in range(rows):
        for j in range(cols):
            if (img[i, j] <= 128):
                img[i, j] = 0
            else:
                img[i, j] = 1


    binpix = np.ravel(img)
    pixs = binpix.tolist()
    # the max number of factors: 760 ; extend all lists
    # max_len = max(len(pixs), max_len)
    if max_bias>len(pixs):
        add_num = max_bias - len(pixs)
        pixs += [1 for i in range(add_num)]
    return pixs


def getfiles(dirs):
    fs = []
    for fr in os.listdir(dirs):
        f = dirs + fr
        if f.rfind(u'.DS_Store') == -1:
            fs.append(f)
    return fs


def writeFile(content):
    with open(u'D:/test/captcha-break/training/train_data.txt', 'a+') as f:
        f.write(content)
        f.write('\n')
        f.close()


if __name__ == '__main__':
    dirs = u'D:/test/captcha-break/category/%s/'
    #max_len = 0
    for i in range(26):
        for f in getfiles(dirs % (chr(ord('a')+i))):
            img = Image.open(f)
            pixs = getBinaryPix(img,760)
            #每组特征值之后加上匹配的字符结果
            pixs.append(i)
            pixs = [str(i) for i in pixs]
            content = ','.join(pixs)
            writeFile(content)