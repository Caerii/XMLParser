import datetime
import _elementtree as ET

class Element:
    """Represents an XML element.
    An element has a tag name and a text value. It may also
    have child elements."""
    def __init__(self, tag, text=None):
        """Create a new element with the given tag name and text."""
        self.tag = tag
        self.text = text
        self.children = []
        self.attributes = {}

    def add_attribute(self, name, value):
        """Add an attribute to the element."""
        self.attributes[name] = value

    def add_child(self, element):
        """Add a child element."""
        self.children.append(element)

    def __str__(self, indent=0):
        """Return a string representation of the element tree."""
        s = " " * indent + self.tag
        if self.text:
            s += " " + self.text
        s += "  " + str(len(self.children)) + " children"
        for child in self.children:
            s += " " + child.__str__(indent+2)
        return s
    
    def __repr__(self):
        """Return a string representation of the element tree."""
        return self.__str__()
    
    def __eq__(self, other):
        """Return True if the element tree is equal to the other tree."""
        if self.tag != other.tag:
            return False
        if self.text != other.text:
            return False
        if len(self.children) != len(other.children):
            return False
        for i in range(len(self.children)):
            if self.children[i] != other.children[i]:
                return False
        return True
    
    def __ne__(self, other):
        """Return True if the element tree is not equal to the other tree."""
        return not self.__eq__(other)
    
    def __hash__(self):
        """Return a hash value for the element tree."""
        return hash(self.tag) + hash(self.text) + hash(tuple(self.children))
    
    def __iter__(self):
        """Return an iterator over the element tree."""
        yield self
        for child in self.children:
            for element in child:
                yield element
                
    def find(self, tag):
        """Return the first element with the given tag name."""
        for element in self:
            if element.tag == tag:
                return element
        return None
    
    def findall(self, tag):
        """Return a list of all elements with the given tag name."""
        elements = []
        for element in self:
            if element.tag == tag:
                elements.append(element)
        return elements
    
    def findtext(self, tag):
        """Return the text of the first element with the given tag name."""
        element = self.find(tag)
        if element is not None:
            return element.text
        return None
    
    def findalltext(self, tag):
        """Return a list of the text of all elements with the given tag name."""
        elements = self.findall(tag)
        return [element.text for element in elements]
    
    def get(self, tag, default=None):
        """Return the text of the first element with the given tag name.
        If no element is found, return the default value."""
        element = self.find(tag)
        if element is not None:
            return element.text
        return default
    
    def getall(self, tag, default=None):
        """Return a list of the text of all elements with the given tag name.
        If no element is found, return the default value."""
        elements = self.findall(tag)
        if elements:
            return [element.text for element in elements]
        return default
    
    def getint(self, tag, default=None):
        """Return the text of the first element with the given tag name
        converted to an integer. If no element is found, return the
        default value."""
        element = self.find(tag)
        if element is not None:
            return int(element.text)
        return default
    
    def getallint(self, tag, default=None):
        """Return a list of the text of all elements with the given tag name
        converted to an integer. If no element is found, return the
        default value."""
        elements = self.findall(tag)
        if elements:
            return [int(element.text) for element in elements]
        return default
    
    def getfloat(self, tag, default=None):
        """Return the text of the first element with the given tag name
        converted to a float. If no element is found, return the
        default value."""
        element = self.find(tag)
        if element is not None:
            return float(element.text)
        return default
    
    def getallfloat(self, tag, default=None):
        """Return a list of the text of all elements with the given tag name
        converted to a float. If no element is found, return the
        default value."""
        elements = self.findall(tag)
        if elements:
            return [float(element.text) for element in elements]
        return default
    
    def getbool(self, tag, default=None):
        """Return the text of the first element with the given tag name
        converted to a boolean. If no element is found, return the
        default value."""
        element = self.find(tag)
        if element is not None:
            return bool(int(element.text))
        return default
    
    def getallbool(self, tag, default=None):
        """Return a list of the text of all elements with the given tag name
        converted to a boolean. If no element is found, return the
        default value."""
        elements = self.findall(tag)
        if elements:
            return [bool(int(element.text)) for element in elements]
        return default
    
    def getdate(self, tag, default=None):
        """Return the text of the first element with the given tag name
        converted to a date. If no element is found, return the
        default value."""
        element = self.find(tag)
        if element is not None:
            return datetime.datetime.strptime(element.text, "%Y-%m-%d").date()
        return default
    
    def getalldate(self, tag, default=None):
        """Return a list of the text of all elements with the given tag name
        converted to a date. If no element is found, return the
        default value."""
        elements = self.findall(tag)
        if elements:
            return [datetime.datetime.strptime(element.text, "%Y-%m-%d").date() for element in elements]
        return default
    
    def getdatetime(self, tag, default=None):
        """Return the text of the first element with the given tag name
        converted to a datetime. If no element is found, return the
        default value."""
        element = self.find(tag)
        if element is not None:
            return datetime.datetime.strptime(element.text, "%Y-%m-%d %H:%M:%S")
        return default
    
    def getalldatetime(self, tag, default=None):
        """Return a list of the text of all elements with the given tag name
        converted to a datetime. If no element is found, return the
        default value."""
        elements = self.findall(tag)
        if elements:
            return [datetime.datetime.strptime(element.text, "%Y-%m-%d %H:%M:%S") for element in elements]
        return default
    
    def gettime(self, tag, default=None):
        """Return the text of the first element with the given tag name
        converted to a time. If no element is found, return the
        default value."""
        element = self.find(tag)
        if element is not None:
            return datetime.datetime.strptime(element.text, "%H:%M:%S").time()
        return default
    
    def getalltime(self, tag, default=None):
        """Return a list of the text of all elements with the given tag name
        converted to a time. If no element is found, return the
        default value."""
        elements = self.findall(tag)
        if elements:
            return [datetime.datetime.strptime(element.text, "%H:%M:%S").time() for element in elements]
        return default
    
    def gettimedelta(self, tag, default=None):
        """Return the text of the first element with the given tag name
        converted to a timedelta. If no element is found, return the
        default value."""
        element = self.find(tag)
        if element is not None:
            return datetime.datetime.strptime(element.text, "%H:%M:%S") - datetime.datetime(1900, 1, 1)
        return default
    
    def getalltimedelta(self, tag, default=None):
        """Return a list of the text of all elements with the given tag name
        converted to a timedelta. If no element is found, return the
        default value."""
        elements = self.findall(tag)
        if elements:
            return [datetime.datetime.strptime(element.text, "%H:%M:%S") - datetime.datetime(1900, 1, 1) for element in elements]
        return default
    
    def getpath(self, path, default=None):
        """Return the text of the first element found by the given path.
        If no element is found, return the default value."""
        element = self.findpath(path)
        if element is not None:
            return element.text
        return default
    
    def getallpath(self, path, default=None):
        """Return a list of the text of all elements found by the given path."""
        elements = self.findallpath(path)
        if elements:
            return [element.text for element in elements]
        return default

