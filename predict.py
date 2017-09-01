from binary_transform import *
from factors_config import *
from sklearn.svm import SVC
import numpy as np

"""
    识别验证码
    function name: predict
    parameters: clf--the trained model; folder--the folder containing samples
    return: none
    stdout: the predictions
"""
def predict(clf, folder="D:/test/captcha-break/samples/"):
    sample_list = os.listdir(folder)
    for sample in sample_list:
        imgs = cut_img(folder+sample)
        result=''
        for img in imgs:
            binpix = [getBinaryPix(img,760)]
            #print(binpix)
            tmp_result = clf.predict(binpix)
            result += (chr(ord('a')+tmp_result) + ' ')
        print(sample+"\'s prediction: "+result)




