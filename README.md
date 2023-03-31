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
 Step 1. Get the root node.
```python
root = tree.root
print(root.tag) # Prints "root"
```
 Step 2. Get the child nodes.
```python
children = root.children
print(children[0].tag) # Prints "child"
print(children[1].tag) # Prints "child"
```
 Step 3. Get the grandchild nodes.
```python
grandchildren = children[0].children
print(grandchildren[0].tag) # Prints "grandchild"
```
 Step 4. Get the data from the grandchild nodes.
```python
print(grandchildren[0].data) # Prints "Some text"
```
# How to access the data in the tree using a path?
 Step 1. Provide the path to the data.
```python
path = "root.child.grandchild"
```
 Step 2. Get the data from the tree.
```python
data = tree.get(path)
print(data) # Prints "Some text"
```
# How to access the data in the tree using a path and an index?
 Step 1. Provide the path to the data.
```python
path = "root.child.grandchild"
```
 Step 2. Provide the index of the data.
```python
index = 1
```
 Step 3. Get the data from the tree.
```python
data = tree.get(path, index)
print(data) # Prints "Some more text"
```

