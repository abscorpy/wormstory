# Hi, I am page.
from pygame import *

class page(object):
	def __init__(self, g):
		self.g = g
		self.clock = time.Clock()
		self.mark_time = 2
		self.playing_configure_state = 0
		
	def mark_page(self):
		while self.mark_time:
			self.clock.tick(1)
			self.mark_time -= 1
			self.g.screen.blit(
				self.g.cow_logo_image.convert_alpha(), (250,100)
				)
			display.flip()
		self.mark_time = 2
		while self.mark_time:	
			self.clock.tick(1)
			self.mark_time -= 1
			self.g.screen.blit(
				self.g.game_info_font.render('Milker\'s Solo Game', 1, 
						(100,100,100)), (200,500))
			display.flip()
		self.mark_time = 2
		while self.mark_time:	
			self.clock.tick(1)
			self.mark_time -= 1
			self.g.screen.blit(self.g.s.black_s, (0,0))
			self.g.screen.blit(
				self.g.game_info_font.render('Copyleft (cl) by', 1, 
						(100,100,100)),(200,340))
			self.g.screen.blit(
				self.g.game_info_font.render('http://www.milk2cows.com', 1,
						(100,100,100)), (200,380))
			self.g.screen.blit(
				self.g.game_info_font.render('2008-4', 1, 
						(100,100,100)), (200,420))
			display.flip()

	def main_page(self):
		#title page:
		while not self.g.d.io.quit : # and not self.g.d.io.all_buttons[8]['down']:
			self.clock.tick(10)
			self.g.event_update()
			self.g.s.draw()
			
			# black the playarea_s
			self.g.s.playarea_s.blit(self.g.s.black_s, (0,0))
			
			self.g.s.playarea_s.blit(
				self.g.game_info_font.render('Dancing Block', 1, (180,0,0)), (40,150))

			# clear the menu_s.
			self.g.s.menu_s.blit(self.g.s.black_s, (0,0))
			self.g.m_m.update()
			self.g.s.playinfo_s.blit(self.g.s.menu_s, (0, 420))
			
			# buttons take one and reset it.
			if self.g.d.io.all_buttons[8]['down']:
				self.g.d.io.all_buttons[8]['down'] = 0
				return self.g.m_list[self.g.menu_choice_id].gotopage
						
#			if joystick.get_count():
#				self.g.s.playarea_s.blit(
#					self.g.game_info_font.render('PRESS [select] TO PLAY', 1, 
#						(0,128,0)), (40,500))
#				self.g.s.playarea_s.blit(
#					self.g.game_info_small_font.render('^^ USE dance-pad TO PLAY', 1, 
#						(0,0,128)), (40,550))
#			else:
#				self.g.s.playarea_s.blit(
#					self.g.game_info_font.render('PRESS [SPACE] TO PLAY', 1, 
#						(0,128,0)), (40,500))
#				self.g.s.playarea_s.blit(
#					self.g.game_info_small_font.render('^^ USE KEYBROAD TO PLAY', 1, 
#						(0,0,128)), (40,550))

			display.flip()
			
	def __check_playing_configure_state(self, t):
		if self.g.d.io.all_buttons[8]['down']:
			self.g.d.io.all_buttons[8]['down'] = 0
			self.playing_configure_state = t
					
	def game_page(self):
		self.mark_time = 72
		while self.mark_time : # and not self.g.d.io.all_buttons[9]['down'] : #21
			self.clock.tick(24)
			self.g.event_update()
			
			# draw the background.
			self.g.s.draw()

			if self.g.score > 0 and not self.playing_configure_state:
				self.g.groundblock_group.update()
				self.g.groundblock_group.draw(self.g.s.playarea_s)
				self.__check_playing_configure_state(1)
			elif self.g.score <= 0:
				self.g.s.playarea_s.blit(
					self.g.game_info_font.render('GAMEOVER', 1, (180,0,0)), (210,210))
				self.g.s.playarea_s.blit(
					self.g.game_info_small_font.render('http://www.milk2cows.com/dancingblock', 1,
				(0,0,128)), (40,570))
				self.mark_time -= 1
			elif self.playing_configure_state:
				self.g.s.playarea_s.blit(self.g.menu_background_image , (211, 201))
				self.g.p_m.update()
				self.g.s.playarea_s.blit(self.g.s.menu_s, (211, 201))
				
#				self.__check_playing_configure_state(0)
				if self.g.d.io.all_buttons[8]['down']:
					self.g.d.io.all_buttons[8]['down'] = 0
					self.playing_configure_state = 0
					if not self.g.m_list[self.g.menu_choice_id].gotopage == self.g.GAME_PAGE:
						return self.g.m_list[self.g.menu_choice_id].gotopage
			
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
		return self.g.QUIT_PAGE
	
	def quit_page(self):
		self.mark_time = 3
		while self.mark_time:
			self.clock.tick(1)
			self.mark_time -= 1
			self.g.screen.blit(self.g.s.black_s, (0,0))
			self.g.screen.blit(
				self.g.game_info_font.render('Thank You.', 1, 
						(100,100,100)),(200,340))
			self.g.screen.blit(
				self.g.game_info_font.render('for you play this game.', 1,
						(100,100,100)), (200,380))
			display.flip()
		self.mark_time = 3
		while self.mark_time:
			self.clock.tick(1)
			self.mark_time -= 1
			self.g.screen.blit(self.g.s.black_s, (0,0))
			self.g.screen.blit(
				self.g.cow_logo_image.convert_alpha(), (250,100)
				)
			self.g.screen.blit(
				self.g.game_info_font.render('bye !', 1,
						(100,100,100)), (200,340))
			display.flip()
	
	def configure_page(self):
#		print 'CP Out!!'
		while not self.g.d.io.quit :
			self.clock.tick(10)
			self.g.event_update()
			self.g.s.draw()
			
			# black the playarea_s
			self.g.s.playarea_s.blit(self.g.s.black_s, (0,0))

			# clear the menu_s.
			self.g.s.menu_s.blit(self.g.s.black_s, (0,0))
			self.g.c_m.update()
			self.g.s.playinfo_s.blit(self.g.s.menu_s, (0, 420))
			
#			self.g.s.menu_choicebar_s.blit(self.g.s.black_s, (0,0))
#			self.g.c_b_m.update()
#			self.g.s.playarea_s.blit(self.g.s.menu_choicebar_s, (0, 250))
		
			# Oh! this isn't my taste.
			if self.g.d.io.all_buttons[8]['down']:
				self.g.d.io.all_buttons[8]['down'] = 0
#				print 'mcid: %s' %self.g.menu_choice_id
				return self.g.m_list[self.g.menu_choice_id].gotopage
			
			display.flip()