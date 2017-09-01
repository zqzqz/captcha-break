from sklearn.svm import SVC
import numpy as np
import time
from predict import *


def load_data():
    dataset = np.loadtxt(u'D:/test/captcha-break/training/train_data.txt', delimiter=',')
    return dataset


"""
    使用SVC训练数据
    return the trained model
"""
def cross_validation():
    dataset = load_data()
    row, col = dataset.shape
    X = dataset[:, :col - 1]
    Y = dataset[:, -1]
    clf = SVC(kernel='rbf', C=1000)
    clf.fit(X, Y)
    #scores = cs.cross_val_score(clf, X, Y, cv=5)
    #print("Accuracy: %0.2f (+- %0.2f)" % (scores.mean(), scores.std()))
    return clf

def train():
    t0 = time.time()
    clf = cross_validation()
    print("fit time:", round(time.time() - t0, 3), "s")
    return clf



if __name__ == "__main__":
    clf = train()
    print(clf)
    predict(clf)