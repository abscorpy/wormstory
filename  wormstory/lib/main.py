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
#	g.spider_group.add(spider)

	while not g.j.quit and not g.j.all_buttons[9]['down'] and not g.j.all_buttons[21]['down']:
		g.event_update()
		spider.update()
#		g.spider_group.update()
		s.draw()
		g.screen.blit(spider.image.convert_alpha(), (spider.rect.left, spider.rect.top))

		draw.line(g.screen, (255, 255, 255), 
			(spider.rect.left, spider.rect.top - 1), 
			(spider.rect.left + g.j.all_buttons[18]['pressed_time'] * 5, spider.rect.top - 5), 3)

#		print 'top: %s' %spider.rect.top
#		print 'left: %s' %spider.rect.left
#		g.spider_group.draw(g.screen)
#		gdebug.debug_jioe()
		display.flip()


