from gobj import gobj
from scene import scene
from jioe import jioe
from spider import spider
from pygame import *
from map import map
from game_debug import game_debug
from bigblock import bigblock
from random import randint

if __name__ == "__main__":
	g = gobj()
#	gdebug = game_debug(g)
	s = scene(g)
	m = map(g)
	m.set_map_data()
	s.draw()
	display.flip()
	spider = spider(g, (100,300))
	g.spider_group.add(spider)
	# setup 8 bigblock
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

	while not g.j.quit and not g.j.all_buttons[9]['down'] : #21
		g.event_update()
		g.groundblock_group.update()
		s.draw()
		g.groundblock_group.draw(g.screen)
		g.playinfo_image.blit(
				g.sys_font.render('123456', 1,
					(255,100,100)),(10, 10))
		display.flip()