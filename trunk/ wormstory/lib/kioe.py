from pygame.locals import *
from pygame import *

# Please handle the axis.

class kioe(object):

    def __init__(self):
        
        self.keymap = {
            97: 0, #a
            120: 1, #x
            119: 2, #w
            100: 3, #d
            99: 4, #c
            122: 5, #z
            101: 6, #e
            113: 7, #q
            32: 8,
            27: 9
            }
            
#        # Just need first joystick.
#        self.joystick = joystick.Joystick(0)
#        self.joystick.init()
        self.active_buttons = 10
        self.reset()
    
    def update(self,events):
        self.reset_up_down()
        
        for k in events:
            if k.type == KEYDOWN and self.keymap.has_key(k.key):
                self.all_buttons[ self.keymap[k.key] ]['down'] = 1
                self.all_buttons[ self.keymap[k.key] ]['pressed'] = 1
            elif k.type == KEYUP and self.keymap.has_key(k.key):
                self.all_buttons[ self.keymap[k.key] ]['up'] = 1
                self.all_buttons[ self.keymap[k.key] ]['pressed'] = 0

        for i in range(0, self.active_buttons):
            if self.all_buttons[i]['pressed'] :
                self.all_buttons[i]['pressed_time'] += 1
            else:
                self.all_buttons[i]['pressed_time'] = 0

        self.quit=[k for k in events if k.type==QUIT]
        self.user=[e for e in events if e.type==USEREVENT]

#        for j in events:
#            if j.type == JOYAXISMOTION:
#                self.all_axis[j.axis] = j.value
    
    def reset(self):
        self.quit=[]
        self.user=[]
#        self.all_axis={}
        self.all_buttons = {}
        for i in range(0, self.active_buttons):
            self.all_buttons[i] = {}
            self.all_buttons[i]['pressed'] = self.all_buttons[i]['pressed_time'] = 0
        self.reset_up_down()

    def reset_up_down(self):
        for i in range(0, self.active_buttons):
            self.all_buttons[i]['down'] = 0
            self.all_buttons[i]['up'] = 0