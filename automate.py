# To get mouse coordinates, use cmd+shift+4

import os
import sys
import time

from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import CGEventSetFlags
from Quartz.CoreGraphics import CFRelease
from Quartz.CoreGraphics import kCGEventFlagMaskCommand
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz.CoreGraphics import CGEventCreateKeyboardEvent

# Mouse targets in (x,y) coordinates
targets =  {
  'basic':    (51, 802),
  'name':     (120, 870),
  'settings': (150, 800),
  'qnumber':  (170, 950),
  'qlist':    (280, 950),
}

def mouseEvent(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(
                   None, 
                   type, 
                   (posx,posy), 
                   kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
        mouseEvent(kCGEventMouseMoved, posx,posy);

def mouseclick(posx,posy):
        # uncomment this line if you want to force the mouse 
        # to MOVE to the click location first (I found it was not necessary).
        #mouseEvent(kCGEventMouseMoved, posx,posy);
        mouseEvent(kCGEventLeftMouseDown, posx,posy);
        mouseEvent(kCGEventLeftMouseUp, posx,posy);

def keypress(keycode):
  theEvent = CGEventCreateKeyboardEvent(None, keycode, True)
  CGEventPost(kCGHIDEventTap, theEvent)

def cmdC():
  theEvent = CGEventCreateKeyboardEvent(None, 0x08, True)
  CGEventSetFlags(theEvent, kCGEventFlagMaskCommand)
  CGEventPost(kCGHIDEventTap, theEvent)
  #CFRelease(theEvent)

def cmdV():
  theEvent = CGEventCreateKeyboardEvent(None, 0x09, True)
  CGEventSetFlags(theEvent, kCGEventFlagMaskCommand)
  CGEventPost(kCGHIDEventTap, theEvent)
  #CFRelease(theEvent)



activate_qlab = """ osascript -e 'tell application "Qlab" to activate' """

cmd = """ osascript -e 'tell application "System Events" to keystroke "m" using {command down}' """

resize_qlab = """ osascript -e 'set bounds of window 1 of application "Qlab" to {0,0,1200, 1000}' """

printable_codes = {
  '0': 0x52,
  '1': 0x53,
  '2': 0x54,
  '3': 0x55,
  '4': 0x56,
  '5': 0x57,
  '6': 0x58,
  '7': 0x59,
  '8': 0x5B,
  '9': 0x5C,
  '.': 0x2F,
  ' ': 0x31
}

control_codes = {
  'return':   0x24,
  'tab':      0x30,
  'esc':      0x35
}

def toKeyCodeArr(string):
  result = []
  for letter in string:
    result.append(printable_codes[letter])
  return result


def quartzType(keycodeArr):
  for k in keycodeArr:
    keypress(k)

# minimize active window
os.system(activate_qlab)
#os.system(resize_qlab)


#res = toKeyCodeArr('123')
#quartzType(res)


time.sleep(0.1)
cmdC()
cmdV()
#mouseclick(*targets['settings'])
#mouseclick(*targets['basic'])
