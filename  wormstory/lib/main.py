from gobj import gobj
from scene import scene
from jioe import jioe
from spider import spider
from pygame import *
from game_debug import game_debug

if __name__ == "__main__":
	g = gobj()
#	gdebug = game_debug(g)
	s = scene(g)
	s.draw()
	display.flip()
#	spider = spider(g, (100,300))
#	g.spider_group.add(spider)

	while not g.j.quit and not g.j.all_buttons[9]['down'] and not g.j.all_buttons[21]['down']:
		g.event_update()
		g.slave_spider.update()
#		g.spider_group.update()
		s.draw()
		g.screen.blit(g.slave_spider.image.convert_alpha(), 
			(g.slave_spider.rect.left, g.slave_spider.rect.top))

		g.debug.debug_pressed_time()
		
#		print 'top: %s' %spider.rect.top
#		print 'left: %s' %spider.rect.left
#		g.spider_group.draw(g.screen)
		g.debug.debug_jioe()
		display.flip()


