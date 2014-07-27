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
# create a bunch of random lines
for i in range(64):
   imd.line((randrange(144),randrange(1440),randrange(144),randrange(1440)),(randrange(br),randrange(br),randrange(br)))


#imb1 = im.filter(ImageFilter.BLUR)
#imb2 = imb1.filter(ImageFilter.BLUR)

while True:
   for slice in range(0,1445):
     disp1.paste(im.crop((0,slice,145,slice+1)))
     disp2.paste(im.crop((0,slice+4,145,slice+5)))
     sock.sendto(disp1.tostring()+str().join(fill)+disp2.tostring(),dest)
     sleep(.008)

