# Hi I am playing menu

from menu_menu_s import menu_menu_s
from menu_title_items import menu_quit, menu_configure, menu_back

class playing_menu(menu_menu_s):
	def _add_item(self):						
		self.g.m_list = [ menu_back(self.g, self.g.GAME_PAGE, (10,60)),
						menu_configure(self.g, self.g.CONFIGURE_PAGE, (10,90)),
						menu_quit(self.g, self.g.QUIT_PAGE, (10,120))
						]
						