


v=36

import serial
import numpy
from PIL import Image
from PIL import Image as im
import time
import rd as r

i=0
global z
z=False
global m
m=True
list1 = []
o = input("input :")
ser = serial.Serial(o, baudrate=9600, timeout=0.1)
while v==36:
    arduino = ser.readline()
    arduind = arduino.decode()

    if arduino==b'256\n':
        z=True
    elif arduino==b'fff\n'or arduino==b'FFF\n':
        break
    if z==True and r.data(arduino)!=None:
       K=r.data(arduino)
       list1.insert(i,K)
       i++1
       print(K)



list1.reverse()
print(list1)
c = bytes(list1)
data = im.frombytes("RGBA", (7, 10), c)#change the things depending on the inputs data program :MAIN"inputs.py" put the photo and take these numbers and put it here
data.save('reee.png')#photo name





