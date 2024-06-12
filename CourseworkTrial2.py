from pygame import *
import sys
screen = display.set_mode((640,480))
init()
clock = time.Clock()
font = font.SysFont(None, 40)

class FadingButton:
	def __init__(self,text):
		self.orig_surf = font.render(text, True, "black")
		self.txt_surf = self.orig_surf.copy()
		self.alpha_surf = Surface(self.txt_surf.get_size(), SRCALPHA)
		self.alpha = 0 # set to 255 for Fade out
	def FadeIn(self):
		if self.alpha < 255:
			self.alpha = min(self.alpha + 4, 255)
			self.txt_surf = self.orig_surf.copy()
			self.alpha_surf.fill((255, 255, 255, self.alpha))
			self.txt_surf.blit(self.alpha_surf, (0, 0), special_flags=BLEND_RGBA_MULT)
	def FadeOut(self):
		if self.alpha > 0:
			self.alpha = max(self.alpha - 4, 0)
			self.txt_surf = self.orig_surf.copy()
			self.alpha_surf.fill((255, 255, 255, self.alpha))
			self.txt_surf.blit(self.alpha_surf, (0, 0), special_flags=BLEND_RGBA_MULT)
	def update(self,screen):
		screen.blit(self.txt_surf, (30,60))
	

Button1 = FadingButton("Hello")
while True:
	Button1.FadeIn()
	screen.fill((255,255,255))
	Button1.update(screen)
	for e in event.get():
		if e.type == QUIT:
			quit()
			sys.exit()
	display.flip()
	clock.tick(30)
