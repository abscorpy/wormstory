# Hi I am game_debug.

class game_debug(object):
	def __init__(self, g):
		self.g = g

	def debug_jioe(self):
		y = 140
		for j in self.g.j.down:
			self.g.screen.blit(
				self.g.sys_font.render('Press the JoyStick Button: %s' %str(j), 1, 
					(255,100,100)), (40, y))
			y = y + 20
			
		for j in self.g.j.pressed:
			self.g.screen.blit(
				self.g.sys_font.render('Pressed Buttons: %s' %str(j), 1,
					(255,100,100)),(40, y))
			y = y + 20
		
		for j in self.g.j.axis:
			self.g.screen.blit(
				self.g.sys_font.render('AXIS: %s, VALUE: %s' %(str(j[0]), str(j[1])), 1,
					(255,100,100)),(40, y))
			y = y + 20

		for j in self.g.j.still:
			self.g.screen.blit(
				self.g.sys_font.render('AXIS: %s, VALUE: %s' %(str(j[0]), str(j[1])), 1,
					(255,100,100)),(40, y))
			y = y + 20