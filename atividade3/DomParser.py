from xml.dom.minidom import parse
import time
init = time.time()
BancoDocument = parse('map.osm')

print("Starting DOM Parser...")
for c in BancoDocument.getElementsByTagName("node"):	
	#if c.getAttribute("id") == "2517948726":
		exist = False
		for tag in c.getElementsByTagName("tag"):
			if tag.getAttribute("k") == "amenity":
				local = c.getElementsByTagName("tag")
				exist = True
		if exist:
			for tag in local:
				if tag.getAttribute("k") == "amenity":	
					print("Tipo: ", tag.getAttribute("v"))
				if tag.getAttribute("k") == "name":
					print("Nome: ", tag.getAttribute("v"))
			print("longitude: ", c.getAttribute("lon"))
			print("latitude: ", c.getAttribute("lat"))
			print("\n")


end = time.time()
print("tempo de execução: ", end - init)