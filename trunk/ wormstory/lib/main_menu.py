# Hi, I am menu Obj.

from menu_title_items import menu_configure, menu_play, menu_quit
from menu_menu_s import menu_menu_s

class main_menu(menu_menu_s):
	def _add_item(self):
		self.g.m_list = [ menu_play(self.g, self.g.GAME_PAGE, (10,60)),
						menu_configure(self.g, self.g.CONFIGURE_PAGE, (10,90)),
						menu_quit(self.g, self.g.QUIT_PAGE, (10,120)) ]