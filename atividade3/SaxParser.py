import xml.sax
import time
init = time.time()

class Listener(xml.sax.ContentHandler):
  def __init__(self):
    self.currentData = ""
    self.clientId = ""
    self.nodeLat = ""
    self.nodeLon = ""
    self.nodeName = ""
    self.nodeType = ""
    self.selected = False

  def startElement(self, tag, attributes):    
    self.currentData = ""
    if tag == "node":  
      self.selected = False
      self.nodeLat = attributes.get("lat")  
      self.nodeLon = attributes.get("lon")  

    if tag == "tag":
      if attributes.get("k")=="amenity":
        self.nodeType = attributes.get("v") 
        self.selected = True
      if attributes.get("k")=="name":
        self.nodeName = attributes.get("v") 

  def endElement(self, tag):    
    if tag == "node" and self.selected == True:	
      print("Tipo:", self.nodeType) 
      print("Nome:", self.nodeName) 
      print("Latitude:", self.nodeLat) 
      print("Longitude:", self.nodeLon) 
      print("\n")

  def characters(self, content):	
    self.currentData += content

parser =  xml.sax.make_parser()

Handler = Listener()
parser.setContentHandler(Handler)

print("Starting SAX Parser...")
parser.parse("map.osm")
end = time.time()
print("tempo de execução: ", end - init)