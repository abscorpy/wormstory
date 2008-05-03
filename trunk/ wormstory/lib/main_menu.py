# Hi, I am menu Obj.

from menu_items import menu_configure, menu_play, menu_quit
from menu import menu

class main_menu(menu):
	def _add_item(self):
		self.g.m_dict = { 1:menu_play(self.g, self.g.GAME_PAGE, (120,0)),
						2:menu_configure(self.g, self.g.CONFIGURE_PAGE, (120,50)),
						3:menu_quit(self.g, self.g.QUIT_PAGE, (120,100)) }