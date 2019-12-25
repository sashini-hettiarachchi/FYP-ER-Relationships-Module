# open input text scenario
import xml.etree.ElementTree as ET
import os

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

def remove_files():
    if os.path.exists("G:\\FYP-new\\src\\data\\first_output.xml"):
        os.remove("G:\\FYP-new\\src\\data\\first_output.xml")
    else:
        print('first_output.xml does not exit')

    if os.path.exists("G:\\FYP-new\\src\\data\\er.csv"):
        os.remove("G:\\FYP-new\\src\\data\\er.csv")
    else:
        print('er.csv does not exit')

    if os.path.exists("G:\\FYP-new\\src\\data\\er.txt"):
        os.remove("G:\\FYP-new\\src\\data\\er.txt")
    else:
        print('er.txt does not exit')

    if os.path.exists("G:\\FYP-new\\src\\data\\output.json"):
        os.remove("G:\\FYP-new\\src\\data\\output.json")
    else:
        print('output.json does not exit')

    if os.path.exists("G:\\FYP-new\\src\\data\\output.xml"):
        os.remove("G:\\FYP-new\\src\\data\\output.xml")
    else:
        print('output.xml does not exit')

    if os.path.exists("G:\\FYP-new\\src\\data\\relation.json"):
        os.remove("G:\\FYP-new\\src\\data\\relation.json")
    else:
        print('relation.json does not exit')

    if os.path.exists("G:\\FYP-new\\src\\data\\relation.xml"):
        os.remove("G:\\FYP-new\\src\\data\\relation.xml")
    else:
        print('relation.xml does not exit')
