import cv2
import numpy as np
from sklearn import tree
from testquest import TestQuest

tq = TestQuest()
imgs = tq.cutAlternative(tq.cutQuest(tq.cutTest(np.array(cv2.imread(tq.prova1_path, cv2.IMREAD_COLOR)))))

treino = [
    [imgs[0, 0], 0],
    [imgs[0, 1], 1],
    [imgs[0, 2], 0],
    [imgs[0, 3], 0],
    [imgs[0, 4], 0],

    [imgs[1, 0], 0],
    [imgs[1, 1], 0],
    [imgs[1, 2], 2],
    [imgs[1, 3], 0],
    [imgs[1, 4], 0],

    [imgs[2, 0], 0],
    [imgs[2, 1], 2],
    [imgs[2, 2], 0],
    [imgs[2, 3], 0],
    [imgs[2, 4], 0],

    [imgs[3, 0], 2],
    [imgs[3, 1], 0],
    [imgs[3, 2], 0],
    [imgs[3, 3], 0],
    [imgs[3, 4], 0],

    [imgs[4, 0], 0],
    [imgs[4, 1], 2],
    [imgs[4, 2], 0],
    [imgs[4, 3], 0],
    [imgs[4, 4], 0],

    [imgs[5, 0], 1],
    [imgs[5, 1], 0],
    [imgs[5, 2], 0],
    [imgs[5, 3], 0],
    [imgs[5, 4], 1],

    [imgs[6, 0], 0],
    [imgs[6, 1], 2],
    [imgs[6, 2], 1],
    [imgs[6, 3], 0],
    [imgs[6, 4], 0],

    [imgs[7, 0], 1],
    [imgs[7, 1], 2],
    [imgs[7, 2], 0],
    [imgs[7, 3], 0],
    [imgs[7, 4], 0],

    [imgs[8, 0], 0],
    [imgs[8, 1], 2],
    [imgs[8, 2], 0],
    [imgs[8, 3], 0],
    [imgs[8, 4], 0],

    [imgs[9, 0], 2],
    [imgs[9, 1], 2],
    [imgs[9, 2], 2],
    [imgs[9, 3], 2],
    [imgs[9, 4], 2],
]

for img in imgs:
    for alt in img:
        cv2.imshow('title', alt)
        cv2.waitKey(0)