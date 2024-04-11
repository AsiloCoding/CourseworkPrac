from pygame import *
import os
import sys
init()
width = 800
height = 600
white = (255,255,255)
window = display.set_mode((width,height))
Nextimage = image.load(os.path.join("RightButton.webp"))
Next = transform.scale(Nextimage, (45,45))
Back = transform.rotate(transform.scale(Nextimage, (45,45)), 180)
Font = font.SysFont("comicsans",50)
Program = True

class Screen():
	def __init__(self, window):
		self.window = window
		
	def SetColour(self,colour):
		self.window.fill(colour)
		
class Button(): #based off of the example code excluding buttons that use text and highlighting the text
	def __init__(self, image, pos):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		screen.blit(self.image, self.rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): #compares the given position with the area of the button
			return True
		else:
			return False
def GSWScreen():
	while True:
		GSW = Screen(window)
		GSW.SetColour(white)
		Pos = mouse.get_pos()
		GoBack = Button(Back, (50,550))
		GoBack.update(window)
		text = Font.render("GSW screen", 1, "black")
		window.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2)) #sets text in the middle of the screen
		for e in event.get():
			if e.type == QUIT:
				quit()
				sys.exit()
			if e.type == MOUSEBUTTONDOWN:
				if GoBack.checkForInput(Pos):
					menu()
			display.update()
def NextScreen():
	while True:
		NextScreen = Screen(window)
		NextScreen.SetColour(white)
		Pos = mouse.get_pos()
		GoBack = Button(Back, (50,550))
		GoBack.update(window)
		text = Font.render("Next Screen", 1, "black")
		window.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
		for e in event.get():
			if e.type == QUIT:
				quit()
				sys.exit()
			if e.type == MOUSEBUTTONDOWN:
				if GoBack.checkForInput(Pos):
					menu()
		display.update()
def menu():
	while True:
		GSWimage = image.load(os.path.join("Goldenstate.png"))
		GSW = transform.scale(GSWimage, (120,96))
		menu = Screen(window)
		menu.SetColour(white)
		Pos = mouse.get_pos()
		icon1 = Button(GSW, (50,50))
		icon2 = Button(Next, (750,550))
		for icon in [icon1,icon2]:
			icon.update(window)
		for e in event.get():
			if e.type == QUIT:
				quit()
				sys.exit()
			if e.type == MOUSEBUTTONDOWN:
				if icon1.checkForInput(Pos):
					GSWScreen()
				if icon2.checkForInput(Pos):
					NextScreen()

		display.update()
	
menu()
