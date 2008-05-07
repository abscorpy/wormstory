# Hi, I am menu Obj.

from menu_item import menu_item
from menu import menu

class main_menu(menu):
	def _add_item(self):
		if self.g.can_replay:
			self.g.m_list = [ menu_item(self.g, 'PLAY NEW',  (10,30), self.g.NEW_GAME_PAGE),
						menu_item(self.g, 'PLAY AGAIN',  (10,60), self.g.GAME_PAGE),
						menu_item(self.g, 'CONFIGURE', (10,90), self.g.CONFIGURE_PAGE),
						menu_item(self.g, 'QUIT', (10,120), self.g.QUIT_PAGE) ]
		else:
			self.g.m_list = [ menu_item(self.g, 'PLAY NEW',  (10,60), self.g.NEW_GAME_PAGE),
						menu_item(self.g, 'CONFIGURE', (10,90), self.g.CONFIGURE_PAGE),
						menu_item(self.g, 'QUIT', (10,120), self.g.QUIT_PAGE) ]			