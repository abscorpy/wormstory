# Hi, I am menu Obj.

from pygame import *

class menu_item(sprite.Sprite):
	def __init__(self, g, title, location):
		sprite.Sprite.__init__(self)
		self.g = g
		self.title = title
		self.image = self.g.game_info_font.render(self.title, 1, (0,128,0))
		self.rect = self.image.get_rect(topleft=location)		

class menu_play(menu_item):
	def __init__(self, g):
		menu_item.__init__(self, g, 'PLAY', (120,0))
	def update(self):
		pass
	
class menu_configure(menu_item):
	def __init__(self, g):
		menu_item.__init__(self, g, 'CONFIGURE', (120,50))
	def update(self):
		pass
		

class menu(sprite.Sprite):
	def __init__(self, g):
		sprite.Sprite.__init__(self)
		self.g = g
		self.m_c = menu_configure(self.g)
		self.m_p = menu_play(self.g)
		self.g.menu_group.add(self.m_c)
		self.g.menu_group.add(self.m_p)
		self.image = self.g.s.menu_s
		self.rect = self.image.get_rect(topleft=(0,250))
	
	def update(self):
		self.m_c.update()
		self.m_p.update()
		self.g.menu_group.draw(self.image)
		self.g.s.menu_s.blit(	
			self.g.game_info_small_font.render('http://www.milk2cows.com/dancingblock', 1,
				(0,0,128)), (40,300))