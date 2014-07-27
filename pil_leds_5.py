#!/usr/bin/python

import Image, ImageDraw, ImageFilter
from time import sleep
import socket
from itertools import repeat
from random import randrange

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = ("192.168.1.235", 9999)

fill = list(repeat(chr(0),3*110))

im = Image.new("RGB",(145,1450))
imd = ImageDraw.Draw(im)

disp1 = Image.new("RGB",(145,1))
disp2 = Image.new("RGB",(145,1))

br=64
# create a bunch of random arcs
for i in range(256):
   x1 = randrange(145-50)
   x2 = x1 + randrange(35,50)
   y1 = randrange(1450-50)
   y2 = y1 + randrange(35,50)
   imd.arc((x1,y1,x2,y2),randrange(-45,45),randrange(180-45,180+45),(randrange(br),randrange(br),randrange(br)))


#imb1 = im.filter(ImageFilter.BLUR)
#imb2 = imb1.filter(ImageFilter.BLUR)

while True:
   for slice in range(0,1445):
     disp1.paste(im.crop((0,slice,145,slice+1)))
     disp2.paste(im.crop((0,slice+4,145,slice+5)))
     sock.sendto(disp1.tostring()+str().join(fill)+disp2.tostring(),dest)
     sleep(.008)

