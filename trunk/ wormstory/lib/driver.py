# Hi I am jdriver ( higher then jioe )
from jioe import jioe
from kioe import kioe
from pygame import *
import sys

class driver(object):
	def __init__(self):
		if joystick.get_count():
			self.io = jioe()
		else:
			self.io = kioe()
#			
#			print 'You don\'t have Joystick.'
#			sys.exit()