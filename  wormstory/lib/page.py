# Hi, I am page.
from pygame import *

class page(object):
	def __init__(self, g):
		self.g = g
	def title_page(self):
		#title page:
		while not self.g.d.io.quit and not self.g.d.io.all_buttons[8]['down']:
			self.g.event_update()
			self.g.s.draw()
			
			# Set black.
			black_s = Surface((600,600))
			black_s.fill((0,0,0))
			self.g.s.playarea_s.blit(black_s, (0,0))
			
			self.g.s.playarea_s.blit(
				self.g.game_info_font.render('Dancing Block', 1, (180,0,0)), (40,150))
			self.g.s.playarea_s.blit(
				self.g.game_info_font.render('Milker\'s Solo Game', 1, 
						(100,100,100)), (40,200))
			self.g.s.playarea_s.blit(
				self.g.game_info_font.render('Copyleft (cl) by', 1, (100,100,100)), (40,240))	
			self.g.s.playarea_s.blit(
				self.g.game_info_font.render('http://www.milk2cows.com', 1,
						(100,100,100)), (50,280))	
			self.g.s.playarea_s.blit(
				self.g.game_info_font.render('2008-4', 1, 
						(100,100,100)), (40,320))
			if joystick.get_count():
				self.g.s.playarea_s.blit(
					self.g.game_info_font.render('PRESS [select] TO PLAY', 1, 
						(0,128,0)), (40,500))
				self.g.s.playarea_s.blit(
					self.g.game_info_small_font.render('^^ USE dance-pad TO PLAY', 1, 
						(0,0,128)), (40,550))
			else:
				self.g.s.playarea_s.blit(
					self.g.game_info_font.render('PRESS [SPACE] TO PLAY', 1, 
						(0,128,0)), (40,500))
				self.g.s.playarea_s.blit(
					self.g.game_info_small_font.render('^^ USE KEYBROAD TO PLAY', 1, 
						(0,0,128)), (40,550))
			display.flip()
		
	def game_page(self):
		while not self.g.d.io.quit and not self.g.d.io.all_buttons[9]['down'] : #21
			self.g.event_update()
			if self.g.score > 0:
				self.g.groundblock_group.update()
			else:
				self.g.s.playarea_s.blit(
					self.g.game_info_font.render('GAMEOVER', 1, (180,0,0)), (210,210))
			self.g.s.draw()
			self.g.groundblock_group.draw(self.g.s.playarea_s)
			self.g.s.playinfo_s.blit(
					self.g.game_info_font.render('s: %s' %self.g.score, 1,
						(180,0,0)),(10, 470))
			self.g.s.playinfo_s.blit(
					self.g.game_info_font.render('level: %s' %(self.g.hit_block/10), 1,
						(180,0,0)),(10, 510))
			self.g.s.playinfo_s.blit(
					self.g.game_info_font.render('hit: %s' %self.g.hit_block, 1,
						(180,0,0)),(10, 550))
			display.flip()