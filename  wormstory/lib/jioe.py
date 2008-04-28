from pygame.locals import *
from pygame import *

# Please handle the axis.

class jioe(object):

    def __init__(self):
        self.twin_joystick = joystick.Joystick(0)
        self.twin_joystick.init()
        self.buttons = self.twin_joystick.get_numbuttons()
        self.reset()
    
    def update(self,events):
        self.reset_up_down()
        
        for j in events:
            if j.type == JOYBUTTONDOWN:
                self.all_buttons[j.button]['down'] = 1
                self.all_buttons[j.button]['pressed'] = 1
            elif j.type == JOYBUTTONUP:
                self.all_buttons[j.button]['up'] = 1
                self.all_buttons[j.button]['pressed'] = 0

#        for i in range(0, self.buttons):
#            if self.all_buttons[i]['pressed'] :
#                self.all_buttons[i]['pressed_time'] += 1
#            else:
#                self.all_buttons[i]['pressed_time'] = 0

        self.quit=[k for k in events if k.type==QUIT]
        self.user=[e for e in events if e.type==USEREVENT]

        for j in events:
            if j.type == JOYAXISMOTION:
                self.all_axis[j.axis] = j.value
    
    def reset(self):
        self.quit=[]
        self.user=[]
        self.all_axis={}
        self.all_buttons = {}
        for i in range(0, self.buttons):
            self.all_buttons[i] = {}
        self.reset_up_down()

    def reset_up_down(self):
        for i in range(0, self.buttons):
            self.all_buttons[i]['down'] = 0
            self.all_buttons[i]['up'] = 0