from gobj import gobj
from scene import scene
from jioe import jioe
from pygame import *

if __name__ == "__main__":
	je = jioe()
	g = gobj()
	s = scene(g)
	s.draw()
	display.flip()
	joystick.Joystick(0).init()
	my_font = font.Font(None, 36)
	while not je.quit and not (9 in je.down) and not (21 in je.down):
		events = event.get()
		je.update(events)
		s.draw()

		y = 140
		for j in je.down:
			g.screen.blit(
				my_font.render('Press the JoyStick Button: %s' %str(j), 1, 
					(255,100,100)), (40, y))
			y = y + 20
			
		for j in je.pressed:
			g.screen.blit(
				my_font.render('Pressed Buttons: %s' %str(j), 1,
					(255,100,100)),(40, y))
			y = y + 20
		
		for j in je.axis:
			g.screen.blit(
				my_font.render('AXIS: %s, VALUE: %s' %(str(j[0]), str(j[1])), 1,
					(255,100,100)),(40, y))
			y = y + 20

		for j in je.still:
			g.screen.blit(
				my_font.render('AXIS: %s, VALUE: %s' %(str(j[0]), str(j[1])), 1,
					(255,100,100)),(40, y))
			y = y + 20

		display.flip()