# Hi, I am menu Obj.

class menu(object):
	def __init__(self, g, s):
		self.g = g
		self.s = s
		self.g.menu_choice_id = 0
	
	def set_menu_group(self):
		self.g.menu_group.empty()
		self._add_item()
		for m in self.g.m_list:
			self.g.menu_group.add(m)

	def _add_item(self):
		pass
	
	def update(self):
		# Is it a good idea. everytime to recreate the menubar ? 
		self.set_menu_group()
		if self.g.menu_choice_id < (len(self.g.menu_group.sprites()) - 1):
			if self.g.d.io.all_buttons[6]['down']:
				self.g.menu_choice_id += 1
		if self.g.menu_choice_id > 0:
			if self.g.d.io.all_buttons[1]['down']:
				self.g.menu_choice_id -= 1
		
		self.s.blit(self.g.menu_background_image, (0,0))
		self.g.menu_group.update()
		self.g.menu_group.draw(self.s)
		self.g.s.playarea_s.blit(
			self.g.game_info_small_font.render('http://www.milk2cows.com/dancingblock', 1,
				(0,0,128)), (40,570))