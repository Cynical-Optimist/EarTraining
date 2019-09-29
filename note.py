from Note_list import note_dict_list
from graphics import *
import pygame.midi
import time

class Note:
	def __init__(self, midi_num, ansi, height, is_sharp):
		self.midi_num = midi_num
		self.ansi     = ansi
		self.height   = height
		self.is_sharp = is_sharp
	def __repr__(self):
		return self.ansi
	def play(self, output_player, duration=1, volume=64):
		output_player.note_on(self.midi_num, volume)
		time.sleep(duration)
		output_player.note_off(self.midi_num, volume)	


note_object_list = []
for note_dict in note_dict_list:
	note_object_list.append(Note(
		note_dict["Midi Number"], 
		note_dict["ANSI Note"  ], 
		note_dict["Height"     ], 
		note_dict["Is Sharp"   ]
	))

class Stave:
	def __init__(self, note_and_duration_list, x, y, graph_window):
		self.note_and_duration_list = note_and_duration_list
		self.graph_window = graph_window
		self.x            = x
		self.y            = y
		self.max_x        = x + 400
		self.max_y        = y + 70
		self.line_list    = []
		self.circle_list  = []
		self.outline_box  = Rectangle(Point(x-5, y-5), Point(self.max_x+5,self.max_y+5))
		self.outline_box.setOutline("yellow")
		self.outline_box.width = 40
		
		for i in range(1,6):
			self.line_list.append(
				Line(Point(self.x,self.y+i*12), Point(self.x+400, self.y+i*12))
			)
		
		
	def __repr__(self):
		return_text  = "Stave: ["
		for n_d in self.note_and_duration_list:
			return_text += n_d[0].ansi + ", "
		return_text  = return_text.rstrip(", ")
		return_text += "]"
		return return_text
	def play(self, output_player):
		for n_d in self.note_and_duration_list:
			n_d[0].play(output_player, duration=n_d[1])
	def update_circles(self):
		for c in self.circle_list:
			c.undraw()
		self.circle_list = []
		x_pos = self.x
		for n_d in self.note_and_duration_list:
			x_pos += 24
			y_pos  = self.y + (n_d[0].height * 6)
			c = Circle(Point(x_pos,y_pos), 6)
			c.setFill("black")
			self.circle_list.append(c)
	def display_stave(self):
		for l in self.line_list:
			l.draw(self.graph_window)
	def display_circles(self, output_player=None, border_color = None):
		if border_color is not None:
			self.outline_box.setOutline(border_color)
			self.outline_box.draw(self.graph_window)
#			print(border_color)
		self.update_circles()
		for i in range(len(self.circle_list)):
			self.circle_list[i].draw(self.graph_window)
			if output_player is not None:
				n_d = self.note_and_duration_list[i]
				n_d[0].play(output_player, duration=n_d[1])
		self.outline_box.setOutline("yellow")
		self.outline_box.undraw()
	def is_on_loc(self, location_object):
		if ( 
			(self.x <= location_object.x and location_object.x <= self.max_x) and 
			(self.y <= location_object.y and location_object.y <= self.max_y)
		):
			return True
		return False

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		