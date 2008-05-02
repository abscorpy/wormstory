from gobj import gobj

class main_loop(object):
	def __init__(self):
		self.g = gobj()

def main():
	game = main_loop()
	game.g.set_bigblock()
	game.g.p.mark_page()
	goto_page = game.g.p.title_page()
	if goto_page == game.g.GAME_PAGE:
		game.g.p.game_page()
	elif goto_page == game.g.CONFIGURE_PAGE:
		game.g.p.configure_page()
	elif goto_page == game.g.QUIT_PAGE:
		game.g.p.quit_page()

if __name__ == "__main__":
	main()
