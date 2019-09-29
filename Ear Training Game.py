import pygame.midi
import note
from graphics import *
import random

note_set = note.note_object_list

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(0)

win = GraphWin("My Music", 600, 600)
win.setCoords(0,0,600,600)
close_x1 = 510
close_x2 = 600
close_y1 =   0
close_y2 =  90

rect_1 = Rectangle(Point(close_x1,close_y1), Point(close_x2,close_y2))
rect_1.setFill("red")
rect_1.draw(win)

c_major = [note for note in note_set if (note.height >= 0 and note.height <= 12 and not note.is_sharp)]

stave_list = []
for i in range(4):
	sta = note.Stave([], 100, 60+(120*i), win)
	stave_list.append(sta)
	sta.display_stave()
stave1 = stave_list[0]

while True:
	correct_stave = random.choice(stave_list)
	for sta in stave_list:
		sta.note_and_duration_list = []
		for i in range(10):
			sta.note_and_duration_list.append(
				(random.choice(c_major), random.choice([0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 1]))
			)
		sta.display_circles()
	proceed_loc = win.getMouse()
	
	selection_loc = None
	while (selection_loc == None):
		correct_stave.play(player)
		time.sleep(3)
		selection_loc = win.checkMouse()
	
	chosen_stave = None
	for sta in stave_list:
		if sta.is_on_loc(selection_loc):
			chosen_stave = sta
	if chosen_stave is correct_stave:
		correct_stave.display_circles(player, border_color = "blue")
	else:
		correct_stave.display_circles(player, border_color = "red")
	
	
	click_loc = win.getMouse()
	if ( 
		(close_x1 <= click_loc.x and click_loc.x <= close_x2) and 
		(close_y1 <= click_loc.y and click_loc.y <= close_y2)
	):
		break





pygame.midi.quit()
print("closing")
win.close()    # Close window when done

