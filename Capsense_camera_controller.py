from pynput.mouse import Listener
from adafruit_servokit import ServoKit
import time
from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.rotation = 0

kit = ServoKit(channels=16)

prevx = 0
prevy = 0

kit.servo[0].angle = 0
kit.servo[1].angle = 0
 
angle0 = 0
angle1= 0

camera.start_preview()

def on_move(x, y):
    global prevx, prevy, angle0, angle1
    
    #print('Mouse moved to ({0}, {1})'.format(x, y))
    #print('prev moved to ({0}, {1})'.format(prevx, prevy))
    
    print('servo0 {0}'.format(angle0))
    
    if((prevx-x)>0) and angle0 >= 0 and angle0 <= 180:
        kit.servo[1].angle = angle0
        if(angle0 < 180):
            angle0 = angle0 + 10
        print('servo0 + {0}'.format(angle0))
        
    elif((prevx-x)<0) and angle0 >= 0 and angle0 <= 180:
        
        kit.servo[1].angle = angle0
        if(angle0 > 0):
            angle0 = angle0 - 10
        print('servo0 - {0}'.format(angle0))
     
    if((prevy-y)<0) and angle1 >= 0 and angle1 <= 180:
          kit.servo[0].angle = angle1
          if(angle1 < 180):
              angle1 = angle1 + 10
          print('servo1 + {0}'.format(angle1))
        
    elif((prevy-y)>0) and angle1 >= 0 and angle1 <= 180:
        kit.servo[0].angle = angle1
        if(angle1 > 0):
            angle1 = angle1 - 10
        print('servo1 - {0}'.format(angle1))
    
    prevx = x
    prevy = y
    
    
    


def on_click(x, y, button, pressed):
    pass

def on_scroll(x, y, dx, dy):
    pass

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
    
    