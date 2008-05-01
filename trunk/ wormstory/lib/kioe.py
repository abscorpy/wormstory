from pygame.locals import *
from pygame import *
from ioe import ioe

# Please handle the axis.

class kioe(ioe):

    def __init__(self):
        
        self.keymap = {
            K_a: 0, #a
            K_x: 1, #x
            K_w: 2, #w
            K_d: 3, #d
            K_c: 4, #c
            K_z: 5, #z
            K_e: 6, #e
            K_q: 7, #q
            K_SPACE : 8,
            K_ESCAPE: 9
            }
            
        self.buttons_init()
    
    def events_detect(self, events):
        for k in events:
            if k.type == KEYDOWN and self.keymap.has_key(k.key):
                self.all_buttons[ self.keymap[k.key] ]['down'] = 1
                self.all_buttons[ self.keymap[k.key] ]['pressed'] = 1
            elif k.type == KEYUP and self.keymap.has_key(k.key):
                self.all_buttons[ self.keymap[k.key] ]['up'] = 1
                self.all_buttons[ self.keymap[k.key] ]['pressed'] = 0