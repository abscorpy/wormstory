from pygame.locals import *
from pygame import *
from ioe import ioe

# Please handle the axis.

class jioe(ioe):

    def __init__(self):
        self.keymap = {
            7: 0, #a
            2: 1, #x
            6: 2, #w
            0: 3, #d
            3: 4, #c
            5: 5, #z
            1: 6, #e
            4: 7, #q
            8: 8,
            9: 9
            }
            
        # Just need first joystick.
        self.joystick = joystick.Joystick(0)
        self.joystick.init()
        self.buttons_init()
        
    def events_detect(self, events):        
        for j in events:
            if j.type == JOYBUTTONDOWN:
                self.all_buttons[ self.keymap[j.button] ]['down'] = 1
                self.all_buttons[ self.keymap[j.button] ]['pressed'] = 1
            elif j.type == JOYBUTTONUP:
                self.all_buttons[ self.keymap[j.button] ]['up'] = 1
                self.all_buttons[ self.keymap[j.button] ]['pressed'] = 0

        for j in events:
            if j.type == JOYAXISMOTION:
                self.all_axis[j.axis] = j.value
    
