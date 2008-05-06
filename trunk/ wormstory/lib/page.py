# Hi, I am page.
from pygame import *

class page(object):
	def __init__(self, g):
		self.g = g
		self.clock = time.Clock()
		self.playing_configure_state = 0
		
	def _skip_handle(self):
			# handle skip.
		self.g.screen.blit(
			self.g.menu_info_font.render('[ SKIP ]', 1, (0, 150, 0)), (330, 550)
			)
		if self.g.d.io.all_buttons[8]['down']:
			self.g.d.io.all_buttons[8]['down'] = 0
			return self.g.MAIN_PAGE
		else:
			return 0

	def mark_page(self):
		self.mark_time = 30
		while self.mark_time:
			self.clock.tick(10)
			self.g.event_update()
			self.mark_time -= 1
			self.g.screen.blit(
				self.g.cow_logo_image.convert_alpha(), (250,100)
				)
			
			r = self._skip_handle()
			if r: return r

			display.flip()
		self.mark_time = 30
		while self.mark_time:	
			self.clock.tick(10)
			self.g.event_update()
			self.mark_time -= 1
			self.g.screen.blit(
				self.g.game_info_font.render('Milker\'s Solo Game', 1, 
						(100,100,100)), (200,500))
			
			r = self._skip_handle()
			if r: return r
			
			display.flip()
		self.mark_time = 30
		while self.mark_time:	
			self.clock.tick(10)
			self.g.event_update()
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
			
			r = self._skip_handle()
			if r: return r
			
			display.flip()

	def main_page(self):
		#title page:
		self.g.menu_choice_id = 0	
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

			display.flip()
								
	def game_page(self):
		menu_state = 0
		self.g.menu_choice_id = 0
		self.mark_time = 72
		while self.mark_time : # and not self.g.d.io.all_buttons[9]['down'] : #21
			self.clock.tick(24)
			self.g.event_update()
			
			# draw the background.
			self.g.s.draw()

			if self.g.score > 0 and not menu_state:
				self.g.groundblock_group.update()
				self.g.groundblock_group.draw(self.g.s.playarea_s)
				
				if self.g.d.io.all_buttons[8]['down']:
					self.g.d.io.all_buttons[8]['down'] = 0
					menu_state = 1
			elif self.g.score <= 0:
				self.g.s.playarea_s.blit(
					self.g.game_info_font.render('GAMEOVER', 1, (180,0,0)), (210,210))
				self.g.s.playarea_s.blit(
					self.g.game_info_small_font.render('http://www.milk2cows.com/dancingblock', 1,
				(0,0,128)), (40,570))
				self.mark_time -= 1
			elif menu_state:
				self.g.s.playarea_s.blit(self.g.menu_background_image , (211, 201))
				self.g.p_m.update()
				self.g.s.playarea_s.blit(self.g.s.menu_s, (211, 201))
				
#				self.__check_playing_configure_state(0)
				if self.g.d.io.all_buttons[8]['down']:
					self.g.d.io.all_buttons[8]['down'] = 0
					menu_state = 0
					if self.g.m_list[self.g.menu_choice_id].gotopage:
						gotopage = self.g.m_list[self.g.menu_choice_id].gotopage
						self.g.menu_choice_id = 0
						return gotopage
			
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
		self.mark_time = 30
		while self.mark_time:
			self.clock.tick(10)
			self.g.event_update()
			self.mark_time -= 1
			self.g.screen.blit(self.g.s.black_s, (0,0))
			self.g.screen.blit(
				self.g.game_info_font.render('Thank You.', 1, 
						(128,128,0)),(200,340))
			self.g.screen.blit(
				self.g.game_info_font.render('for you play this game.', 1,
						(128,128,0)), (200,380))
						
			r = self._skip_handle()
			if r: return r
			
			display.flip()
		self.mark_time = 30
		while self.mark_time:
			self.clock.tick(10)
			self.g.event_update()
			self.mark_time -= 1
			self.g.screen.blit(self.g.s.black_s, (0,0))
			self.g.screen.blit(
				self.g.cow_logo_image.convert_alpha(), (250,100)
				)
			self.g.screen.blit(
				self.g.game_info_font.render('bye !', 1,
						(100,100,100)), (200,340))
			
			r = self._skip_handle()
			if r: return r
			
			display.flip()
	
	def configure_page(self):
		menu_state = 0
		self.g.menu_choice_id = 0
		while not self.g.d.io.quit :
			self.clock.tick(10)
			self.g.event_update()
			self.g.s.draw()
			
			# black the playarea_s
			self.g.s.playarea_s.blit(self.g.s.black_s, (0,0))

			if not menu_state:
				self.g.s.menu_choicebar_s.blit(self.g.s.black_s, (0,0))
				self.g.c_g_m.update()
				# Now just try it.
				self.g.choicebar.set_pos((220, self.g.menu_choice_id * 30 + 60))
				self.g.choicebar.update()
				self.g.s.playarea_s.blit(self.g.s.menu_choicebar_s, (0,250))
				
				if self.g.d.io.all_buttons[8]['down']:
					self.g.d.io.all_buttons[8]['down'] = 0
					menu_state = 1
					self.g.menu_choice_id = 0
			
			else:
				# clear the menu_s.
				self.g.s.menu_s.blit(self.g.s.black_s, (0,0))
				self.g.c_m.update()
				self.g.s.playinfo_s.blit(self.g.s.menu_s, (0, 420))
				
				if self.g.d.io.all_buttons[8]['down']:
					self.g.d.io.all_buttons[8]['down'] = 0
					menu_state = 0
					
					if self.g.m_list[self.g.menu_choice_id].gotopage:
						gotopage = self.g.m_list[self.g.menu_choice_id].gotopage
						self.g.menu_choice_id = 0
						return gotopage
			
			display.flip()