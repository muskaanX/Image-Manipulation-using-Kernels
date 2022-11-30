# Edge Detection using Kernels

from images_fcp import *


kernel_identity = [
	[ 0, 0, 0, 0, 0],
	[ 0, 0, 0, 0, 0],
	[ 0, 0, 1, 0, 0],
	[ 0, 0, 0, 0, 0],
	[ 0, 0, 0, 0, 0]
]

kernel_edgy = [
	[ 0,  0,  -1,  0,  0],
	[ 0, -1,   1, -1,  0],
	[-1,  1,   4,  1, -1],
	[ 0, -1,   1, -1,  0],
	[ 0,  0,  -1,  0,  0]
]

a = readImage(r"images\jett_valorant.png")  

b = convolve(a, kernel_edgy)

writeImage(b, "images\5-2.jpg")  

print("Ready")  # You can find the output file in the assigned folder
