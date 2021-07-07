from PIL import Image
import serial
from PIL import Image as im
import time
import DATA as d


def main(m):
   im_1 = Image.open(m,mode='r')

   width, height = im_1.size
   print( im_1.mode)
   B = im_1.tobytes()
   print(width,height)
   i = 0
   list1 = []  # define a main function
   for x in B:
       list1.insert(i,x)
       i++1

   o = input("input :")
   ser = serial.Serial(o, baudrate=9600, timeout=0.1)

   time.sleep(2)
   ser.write(b'256\n')
   print(list1)
   time.sleep(3)
   q=0
   def load():
       global q
       q+=1
       g=q/280*100
       print("data sending complete :",int(g),"%")
   for x in list1:
        K=d.data(x)

        ser.write(K)
        load()
        print(K)
        

        print(x)
        time.sleep(3)
   for x in range(3):
        time.sleep(2)
        ser.write(b'FFF\n')
s=input()
main(s)