import numpy as np
from math import pi

''' Scramble takes a grayscale image and shifts x, y in Cartesian space by +/- pix
img: grayscale image
pix: number of pixels to scramble the edges by
thr: threshold for edges
'''
def scramble(img, pix=5, thr=200):
    # Max size of the image
    rowMax, colMax = img.shape    

    rows, cols = np.where(img >= thr)

    rows =  limit(np.add(rows, np.round((np.random.rand(np.size(rows)) * 2 * pix) - pix)), rowMax).astype(int)
    cols =  limit(np.add(cols, np.round((np.random.rand(np.size(cols)) * 2 * pix) - pix)), colMax).astype(int)

    return rows, cols

''' Scramble2 takes a grayscale image and shifts x, y in Eucledian space by radius = pix
img: grayscale image
pix: number of pixels to scramble the edges by
thr: threshold for edges
'''
def scramble2(img, pix=5, thr=200):
    # Max size of the image
    rowMax, colMax = img.shape    

    rows, cols = np.where(img >= thr)

    ang = np.random.rand(np.size(rows)) * 2 * pi

    rows =  limit(np.add(rows, np.round(np.dot(pix, np.sin(ang)))), rowMax).astype(int)
    cols =  limit(np.add(cols, np.round(np.dot(pix, np.cos(ang)))), colMax).astype(int)

    return rows, cols

def limit(val, maxVal, minVal=0):
    return np.minimum(maxVal, np.maximum(minVal, val))