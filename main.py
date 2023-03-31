# Path: main.py
from XMLParser import XMLParser

parser = XMLParser()
xml = "<top><child>text</child></top>"
for event, data in parser.parse(xml):
    if event == "start":
        print("Start tag:", data)
    elif event == "end":
        print("End tag:", data)
    elif event == "text":
        print("Text:", data)