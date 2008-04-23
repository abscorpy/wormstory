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
        self.up=[j.button for j in events if j.type==JOYBUTTONUP]
        self.down=[j.button for j in events if j.type==JOYBUTTONDOWN]

        for i in self.down:
            self.all_buttons[i]['pressed'] = 1

        for i in self.up:
            self.all_buttons[i]['pressed'] = 0

        for i in range(0, self.buttons):
            if self.all_buttons[i]['pressed'] :
                self.all_buttons[i]['pressed_time'] += 1
            else:
                self.all_buttons[i]['pressed_time'] = 0

        self.quit=[k for k in events if k.type==QUIT]
        self.user=[e for e in events if e.type==USEREVENT]

        for j in events:
            if j.type == JOYAXISMOTION:
                self.all_axis[j.axis] = j.value
    
    def reset(self):
        self.up=[]
        self.down=[]
        self.quit=[]
        self.user=[]
        self.all_axis={}
        self.all_buttons = {}
        for i in range(0, self.buttons):
            self.all_buttons[i] = {}