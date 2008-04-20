from pygame.locals import *
from pygame import *

# Please handle the axis.

class jioe(object):

    def __init__(self):
        #Creates local variables
        self.reset()
    
    def update(self,events):
        """Dump the event list from pygame and it will sort them into lists for up, pressed, down, quit and user.
        When an up event is processed that key is removed from the pressed list and vice versa for down events."""
        #for every key released add the key to the up list
        self.up=[j.button for j in events if j.type==JOYBUTTONUP]
         #fill the down list the same way as the up list
        self.down=[j.button for j in events if j.type==JOYBUTTONDOWN]
        #remove any keys that were somehow pressed twice without being released or where pressed and released in one frame.
        for i in self.down:
            self.pressed=[x for x in self.pressed if x != i]
        #If a key is pushed down then it is being pressed until it is let up
        self.pressed+=self.down
        #for each key in the up list, filter those keys from the pressed list
        for i in self.up:
            self.pressed=[x for x in self.pressed if x != i]
        #quit and user actions don't have key values so they are just added directly to respective lists
        self.quit=[k for k in events if k.type==QUIT]
        self.user=[e for e in events if e.type==USEREVENT]

        # handle the joystick's axis.
        self.axis=[(j.axis, j.value) for j in events if j.type==JOYAXISMOTION]
 
        for i in self.axis:
            self.still=[x for x in self.still if x[0] != i[0]]
        
        self.still+=self.axis
        
    def reset(self):
        """Empties all the lists. Use this when going back to a menu otherwise keys could be stuck in the pressed list.""" 
        #clears all the lists by setting them equal to an empty list.
        self.up=[]
        self.down=[]
        self.pressed=[]
        self.quit=[]
        self.user=[]
        self.axis=[]
        self.still=[] 