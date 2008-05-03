# Hi I am configure menu

from menu import menu
from menu_items import menu_back, menu_play, menu_quit

class configure_menu(menu):
	def _add_item(self):						
		self.g.m_list = [ menu_play(self.g, self.g.GAME_PAGE, (10,60)),
						menu_back(self.g, self.g.MAIN_PAGE, (10,90)),
						menu_quit(self.g, self.g.QUIT_PAGE, (10,120))
						]
						