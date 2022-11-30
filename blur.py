# Blurring Images using Kernels

from images import *

kernel_identity = [
	[ 0, 0, 0, 0, 0],
	[ 0, 0, 0, 0, 0],
	[ 0, 0, 1, 0, 0],
	[ 0, 0, 0, 0, 0],
	[ 0, 0, 0, 0, 0]
]

# GAUSSIAN BLUR METHOD

kernel_blur = [
	[ 1/256,  4/256,   6/256,  4/256,  1/256],
	[ 4/256, 16/256,  24/256, 16/256,  4/256],
	[ 6/256, 24/256,  36/256, 24/256,  6/256],
	[ 4/256, 16/256,  24/256, 16/256,  4/256],
	[ 1/256,  4/256,   6/256,  4/256,  1/256]
]

# AVERAGE BLUR METHOD

'''kernel_blur = [
	[ 1/25,  1/25,   1/25,  1/25,  1/25 ],
	[ 1/25,  1/25,   1/25,  1/25,  1/25 ],
	[ 1/25,  1/25,   1/25,  1/25,  1/25 ],
	[ 1/25,  1/25,   1/25,  1/25,  1/25 ],
	[ 1/25,  1/25,   1/25,  1/25,  1/25 ]
]'''

a = readImage(r"images/landscape.jpg")

b = convolve(a, kernel_blur)

writeImage(b, "images/5-3.jpg")

print("Ready")  # You can locate the output file in the assigned folder
