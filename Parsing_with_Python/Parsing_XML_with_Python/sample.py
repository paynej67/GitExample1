import xml.etree.ElementTree as ET

#Get the XML file data
stream = open('sample.xml' , 'r')

#Parse the data into an Element Tree object
xml = xml.getroot()

#Get the "root" Element object from the ElementTree
root = xml.getroot()

#Iterate through each child of the root Element 
for e in root:
    #Print the stringified version of the element
    print(ET.tostring(e) )
    print("")

    #Print the 'Id' attribute of the Element object
    print(e.get("Id"))