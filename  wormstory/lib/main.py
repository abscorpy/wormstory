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
	# setup 9 bigblock
	for x in range(0, 3):
		for y in range(0, 3):
			g.groundblock_group.add(bigblock(g, 
				(randint(0,255),randint(0,255),randint(0,255)), (x * 200,y * 200)))

	while not g.j.quit and not g.j.all_buttons[9]['down'] : #21
		g.event_update()
	
#		g.slave_spider.update()
#		g.spider_group.update()
		s.draw()
		
		g.groundblock_group.draw(g.screen)
		
#		g.debug.debug_jioe()
#		m.draw()
		
#		g.screen.blit(g.slave_spider.image.convert_alpha(),
#			(g.slave_spider.rect.left, g.slave_spider.rect.top))

#		g.debug.debug_pressed_time()
#		g.spider_group.draw(g.screen)
		
		display.flip()