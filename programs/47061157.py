from lxml import etree

attribute = "state"
attribute_value = "NJ"
root = []
root.append(etree.Element("Entry1", attribute = attribute_value))
print(root)