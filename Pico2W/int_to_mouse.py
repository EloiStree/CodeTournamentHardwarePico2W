from adafruit_hid.mouse import Mouse



import time
import board
import digitalio
import usb_hid

class IntS2WToMouse:
  
    def __init__(self):
        self.mouse = Mouse(usb_hid.devices)


    def int_to_mouse(self, value: int) :
       
       return
        # # Move Up 2001
        # if value == 2001:
        #      self.mouse.move(y=-10)
        # # Move Down 2002
        # elif value == 2002:
        #      self.mouse.move(y=10)
        # # Move Left 2003
        # elif value == 2003:
        #      self.mouse.move(x=-10)
        # # Move Right 2004
        # elif value == 2004:
        #      self.mouse.move(x=10)
        # # Left Click 2010
        # elif value == 2010:
        #      self.mouse.click(Mouse.LEFT_BUTTON)
        # # Right Click 2011
        # elif value == 2011:
        #      self.mouse.click(Mouse.RIGHT_BUTTON)
        # else:
        #     pass

    #     if False: # EXPERIMENT WITH MOUSE 🏳️
    # for _ in range(10):
    #     mouse.move(x=10, y=10, wheel=0)
    #     mouse.press(Mouse.LEFT_BUTTON)
    #     mouse.release(Mouse.LEFT_BUTTON)