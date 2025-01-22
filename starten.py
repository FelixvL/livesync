print("hij doet het")
# Procedureel Programmeren
# jaren 90    Java heel radicaal
# Object Oriented Programming

# het is succesvolle manier 
# van programeurs om de wereld
# zoals wij die waarnemen 
# om te zetten in broncode

# class    cakevorm  ovenschaal bouwtekening mal    1
# object   cakeje    lasagna     huis        uitgietsel  oneindig

# kenmerk
# lichtje lampje      synoniem
# bank                homoniem

# een mens heeft het (kenmerk) dat hij een voornaam - elk lid
# een (waarde van een kenmerk) van hem is dat hij felix heet - een lid

# class kenmerk
# object waarden van die kenmerken vast

class Auto:
	kleur = "ntb"
	snelheid = 8
	wielen = ["linkervoorwiel","linkerachterwiel","rechtervoorwiel","rechterachterwiel"]
	def __init__(_self, dekleur):
		_self.kleur = dekleur

	def rijden(_self):
		print("ik ben aan het rijden met de snelheid: ", _self.snelheid)
		print("ik rij in het: ", _self.kleur)
		print(_self.wielen[1])
	
	def versnellen(_self, extrasneller):
		_self.snelheid = _self.snelheid + extrasneller

auto1 = Auto("blauw")
auto2 = Auto("rood")
auto3 = Auto("zwart")

auto2.kleur = "rood"
auto1.rijden()
auto2.rijden()
auto3.rijden()
print(auto2.kleur)
print(auto2.snelheid)

print(auto1.kleur)
auto3.rijden()
auto3.versnellen(10)
auto3.rijden()
auto3.versnellen(35)
auto3.rijden()
auto3.versnellen(70)
auto3.rijden()



# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()