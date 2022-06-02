from hashlib import new
import xml.sax
import xml.dom.minidom
"""
    XML PROCESSING
    
    XML stands for Extensible Markup Language

    XML Parser have two modules SAX and DOM

    SAX - Simple Api for XML, DOM - Document Object Model
"""

##XML with Sax
#handler = xml.sax.ContentHandler()
#parser = xml.sax.make_parser()
#parser.setContentHandler(handler)
#parser.parse("intermediate/group.xml")

xml_path = "intermediate/group.xml"

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("--- Person ---")
            id = attrs["id"]
            print("ID: %s" % id)
    
    def endElement(self, name):
        if self.current == "name":
            print("Name: %s" % self.name)
        elif self.current == "age":
            print("Age: %s" % self.age)
        elif self.current == "weight":
            print("Weight: %s" % self.weight)
        elif self.current == "height":
            print("Height: %s" % self.height)
    
    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(xml_path)

# XML WITH DOM

domtree = xml.dom.minidom.parse(xml_path)
group = domtree.documentElement

persons = group.getElementsByTagName("person")

for person in persons:
    print("--- Person with DOM ---")
    if person.hasAttribute("id"):
        print("ID: %s" % person.getAttribute("id"))
    name = person.getElementsByTagName("name")[0]
    age = person.getElementsByTagName("age")[0]
    weight = person.getElementsByTagName("weight")[0]
    height = person.getElementsByTagName("height")[0]

# Manipulating XML Files

##change the name of the first person to new name
#persons[0].getElementsByTagName("name")[0].childNodes[0].nodeValue = "New Name"
#
##apply the changes
#domtree.writexml(open(xml_path, "w"))

# Creating a new element
newperson = domtree.createElement("person")
newperson.setAttribute("id", "6")

paul = ("Paul Smith", "45", "78", "178")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Paul Smith"))

age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("45"))

weight = domtree.createElement("weight")
name.appendChild(domtree.createTextNode("78"))

height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("178"))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)
domtree.writexml(open(xml_path, "w"))

