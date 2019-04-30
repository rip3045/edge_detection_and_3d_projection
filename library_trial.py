import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sunset.jpg', 0)
img = cv2.resize(img, (300, 250))
edges = cv2.Canny(img, 150, 200)
plt.imshow(edges,cmap = 'gray')
plt.show()
print(edges.shape)
#cv2.waitKey(0)

pixels = []
for i in range(edges.shape[1]):
    for j in range(edges.shape[0]):
        if edges[j][i] == 255:
            pixels.append([j, i])
print(pixels)
input("Press any key to continue")
cv2.destroyAllWindows()