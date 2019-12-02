# open input text scenario
import xml.etree.ElementTree as ET

text_file = open("data\\input2_text.txt", "r")


if text_file.mode == 'r':
    # Read the scenario and covert that text file into lowercase
    input_text_load = text_file.read()
    input_text = input_text_load.lower()
    # print(input_text)


# Read input XML file
def xml_input_handling():
    tree = ET.parse("data\\input2_xml.xml")
    root = tree.getroot()
    return root
