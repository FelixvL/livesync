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



# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()