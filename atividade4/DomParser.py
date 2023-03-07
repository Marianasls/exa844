from xml.dom.minidom import parse
import time
import json

init = time.time()
BancoDocument = parse('map.osm')
print("Starting DOM Parser...")

geoJson = dict()
geoJson['type'] = "FeatureCollection"
arrayFeatures = []

for c in BancoDocument.getElementsByTagName("node"):	

	exist = False
	for tag in c.getElementsByTagName("tag"):
		if tag.getAttribute("k") == "amenity":
			local = c.getElementsByTagName("tag")
			exist = True
	if exist:
		node = dict()
		node["type"] = "Feature"
		geometry = dict()
		properties = dict()
		geometry["type"] = "Point"
		for tag in local:
			if tag.getAttribute("k") == "name":
				properties["nome"] = tag.getAttribute("v")
			if tag.getAttribute("k") == "amenity":	
				properties["tipo"] = tag.getAttribute("v")
			
		geometry["coordinates"] = [float(c.getAttribute("lon")), float(c.getAttribute("lat"))]
		node["geometry"] = geometry
		node["properties"] = properties
		arrayFeatures.append(node)

	

geoJson['features'] = arrayFeatures

jsonStr = json.dumps(geoJson, indent=4, ensure_ascii=False)
jsonObj = json.loads(jsonStr)
with open("GeoJson.json", "w") as outfile: 
    json.dump(jsonObj, outfile) 
    
end = time.time()
print("tempo de execução: ", end - init)
