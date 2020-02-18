import json
import xmltodict
from src.find_cardinality import find_cardinality
import glob
from xml.etree import ElementTree
from utils.file_manipulation import PATH


table = []
folder = PATH

def run(folder):
    files = glob.glob(folder + "/*.xml")
    first = None

    for filename in files:
        data = ElementTree.parse(filename).getroot()
        if first is None:
            first = data
        else:
            first.extend(data)
    if first is not None:
        config = ElementTree.tostring(first).decode()
        with open(PATH+"\\first_output.xml", "w+", encoding="utf-8") as h:
            h.write(config)


def create_output_xml_file():
    # print(relation)
    relation_list =  find_cardinality()
    print(relation_list)
    output_dic = {'er': {'relation': relation_list}}

    with open(PATH+'\\relation.json', 'w+') as json_file:
        json.dump(output_dic, json_file, indent=4, sort_keys=True)

    output_xml = xmltodict.unparse(output_dic, pretty=True)

    with open(PATH+'\\relation.xml', 'w+') as xml_file:
        xml_file.write(output_xml)

    run(folder)

create_output_xml_file()
