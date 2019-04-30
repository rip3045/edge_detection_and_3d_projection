"""These are the functions controlling angle output and distance"""
import math

def fov_fac(fov):
	"""Processing factors for the field of view, avoiding repeating functions"""
	unview = ((180 - fov) / 2)*3.1415/180
	in_view = fov*3.1415/180

	return unview, in_view

def angle_value(x_value, x_size, unview, in_view):
	"""This function takes a pixel and returns the angle from center"""
	x_ang = (x_value/x_size)*in_view + unview

	return x_ang
	

def find_distance(x1_ang, x2_ang, y1_ang, y2_ang, d_btw):
	"""This function returns the 3d coordinate of matched pixels, from center of system
	these coordinates, scaled by d are real world distances"""
	length = d_btw/((1/(math.tan(x1_ang)))+(1/(math.tan(x2_ang))))
	x_dist = -1*x2_ang/(math.tan(x1_ang)) - (d_btw/2)								###using this angle to avoid flipping orientation
	y_dist = -d_btw*(1/math.tan(y1_ang+y2_ang/2))

	return x_dist, y_dist, length




if __name__=='__main__':
	print("This is the module for the distance and angle functions")
