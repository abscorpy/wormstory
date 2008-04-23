# Hi I am game_debug.
from pygame import *

class game_debug(object):
	def __init__(self, g):
		self.g = g

	def debug_jioe(self):
# Please change this. structure is changed.
		y = 140
#		for j in self.g.j.down:
#			self.g.screen.blit(
#				self.g.sys_font.render('Press the JoyStick Button: %s' %str(j), 1, 
#					(255,100,100)), (40, y))
#			y = y + 20
#			
#		for j in self.g.j.pressed:
#			self.g.screen.blit(
#				self.g.sys_font.render('Pressed Buttons: %s' %str(j), 1,
#					(255,100,100)),(40, y))
#			y = y + 20
		
		for j in self.g.j.all_axis.keys():
			self.g.screen.blit(
				self.g.sys_font.render('AXIS: %s, VALUE: %s' %(str(j), str(self.g.j.all_axis[j])), 1,
					(255,100,100)),(40, y))
			y = y + 20
	
	def debug_pressed_time(self):
		draw.line(self.g.screen, (255, 255, 255), 
			(self.g.slave_spider.rect.left, 
				self.g.slave_spider.rect.top - 5),
			(self.g.slave_spider.rect.left + self.g.j.all_buttons[18]['pressed_time'] * 5,
			self.g.slave_spider.rect.top - 5), 3)
