import pandas
import json
# reference guide    api   docs documentation    -  bibliotheek
	       # parameter
def uitvoeren(getal, tweede):
	print("letsgo", getal)
	print(getal + tweede)
	return "maandag"
	# returntype
print("doen")
uitvoeren(5, 35) # argument
uitvoeren(17, 66)
uitkomst = uitvoeren(12, 55)
print(uitkomst)
print( uitvoeren(4,6) )
print("go")

document = pandas.read_csv("pokedex.csv", sep=";")
print(document)
zoekterm = input("wat is je favoriete pokemon")
for pok in document["TYPE"]:
	json.loads(pok)