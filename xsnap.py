#!/usr/bin/env python
import gtk, subprocess, argparse



class XSnap():

	def __init__(self):
		self.width = gtk.gdk.screen_width()
		self.height = gtk.gdk.screen_height()
		#default
		self.pos = [0,0,0,100,100]


	def top(self):
		self.pos[4] = 50
	
	def left(self):
		self.pos[3] = 50

	def bottom(self):
		self.pos[2] = 50

	def right(self):
		self.pos[1] = 50


	def _convert_percent_to_pixels(self):
		pos = self.pos
		#x,y,w,h
		pos[0] = self.pos[0]		
		pos[1] = min(self.width,int( 0.01 * self.width * self.pos[1]))
		pos[2] = min(self.height,int( 0.01 * self.height * self.pos[2]))
		pos[3] = min(self.width-pos[1],int( 0.01 * self.width * self.pos[3]))
		pos[4] = min(self.height-pos[2],int( 0.01 * self.height * self.pos[4]))
		pos = [ str(i) for i in pos ]	
		return pos
		
	def execute(self):
		pos = self._convert_percent_to_pixels()
		subprocess.call( "wmctrl -r :ACTIVE: -e" + ",".join(pos), shell=True)

	def test(self):
		print "w: ",width
		print "h: ",height
		pos = self._convert_percent_to_pixels()
		print "CMD: ","wmctrl -r :ACTIVE: -e " + ",".join(pos)


if __name__ == "__main__":
	xs = XSnap()

	parser = argparse.ArgumentParser(description='Provides window snapping commands.')

	parser.add_argument('-l',"--left", action="store_true",
		                help='shift left')
	parser.add_argument('-r',"--right", action="store_true",
		                help='shift right')
	parser.add_argument('-t',"--top", action="store_true",
		                help='shift top')
	parser.add_argument('-b',"--bottom", action="store_true",
		                help='shift bottom')

	args = parser.parse_args()

	if args.left:
		xs.left()
	if args.right:
		xs.right()
	if args.top:
		xs.top()
	if args.bottom:
		xs.bottom()

	xs.execute()




