#!/usr/bin/env python
from ewmh.ewmh import EWMH


class XSnap():

	def __init__( self ):
		self.e = EWMH()
		self.height_padding = 50		
		self.width_padding = 0
		
	
	def get_desktop_height( self ):
		return self.e.getDesktopGeometry()[1] - self.height_padding

	def get_desktop_width( self ):
		return self.e.getDesktopGeometry()[0] - self.width_padding

	def get_geometry( self, window ):
		h = window.get_geometry()._data["height"]
		w = window.get_geometry()._data["width"]
		x = window.get_geometry()._data["x"]
		y = window.get_geometry()._data["y"]
		return [x,y,w,h]

	def get_active_window( self ):
		return self.e.getActiveWindow()
	
	def action( self, input_key ):
		win = self.e.getActiveWindow()
		self.geometry = self.get_geometry( win )
		[x,y,w,h] = self.geometry
		
		# main logic for quarter sections

		if input_key == "up":
			if y == 0:
				if x == 0:
					fullscreen( win )
				else:
					top( win )
			elif x == 0:
				top_left( win )
			elif x == self.get_desktop_width()/2:
				top_right( win )

		elif input_key == "down":
			if y == self.get_desktop_height()/2:
				bottom( win ) # modify this later 
			elif x == 0:
				bottom_left( win )
			elif x == self.get_desktop_width()/2:
				bottom_right( win )

		elif input_key == "left":
			left( win )

		elif input_key == "right":
			right( win )


	def fullscreen( self, win ):
		w = self.get_desktop_width()
		h = self.get_desktop_height()
		x = 0
		y = 0
		self.e.setMoveResizeWindow(win, x=x,y=y,w=w,h=h)
		self.e.display.flush()


	def top( self, win ):
		w = self.get_desktop_width()
		h = self.get_desktop_height()/2
		x = 0
		y = 0
		self.e.setMoveResizeWindow(win, x=x,y=y,w=w,h=h)
		self.e.display.flush()


	def bottom( self, win ):
		w = self.get_desktop_width()
		h = self.get_desktop_height()/2
		x = 0
		y = self.get_desktop_height()/2
		self.e.setMoveResizeWindow(win, x=x,y=y,w=w,h=h)
		self.e.display.flush()


	def bottom_right( self, win ):
		w = self.get_desktop_width()/2
		h = self.get_desktop_height()/2
		x = self.get_desktop_width()/2
		y = self.get_desktop_height()/2
		self.e.setMoveResizeWindow(win, x=x,y=y,w=w,h=h)
		self.e.display.flush()


	def bottom_left( self, win ):
		w = self.get_desktop_width()/2
		h = self.get_desktop_height()/2
		x = 0
		y = self.get_desktop_height()/2
		self.e.setMoveResizeWindow(win, x=x,y=y,w=w,h=h)
		self.e.display.flush()

	
	def top_right( self, win ):
		w = self.get_desktop_width()/2
		h = self.get_desktop_height()/2
		x = self.get_desktop_width()/2
		y = 0
		self.e.setMoveResizeWindow(win, x=x,y=y,w=w,h=h)
		self.e.display.flush()
	

	def top_left( self, win ):
		w = self.get_desktop_width()/2
		h = self.get_desktop_height()/2
		x = 0
		y = 0
		self.e.setMoveResizeWindow(win, x=x,y=y,w=w,h=h)
		self.e.display.flush()


	def left( self, win ):
		w = self.get_desktop_width()/2
		h = self.get_desktop_height()
		x = 0
		y = 0
		self.e.setMoveResizeWindow(win, x=x,y=y,w=w,h=h)
		self.e.display.flush()


	def right( self, win ):
		w = self.get_desktop_width()/2
		h = self.get_desktop_height()
		x = self.get_desktop_width()/2
		y = 0
		self.e.setMoveResizeWindow(win, x=x,y=y,w=w,h=h)
		self.e.display.flush()


if __name__ == "__main__":
	xs = XSnap()

	parser = argparse.ArgumentParser(description='Provides window snapping commands.')

	parser.add_argument('-l',"--left", action="store_true",
		                help='left key')
	parser.add_argument('-r',"--right", action="store_true",
		                help='right key')
	parser.add_argument('-u',"--up", action="store_true",
		                help='up key')
	parser.add_argument('-d',"--down", action="store_true",
		                help='down key')

	args = parser.parse_args()

	if args.left:
		xs.action("left")
	if args.right:
		xs.action("right")
	if args.top:
		xs.action("up")
	if args.bottom:
		xs.action("down")

	xs.execute()







