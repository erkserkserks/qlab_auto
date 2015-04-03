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
  CGEventSetFlags(theEvent, 0)
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

def cmdA():
  theEvent = CGEventCreateKeyboardEvent(None, 0x00, True)
  CGEventSetFlags(theEvent, kCGEventFlagMaskCommand)
  CGEventPost(kCGHIDEventTap, theEvent)
  CGEventSetFlags(theEvent, ~kCGEventFlagMaskCommand)
  #CFRelease(theEvent)

activate_qlab = """ osascript -e 'tell application "Qlab" to activate' """

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


def quartzType(string):
  # Convert string to osx keycodes
  keycodes = []
  for letter in string:
    keycodes.append(printable_codes[letter])

  # Press keys
  for k in keycodes:
    keypress(k)

def overwriteType(string):
  cmdA()
  quartzType(string)

# Generate list of cues to populate qlab
def genCueList(cue_list_num, cue_start, cue_end, increment):
  cue_list = []
  
  for i in xrange(cue_start, cue_end + increment, increment):
    name = "{0}.{1}".format(cue_list_num, i)
    qnumber = str(i)
    qlist = str(cue_list_num)

    cue_list.append({'name': name, 'qnumber': qnumber, 'qlist': qlist})

  return cue_list

def populateQlab(cue_list):
  for cue in cue_list:
    cmdC()
    cmdV()

    mouseclick(*targets['basic'])
    mouseclick(*targets['name'])
    overwriteType(cue['name'])

    mouseclick(*targets['settings'])
    mouseclick(*targets['qnumber'])
    overwriteType(cue['qnumber'])
    mouseclick(*targets['qlist'])
    overwriteType(cue['qlist'])
    keypress(control_codes['return'])

if __name__ == "__main__":
# Resize qlab window to expected dimensions
  os.system(activate_qlab)
  os.system(resize_qlab)

  populateQlab(genCueList(1, 2, 6, 2))
  populateQlab(genCueList(2, 0, 142, 2))
  populateQlab(genCueList(3, 0, 32, 2))
  populateQlab(genCueList(4, 0, 2, 2))
  populateQlab(genCueList(5, 0, 58, 2))
  populateQlab(genCueList(6, 0, 32, 2))
  populateQlab(genCueList(7, 0, 50, 2))
  populateQlab(genCueList(8, 0, 2, 2))
  populateQlab(genCueList(9, 0, 46, 2))
  populateQlab(genCueList(10, 0, 70, 2))
  populateQlab(genCueList(11, 0, 66, 2))
  populateQlab(genCueList(12, 0, 6, 2))
  populateQlab(genCueList(13, 0, 60, 2))
  populateQlab(genCueList(14, 0, 26, 2))
  populateQlab(genCueList(15, 0, 26, 2))
  populateQlab(genCueList(16, 0, 2, 2))
  populateQlab(genCueList(17, 0, 16, 2))
