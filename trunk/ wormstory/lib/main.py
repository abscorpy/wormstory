from gobj import gobj
import sys

class main_loop(object):
	def __init__(self):
		self.g = gobj()
	def go_page(self, goto_page):
		if goto_page == self.g.GAME_PAGE:
			will_go_page = self.g.p.game_page()
		elif goto_page == self.g.CONFIGURE_PAGE:
			will_go_page = self.g.p.configure_page()
		elif goto_page == self.g.MAIN_PAGE:
			will_go_page = self.g.p.main_page()
		elif goto_page == self.g.QUIT_PAGE:
			self.g.p.quit_page()
			sys.exit()
		if not self.g.d.io.quit :
			return will_go_page
		else:
			sys.exit()
		
def main():
	game = main_loop()
#	game.g.set_bigblock()
	game.g.p.mark_page()
	p = game.g.p.main_page()
	while True:
		p = game.go_page(p)

if __name__ == "__main__":
	main()
