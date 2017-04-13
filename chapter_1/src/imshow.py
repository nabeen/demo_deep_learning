import os
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread(os.path.dirname(os.path.abspath(__file__)) + '/img/aoi.png')
plt.imshow(img)

plt.show()
