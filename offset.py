# Adding an offset for contrast in an image

from images import *

offset = int(input("Enter offset percentage (0-100): "))

def autoContrast(p):
    
    x = ((p[0]+p[1]+p[2])/3)  # AGGREGATE OF THE R,G,B VALUES
    
    r = int( p[0] * ( 1 + ((offset/200) if x > 127.5 else (-offset/200) ) ) )  # Divide by 200 to get half the value for light and dark pixels
    g = int( p[1] * ( 1 + ((offset/200) if x > 127.5 else (-offset/200) ) ) )
    b = int( p[2] * ( 1 + ((offset/200) if x > 127.5 else (-offset/200) ) ) )
    
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255
    return (r, g, b)

a = readImage(r"images/trump.jpg") 

w, h = len(a[0]), len(a)

b = [[ autoContrast(a[i][j]) for j in range(w)] for i in range(h)]

writeImage(b, "images/offset.jpg") 

print("Ready")  # You can locate the output file in the assigned folder
