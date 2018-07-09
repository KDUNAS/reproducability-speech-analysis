# May 1, 2018
'''
 These codes are to detect edge of a camaro car in a 
 rgb picture by convolution.
 The rgb picture experiences the following process:
 	 1 rgb -> grey -> binary -> show edge
 	 2 rgb -> grey -> convolution -> invert -> show edge
 You can find different visual effects of two methods.
'''
# coding:utf-8


# import libraries
from PIL import Image
import numpy as np
import os
from skimage import io


# load a rgb picture and show it
im_rgb = Image.open('./Camaro.jpg')
im_rgb.show()
im_rgb_array = np.array(im_rgb)

# show some details of the rgb picture
print (im_rgb_array)
print (im_rgb_array[0][0])
print (len(im_rgb_array))
print (len(im_rgb_array[0]))
print (len(im_rgb_array[0][0]))

# covert to grey level picture
im_grey = Image.open('./Camaro.jpg')
im_grey = im_grey.convert('L')
try:
 	  im_grey.save("Camaro_Grey.jpg")
except IOError:
 	  print ("Cannot convert")
im_grey.show()
im_grey_array = np.array(im_grey)

# setup a converting table with constant threshold 
threshold = 45
table = []
for i in range( 256 ):
     if i < threshold:
        table.append(0)
     else :
        table.append(1)

# convert to binary picture by the table 
im_binary = im_grey.point(table,"1")
im_binary.save( "Camaro_Binary.jpg" ) 
im_binary.show()
im_binary_array = np.array(im_binary)


# convolution kernel array
# This array is named Laplace operator.
# It is used to detect the edge.
conv_input = np.array([[ 1,  1,  1],       
                       [ 1, -8,  1],
                       [ 1,  1,  1]])


# convolution defined function
# import image array and convolution kernel array
def conv (im_array, conv_x):   
	im_copy = im_array.copy() 
	height, width = im_copy.shape
	for i in range(0, height-2):   
		for j in range(0, width-2):
			tmp = (im_array[(i):(i+3),(j):(j+3)]*conv_x).sum()
			if tmp > 255:
				tmp = 255
			elif tmp < 0:
				tmp = 0
			im_copy[i][j] = tmp
	return im_copy 

# import grey image array to function
# output edge detection of grey image. 
im_conv = conv(im_grey_array, conv_input)

# show result
new_im = Image.fromarray(im_conv)
new_im.show()
new_im.save("Camaro_Conv.jpg")

# To make the result more obvious, deal with it further
new_im_arrray = np.array(new_im)

# invert defined function
def invert (im_array):
	im_copy = im_array.copy() 
	height, width = im_copy.shape
	for i in range(0, height-2):   
		for j in range(0, width-2):
			if im_copy[i][j] > 100:
				im_copy[i][j] = 0
			else:
				im_copy[i][j] = 255
	return im_copy

# import output image after convolution to make it obvious
im_invert = invert(new_im_arrray)
new_im_invert = Image.fromarray(im_invert)

# show result again
new_im_invert.show()
new_im_invert.save("Camaro_Conv_Invert.jpg")