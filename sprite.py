import turtle

class Sprite():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.shape = "square"
		self.width = width
		self.height = height
		self.tk = turtle.Turtle()
		self.tk.speed(0)
		self.tk.penup()

	def run(self):
		self.tk.shape(self.shape)
		self.tk.goto(self.x, self.y)

	def shape(self, shape):
		self.shape = shape
		self.tk.shape(self.shape)

	def penUp(self):
		self.tk.penup()

	def penDown(self):
		self.tk.pendown()

	def multiply(self, w, l):
		self.tk.shapesize(stretch_wid=w, stretch_len=l)

	def penSize(self, size):
		self.tk.pensize(size)

	def penColor(self, color):
		self.tk.pencolor(color)

	def paint(self, color):
		self.tk.color(color)