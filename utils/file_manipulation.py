# open input text scenario
import xml.etree.ElementTree as ET

text_file = open("G:\\FYP-new\\src\\data\\input_text.txt", "r")

if text_file.mode == 'r':
    # Read the scenario and covert that text file into lowercase
    input_text_load = text_file.read()
    input_text = input_text_load.lower()
    # print(input_text)


# Read input XML file
def get_root_of_input_xml():
    tree = ET.parse("G:\\FYP-new\\src\\data\\input_xml.xml")
    root = tree.getroot()
    return root


def get_root_of_er_xml():
    tree = ET.parse('G:\\FYP-new\\src\\data\\first_output.xml')
    root = tree.getroot()
    print(root)
    return root
