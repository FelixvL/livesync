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
	def rijden():
		print("ik ben aan het rijden")

auto1 = Auto()
auto2 = Auto()
auto3 = Auto()
auto4 = Auto()
auto5 = Auto()
auto6 = Auto()

auto2.kleur = "rood"
auto2.rijden()
print(auto2.kleur)
print(auto2.snelheid)

print(auto1.kleur)
