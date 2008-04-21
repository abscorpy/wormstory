from gobj import gobj
from scene import scene
from jioe import jioe
from spider import spider
from pygame import *
from game_debug import game_debug

if __name__ == "__main__":
	g = gobj()
	gdebug = game_debug(g)
	s = scene(g)
	s.draw()
	display.flip()
	spider = spider(g, (100,300))
	g.spider_group.add(spider)

	while not g.j.quit and not (9 in g.j.down) and not (21 in g.j.down):
		g.event_update()
		s.draw()
		g.spider_group.draw(g.screen)
#		gdebug.debug_jioe()
		display.flip()


