import tkinter
import random

class GUI:
	def __init__(self):
		self.color = "#b4e075"
		self.scsize = "800x600"
		
		self.gobj = tkinter.Tk()
		self.gobj.title("Symulator rzutu szescienna kostka do gry")
		self.gobj.geometry(self.scsize)
		self.gobj.config(bg = self.color)

		self.btn = tkinter.Button(self.gobj, text = "Wykonaj rzut", command = self.throwdice, font = ("Arial", 30), bd = 5)
		self.btn.pack(side = "bottom", pady = 30)
		
		self.ressection = tkinter.Label(self.gobj, bg = self.color)
		self.ressection.config(width = 600, height = 600)
		self.ressection.pack()

	def throwdice(self):
		res = random.randint(1, 6)
		img = tkinter.PhotoImage(file = "assets/dice%d.png" % res)
		self.ressection.config(image = img)
		self.ressection.image = img
		
	def start(self):
		self.gobj.mainloop()

g = GUI()
g.start()
