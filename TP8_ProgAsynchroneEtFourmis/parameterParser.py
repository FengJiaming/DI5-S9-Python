from xml.dom.minidom import parse
import xml.dom.minidom

# Pour extraire les paramètres dans le fichier de configuration xml
class parameterParser:
    def __init__(self, filename):
        self.filename = filename

    # Pour obtenir les paramètres des fourmis
    def parseElement(self):
        DOMTree = xml.dom.minidom.parse(self.filename)
        collection = DOMTree.documentElement
        return collection.getElementsByTagName("fourmis")

    # Pour obtenir le nombre d'itérations
    def getIteration(self):
        DOMTree = xml.dom.minidom.parse(self.filename)
        collection = DOMTree.documentElement
        if collection.hasAttribute("iteration"):
            return int(collection.getAttribute("iteration"))