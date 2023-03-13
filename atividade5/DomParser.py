import urllib.request
from bs4 import BeautifulSoup

with open("seeds.txt", "r") as file: 
    outputFile = open("data.html", "w", encoding="utf8")
    outputFile.write("<html> <head> <title>Atividade 5 - Mariana Santos</title> </head><body>")
    for line in file:

        page = urllib.request.urlopen(line)

        html = str(page.read().decode('utf-8'))

        soup = BeautifulSoup(html, 'lxml')


        outputFile.write("<p> Título: " + soup.title.string + "</p>")

        for img in soup.find_all('img'):
            linkImg = img.attrs.get("src")
            if linkImg.find("https") != -1:
                outputFile.write('<img src="' + linkImg + '" width="100" height="100" >')
            else:
                 outputFile.write('<img src="' + line+linkImg + '" width="100" height="100" >')
            break
    outputFile.write('</body></html>')

            