class XMLParser:
    """Parses XML into an Element tree.
    The parser is a simple recursive descent parser. It is not
    intended to be a full-featured XML parser. It is intended
    to be simple and easy to understand.
    The parser is implemented as a generator. It yields a token
    for each XML element. The token is a tuple containing the
    token type and the token value. The token type is one of
    "start", "end", or "text". The token value is the tag name
    for "start" and "end" tokens and the text for "text" tokens."""
    def __init__(self):
        self._root = None
        self._current = None
        self._stack = []

    def parse(self, xml):
        """Parse the given XML string and return the root element."""
        self._root = None
        self._current = None
        self._stack = []
        for token in self._tokenize(xml):
            if token[0] == "start":
                self._start(token[1])
            elif token[0] == "end":
                self._end(token[1])
            elif token[0] == "text":
                self._text(token[1])
        return self._root

    def _tokenize(self, xml):
        """Tokenize the given XML string."""
        while xml:
            start = xml.find("<")
            if start == -1:
                yield ("text", xml)
                break
            if start > 0:
                yield ("text", xml[:start])
            xml = xml[start:]
            if xml.startswith("</"):
                end = xml.find(">")
                if end == -1:
                    raise ValueError("Invalid XML")
                yield ("end", xml[2:end])
                xml = xml[end+1:]
            else:
                end = xml.find(">")
                if end == -1:
                    raise ValueError("Invalid XML")
                yield ("start", xml[1:end])
                xml = xml[end+1:]

    def _start(self, tag):
        """Create a new element with the given tag name and
        make it the current element. If there is no current
        element, make it the root element. Otherwise, add it
        as a child of the current element."""
        if self._root is None:
            self._root = Element(tag)
            self._current = self._root
        else:
            element = Element(tag)
            self._current.add_child(element)
            self._stack.append(self._current)
            self._current = element

    def _end(self, tag):
        if self._current.tag != tag:
            raise ValueError("Invalid XML")
        if self._stack:
            self._current = self._stack.pop()
        else:
            self._current = None

    def _text(self, text):
        self._current.text = text

class stringToXML:
    """Converts a string to an XML document.
    Each line of the string is converted to a child element of the root element.
    The root element is named "root".
    The child elements are named "child"."""
    def __init__(self, string):
        self._string = string

    def toXML(self):
        """Convert the string to an XML document and return it. The XML should have brackets and indentation."""
        xml = "<root>   "
        for line in self._string.splitlines():
            xml += "    <child>" + line + "</child>"
        xml += "</root>"
        return xml
    
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





