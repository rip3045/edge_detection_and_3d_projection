
import cv2
import numpy as np
from matplotlib import pyplot as plt
import localization
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

###Load the images in and display
img1 = cv2.imread('left_image.png', 1)
img2 = cv2.imread('right_image.png', 1)

cv2.imshow('left_frame', img1)
cv2.imshow('right_frame', img2)
cv2.waitKey(0)
input("Press enter to continue")
cv2.destroyAllWindows()

###Grayscale the images before processing
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('left_frame', img1)
cv2.imshow('right_frame', img2)
cv2.waitKey(0)
input("Press enter to continue")
cv2.destroyAllWindows()

###Running the canny algorithm to get edges, show
img1 = cv2.Canny(img1, 330, 500, L2gradient=True)
img2 = cv2.Canny(img2, 330, 500, L2gradient=True)

plt.subplot(121),plt.imshow(img1,cmap = 'gray')
plt.title('Left_Frame'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img2,cmap = 'gray')
plt.title('Right_Frame'), plt.xticks([]), plt.yticks([])

plt.show()
input("Press enter to continue")
cv2.destroyAllWindows()

###these loops get the x and y values of the detected pixels in the edges
pixels1 = []
for i in range(img1.shape[1]):
    for j in range(img1.shape[0]):
        if img1[j][i] == 255:
            pixels1.append([j, i])
print(len(pixels1))

pixels2 = []
for i in range(img2.shape[1]):
    for j in range(img2.shape[0]):
        if img2[j][i] == 255:
            pixels2.append([j, i])
print(len(pixels2))

###allocate the arrays
x_array = []
y_array = []
z_array = []

###here we are running the localization functions from the library

fov = 70
unview, in_view = localization.fov_fac(70)

for i in range(0, len(pixels2)):
    x1_ang = localization.angle_value(pixels1[i][0], 300, unview, in_view)
    x2_ang = localization.angle_value(pixels2[i][0], 300, unview, in_view)

    y1_ang = localization.angle_value(pixels1[i][1], 300, unview, in_view)
    y2_ang = localization.angle_value(pixels1[i][1], 300, unview, in_view)

    x, y, z = localization.find_distance(x1_ang, x2_ang, y1_ang, y2_ang, 4)
    x_array.append(x)
    y_array.append(y)
    z_array.append(z)
    i = 0


z_array2 = []
x_array2 = []
y_array2 = []
for i in range(0, len(z_array)):
    if z_array[i] <100 and z_array[i] >0:
        z_array2.append(z_array[i])
        x_array2.append(x_array[i])
        y_array2.append(y_array[i])
print(len(z_array2))
print(len(x_array2))
print(len(y_array2))
z_tuple = tuple(z_array2)
x_tuple = tuple(x_array2)
y_tuple = tuple(y_array2)
input("Press enter again")
#print(z_tuple)
#print(x_tuple)
#print(y_tuple)

input("press enter to plot")

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(x_tuple, y_tuple, z_tuple)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show(fig)
input("Press enter to finish program")

