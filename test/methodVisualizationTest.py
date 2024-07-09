import numpy as np
import matplotlib.pyplot as plt

from math import pi

def limit(val, maxVal, minVal=0):
    return np.minimum(maxVal, np.maximum(minVal, val))

pix = 10
colMax = 30
rowMax = 30

rows = np.zeros(3500)
cols = np.zeros(3500)

# # METHOD 1
# rows =  limit(np.add(rows, np.round(np.random.uniform(-pix, pix, np.size(rows)))), rowMax, -rowMax).astype(int)
# cols =  limit(np.add(cols, np.round(np.random.uniform(-pix, pix, np.size(cols)))), colMax, -colMax).astype(int)

# METHOD 2
ang = np.random.uniform(0, 2 * pi, np.size(rows))
rad = np.random.uniform(0, pix, np.size(rows))

rows =  limit(np.add(rows, np.round(np.multiply(rad, np.sin(ang)))), rowMax, -rowMax).astype(int)
cols =  limit(np.add(cols, np.round(np.multiply(rad, np.cos(ang)))), colMax, -colMax).astype(int)

plt.scatter(cols, rows)
plt.axis('Equal')
plt.show()