from gobj import gobj
from scene import scene
from jioe import jioe
from pygame import *
from bigblock import bigblock
from random import randint
import data

def main():
	g = gobj()
	s = scene(g)
	s.draw()
	display.flip()
	id = 0
	joystick_button_list = [7, 2, 6, 0, 3, 5, 1, 4]
	for y in range(0, 3):
		for x in range(0, 3):
			if y == 1 and x == 1:
				pass
			else:
				g.groundblock_group.add(bigblock(g, joystick_button_list[id],
					(randint(0,255),randint(0,255),randint(0,255)), (x * 200,y * 200)))
				id += 1
	
	#title page:
	while not g.j.quit and not g.j.all_buttons[8]['down']:
		g.event_update()
		s.draw()
		black_g  = Surface((600,600))
		black_g.fill((0,0,0))
		s.playarea_s.blit(black_g, (0,0))
		s.playarea_s.blit(
			g.game_info_font.render('Dancing Block', 1, (180,0,0)), (40,150))
		s.playarea_s.blit(
			g.game_info_font.render('Milker\'s Solo Game', 1, 
					(100,100,100)), (40,200))
		s.playarea_s.blit(
			g.game_info_font.render('Copyleft (cl) by', 1, (100,100,100)), (40,240))	
		s.playarea_s.blit(
			g.game_info_font.render('http://www.milk2cows.com', 1,
					(100,100,100)), (50,280))	
		s.playarea_s.blit(
			g.game_info_font.render('2008-4', 1, 
					(100,100,100)), (40,320))
		s.playarea_s.blit(
			g.game_info_font.render('PRESS [select] TO PLAY', 1, 
				(0,128,0)), (40,500))
		s.playarea_s.blit(
			g.game_info_small_font.render('^^ USE dance-pad TO PLAY', 1, 
				(0,0,128)), (40,550))
		display.flip()

	while not g.j.quit and not g.j.all_buttons[9]['down'] : #21
		g.event_update()
		if g.score > 0:
			g.groundblock_group.update()
		else:
			s.playarea_s.blit(
				g.game_info_font.render('GAMEOVER', 1, (180,0,0)), (210,210))
		s.draw()
		g.groundblock_group.draw(s.playarea_s)
		s.playinfo_s.blit(
				g.game_info_font.render('s: %s' %g.score, 1,
					(180,0,0)),(10, 470))
		s.playinfo_s.blit(
				g.game_info_font.render('level: %s' %(g.hit_block/10), 1,
					(180,0,0)),(10, 510))
		s.playinfo_s.blit(
				g.game_info_font.render('hit: %s' %g.hit_block, 1,
					(180,0,0)),(10, 550))
		display.flip()
		
if __name__ == "__main__":
	main()