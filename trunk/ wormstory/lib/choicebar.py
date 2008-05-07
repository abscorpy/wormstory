# choicebar object
from pygame import *

class choicebar(object):
	def __init__(self, g, s, pos, y):
		self.g = g
		self.s = s
		self.choice_y = y
		self.speed = 30
		self.pos = pos
	def _count_pos(self, (pass_pos)):
		result_pos = (self.pos[0] + pass_pos[0], self.pos[1] + pass_pos[1])
		return result_pos
	
	def _set_configobj_value(self, y):
		pass
	
	def update(self):
		
		if self.choice_y < 340:
			if self.g.d.io.all_buttons[4]['down']:
				self.choice_y += self.speed
		if self.choice_y > 0:
			if self.g.d.io.all_buttons[3]['down']:
				self.choice_y -= self.speed
		
		self._set_configobj_value(self.choice_y)
		
		draw.line(self.s, (128,128,0), 
			self._count_pos((0,10)), self._count_pos((340,10)), 3)
		draw.line(self.s, (128,0,128), 
			self._count_pos((self.choice_y,0)), self._count_pos((self.choice_y,20)), 3)