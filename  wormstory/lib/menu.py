# Hi, I am menu Obj.

from pygame import *

class menu_item(sprite.Sprite):
	def __init__(self, g, title, location):
		sprite.Sprite.__init__(self)
		self.g = g
		self.title = title
		self.non_active_color = (0,100,0)
		self.active_color = (0, 150, 0)
		self.message_title(self.non_active_color)
		self.rect = self.image.get_rect(topleft=location)
	def message_title(self, color):
		self.image = self.g.game_info_font.render(self.title, 1, color)
	def update(self):
#		print 'bf mc: %s, si: %s' %(self.g.menu_choice_id, self.id)
		if self.g.menu_choice_id == self.id:
#			print 'mc: %s, si: %s' %(self.g.menu_choice_id, self.id)
			self.message_title(self.active_color)
		else:
			self.message_title(self.non_active_color)

class menu_play(menu_item):
	def __init__(self, g, id):
		self.id = id
		menu_item.__init__(self, g, 'PLAY', (120,0))

class menu_configure(menu_item):
	def __init__(self, g, id):
		self.id = id
		menu_item.__init__(self, g, 'CONFIGURE', (120,50))
		

class menu_quit(menu_item):
	def __init__(self, g, id):
		self.id = id
#		print 'init si %s' %self.id
		menu_item.__init__(self, g, 'QUIT', (120,100))

class menu(object):
	def __init__(self, g):
		self.g = g
		self.m_c = menu_configure(self.g, 2)
		self.m_p = menu_play(self.g, 1)
		self.m_q = menu_quit(self.g, 3)
		self.g.menu_group.add(self.m_c)
		self.g.menu_group.add(self.m_p)
		self.g.menu_group.add(self.m_q)
		self.g.menu_choice_id = 1 
	
	def update(self):
		if self.g.menu_choice_id < len(self.g.menu_group.sprites()):
#			print 'l: %s' %len(self.g.menu_group.sprites())
			if self.g.d.io.all_buttons[6]['down']:
				self.g.menu_choice_id += 1
		if self.g.menu_choice_id > 1:
			if self.g.d.io.all_buttons[1]['down']:
				self.g.menu_choice_id -= 1
		self.m_c.update()
		self.m_p.update()
		self.m_q.update()
		self.g.menu_group.draw(self.g.s.menu_s)
		self.g.s.menu_s.blit(
			self.g.game_info_small_font.render('http://www.milk2cows.com/dancingblock', 1,
				(0,0,128)), (40,300))