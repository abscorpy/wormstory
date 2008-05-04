# Hi I am configure menu

from menu import menu
from menu_items import menu_play, menu_quit, menu_main

class configure_menu(menu):
	def _add_item(self):						
		self.g.m_list = [ menu_play(self.g, self.g.GAME_PAGE, (10,60)),
						menu_main(self.g, self.g.MAIN_PAGE, (10,90)),
						menu_quit(self.g, self.g.QUIT_PAGE, (10,120))
						]
						