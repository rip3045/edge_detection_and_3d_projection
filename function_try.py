import localization
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


unview, in_view = localization.fov_fac(90)

x1_ang = localization.angle_value(1, 12, unview, in_view)
x2_ang =localization.angle_value(3, 12, unview, in_view)

y1_ang = localization.angle_value(4, 12, unview, in_view)
y2_ang =localization.angle_value(4, 12, unview, in_view)

x, y, z = localization.find_distance(x1_ang, x2_ang, y1_ang, y2_ang, 4)

print(x, y, z)
fig = plt.figure()
ax = Axes3D(fig)

Axes3D.scatter(x, y, z, zdir=1)