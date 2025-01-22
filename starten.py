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
		print(wielen[1])

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
