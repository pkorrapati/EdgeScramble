import numpy as np

''' Scramble takes a grayscale image 
img: grayscale image
pix: number of pixels to scramble the edges by
thr: threshold for edges
'''
def scramble(img, pix=5, thr=200):
    # Max size of the image
    rowMax, colMax = img.shape    

    rows, cols = np.where(img >= thr)

    rows =  limit(np.add(rows, np.round(np.random.rand(np.size(rows)) * pix - (0.5 * pix))), rowMax).astype(int)
    cols =  limit(np.add(cols, np.round(np.random.rand(np.size(cols)) * pix - (0.5 * pix))), colMax).astype(int)

    return rows, cols

def limit(val, maxVal, minVal=0):
    return np.minimum(maxVal, np.maximum(minVal, val))