# Hi, I am menu Obj.

from menu_items import menu_configure, menu_play, menu_quit

class menu(object):
	def __init__(self, g):
		self.g = g
		self.g.menu_choice_id = 1
		self._add_item()
	
	def _add_item(self):
		self.m_c = menu_configure(self.g, 2, (120,50))
		self.m_p = menu_play(self.g, 1, (120,0))
		self.m_q = menu_quit(self.g, 3, (120,100))
		self.g.menu_group.add(self.m_c)
		self.g.menu_group.add(self.m_p)
		self.g.menu_group.add(self.m_q)
	
	def update(self):
		if self.g.menu_choice_id < len(self.g.menu_group.sprites()):
			if self.g.d.io.all_buttons[6]['down']:
				self.g.menu_choice_id += 1
		if self.g.menu_choice_id > 1:
			if self.g.d.io.all_buttons[1]['down']:
				self.g.menu_choice_id -= 1
				
		self.g.menu_group.update()
		self.g.menu_group.draw(self.g.s.menu_s)
		self.g.s.menu_s.blit(
			self.g.game_info_small_font.render('http://www.milk2cows.com/dancingblock', 1,
				(0,0,128)), (40,320))