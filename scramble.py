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

    rows =  limit(np.add(rows, np.round(np.random.uniform(-pix, pix, np.size(rows)))), rowMax).astype(int)
    cols =  limit(np.add(cols, np.round(np.random.uniform(-pix, pix, np.size(cols)))), colMax).astype(int)

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
    
    ang = np.random.uniform(0, 2 * pi, np.size(rows))
    rad = np.random.uniform(0, pix, np.size(rows))

    rows =  limit(np.add(rows, np.round(np.multiply(rad, np.sin(ang)))), rowMax).astype(int)
    cols =  limit(np.add(cols, np.round(np.multiply(rad, np.cos(ang)))), colMax).astype(int)

    return rows, cols

def limit(val, maxVal, minVal=0):
    return np.minimum(maxVal, np.maximum(minVal, val))