from pygame.locals import *
from pygame import *

# Please handle the axis.

class ioe(object):
   
    def buttons_init(self):
        self.active_buttons = len(self.keymap.keys())
        self.reset()
    
    def update(self,events):
        self.reset_up_down()
        self.events_detect(events)

        for i in range(0, self.active_buttons):
            if self.all_buttons[i]['pressed'] :
                self.all_buttons[i]['pressed_time'] += 1
            else:
                self.all_buttons[i]['pressed_time'] = 0

        self.quit=[k for k in events if k.type==QUIT]
        self.user=[e for e in events if e.type==USEREVENT]
    
    def reset(self):
        self.quit=[]
        self.user=[]
        self.all_axis={}
        self.all_buttons = {}
        for i in range(0, self.active_buttons):
            self.all_buttons[i] = {}
            self.all_buttons[i]['pressed'] = self.all_buttons[i]['pressed_time'] = 0
        self.reset_up_down()

    def reset_up_down(self):
        for i in range(0, self.active_buttons):
            self.all_buttons[i]['down'] = 0
            self.all_buttons[i]['up'] = 0