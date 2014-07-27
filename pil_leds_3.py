#!/usr/bin/python

import Image, ImageDraw, ImageFilter
from time import sleep
import socket
from itertools import repeat

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = ("192.168.1.235", 9999)

fill = list(repeat(chr(0),3*110))

im = Image.new("RGB",(145,145))
im_d = ImageDraw.Draw(im)

disp1 = Image.new("RGB",(145,1))
disp2 = Image.new("RGB",(145,1))

# so I can set brightness in one place
br=32

# this creates a diagonal series of colored strips
# not sure why I did diagonal as straight vertical would work just as well!!
for i in range(0,120,30):
    im_d.polygon((i+5,0,i+9,0,0,i+9,0,i+5),(br,0,0))
    im_d.polygon((i+15,0,i+19,0,0,i+19,0,i+15),(0,br,0))
    im_d.polygon((i+25,0,i+29,0,0,i+29,0,i+25),(0,0,br))

im_d.polygon((125,0,129,0,0,129,0,125),(br,0,0))
im_d.polygon((135,0,139,0,0,139,0,135),(0,br,0))
im_d.polygon((140,0,144,0,0,144,0,140),(0,0,br))

for i in range(0,120,30):
   im_d.polygon((145,i+5,145,i+9,i+9,145,i+5,145),(br,0,0))
   im_d.polygon((145,i+15,145,i+19,i+19,145,i+15,145),(0,br,0))
   im_d.polygon((145,i+25,145,i+29,i+29,145,i+25,145),(0,0,br))

im_d.polygon((145,125,145,129,129,145,125,129),(br,0,0))
im_d.polygon((145,135,145,139,139,145,135,145),(0,br,0))

imb1 = im.filter(ImageFilter.BLUR)
#imb2 = imb1.filter(ImageFilter.BLUR)

while True:
   for slice in range(30,120,7):
      for theta in range(360):
         imr = imb1.rotate(theta)
	 #imr = im.rotate(theta)
         disp1.paste(imr.crop((0,slice,145,slice+1)))
	 disp2.paste(imr.crop((0,slice+17,145,slice+18)))
         sock.sendto(disp1.tostring()+str().join(fill)+disp2.tostring(),dest)
         sleep(.01)

