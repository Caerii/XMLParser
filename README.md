# XMLParser
 Simple Parser for XML documents.

# What is an XML document?
 An XML document is a text file that contains a hierarchical structure of data. The data is organized in a tree-like structure, with each node containing a tag and some data. The tag is used to identify the type of data that is contained in the node. The data can be text, numbers, or other tags. The tags can be nested to create a tree-like structure. Data is stored in the nodes, and the nodes are stored in the tree.

# What is a tag?
 A tag is a string of characters that is used to identify the type of data that is contained in a node. Tags are always enclosed in angle brackets. The opening tag is always the same as the closing tag, except that the opening tag has a forward slash before the tag name. The tag name is the name of the data type that is contained in the node. The tag name can be any string of characters, but it is recommended that the tag name be a single word. The tag name is case sensitive.

 Examples of tags are the <root> tag, the <child> tag, and the <grandchild> tag.
 Other tags are the <name> tag, the <age> tag, and the <height> tag.
 And even more tags are the <first> tag, the <middle> tag, and the <last> tag.

# What is an example of a node?
 A node is each tag and its data. A node can contain any number of tags and data.

# Why are files stored in trees?
 The etymology of tree comes from the latin word "treea", which means "to branch out". In the context of file storage, trees are used because they are a natural way to organize data. A tree is made up of branches, which are made up of smaller branches, which are made up of even smaller branches, and so on. This structure is similar to how a computer's file system is organized!

# Example XML document.
```xml
<?xml version="1.0" encoding="UTF-8"?>

<root>
    <child>
        <grandchild>Some text</grandchild>
    </child>
    <child>
        <grandchild>Some more text</grandchild>
    </child>
</root>
```
# How do we parse this?
 We can parse this document by creating a parser object, and then calling the parse() method on the parser object. The parse() method takes a string as an argument, and returns a tree object. The tree object contains the data from the XML document in a tree-like structure. The XML document can be considered a string, because it is a text file.

# Example code in Python.
```python
from xmlparser import XMLParser

parser = XMLParser()
tree = parser.parse("<root><child><grandchild>Some text</grandchild></child><child><grandchild>Some more text</grandchild></child></root>")
```
# How to access the data in the tree?

```python
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
```

# Output
The tree:  root soup  2 children   child bruh  1 children     grandchild I AM HIDDEN!!!  0 children   child  1 children     grandchild Parse my XML you fool, I dare you.  0 children
The root tag:  root
The root text:  soup
The root children:  [child bruh  1 children   grandchild I AM HIDDEN!!!  0 children, child  1 children   grandchild Parse my XML you fool, I dare you.  0 children]
The root attributes:  {}
The root children's tags:  ['child', 'child']
The root children's text:  ['bruh', None]
The root children's children:  [[grandchild I AM HIDDEN!!!  0 children], [grandchild Parse my XML you fool, I dare you.  0 children]]
The root children's attributes:  [{}, {}]
The root children's children's tags:  [['grandchild'], ['grandchild']]
The root children's children's text:  [['I AM HIDDEN!!!'], ['Parse my XML you fool, I dare you.']]
The root children's children's children:  [[[]], [[]]]
<root>       <child>^dreamed: i slept decently, but not for long enough; my last interview is at 13'o wish me luck!!!!</child>    <child>                    ^idea: basically a microformat (<https://microformats.org/>)</child>    <child>                    ^conversational: a way of compressing entire "conversational round subtrees" into single messages, in the way zero-knowledge proofs do</child>    <child>                    *[-3,-2] isn't it cool how dreams can give us cool ideas????</child>    <child>                    # still experimenting with the notation, trying to chose a delimiter pair that is available but not already interpreted is quite challenging when trying to write CROSS-PLATFORM PLAINTEXT (hm ) 「this is actually他和reason i共同啊“Chinese”keyboard」𝚪∞</child>    <child>                    *{-3,-1} although dream conversations  can be hard to remember... which seems to be fine, i guess. grm has been reporting some of the funny stuff i say in my 
sleep. my dreams are usually quite animated, externally.</child>    <child>                    *{-2,-1} do u understand the format by now?</child>    <child>                    # ur turn to play a round :3</child>    <child>                </child></root>
PS F:\Github\XMLParser>


