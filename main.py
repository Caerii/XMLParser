# Path: main.py
from XMLParser import XMLParser, stringToXML, Element

# Example XML document.
"""xml
<?xml version="1.0" encoding="UTF-8"?>

<root>
    <child>
        <grandchild>Some text</grandchild>
    </child>
    <child>
        <grandchild>Some more text</grandchild>
    </child>
</root>
"""
# How do we parse this?
# We can parse this document by creating a parser object, and then calling the parse() method on the parser object. The parse() method takes a string as an argument, and returns a tree object. The tree object contains the data from the XML document in a tree-like structure. The XML document can be considered a string, because it is a text file.

# How to access the data in the tree?

parser = XMLParser()
root = parser.parse("<root>I am the root text.<child>bruh<grandchild>I AM HIDDEN!!!</grandchild></child>soup<child><grandchild>Parse my XML you fool, I dare you.</grandchild></child></root>")
print("The tree: ",root)
print("The root tag: ",root.tag)
print("The root text: ",root.text)
print("The root children: ",root.children)
print("The root attributes: ",root.attributes)
print("The root children's tags: ",[child.tag for child in root.children])
print("The root children's text: ",[child.text for child in root.children])
print("The root children's children: ",[child.children for child in root.children])
print("The root children's attributes: ",[child.attributes for child in root.children])
print("The root children's children's tags: ",[[grandchild.tag for grandchild in child.children] for child in root.children])
print("The root children's children's text: ",[[grandchild.text for grandchild in child.children] for child in root.children])
print("The root children's children's children: ",[[grandchild.children for grandchild in child.children] for child in root.children])

# convert a string into XML
example_string = """^dreamed: i slept decently, but not for long enough; my last interview is at 13'o wish me luck!!!!
                    ^idea: basically a microformat (<https://microformats.org/>)
                    ^conversational: a way of compressing entire "conversational round subtrees" into single messages, in the way zero-knowledge proofs do
                    *[-3,-2] isn't it cool how dreams can give us cool ideas????
                    # still experimenting with the notation, trying to chose a delimiter pair that is available but not already interpreted is quite challenging when trying to write CROSS-PLATFORM PLAINTEXT (hm ) 「this is actually他和reason i共同啊“Chinese”keyboard」𝚪∞
                    *{-3,-1} although dream conversations can be hard to remember... which seems to be fine, i guess. grm has been reporting some of the funny stuff i say in my sleep. my dreams are usually quite animated, externally.
                    *{-2,-1} do u understand the format by now?
                    # ur turn to play a round :3
                """
xml = stringToXML(example_string).toXML()
print(xml)