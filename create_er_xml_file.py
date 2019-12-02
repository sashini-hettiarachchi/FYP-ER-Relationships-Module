import json
import xmltodict
from find_cardinality_2 import relation
import glob
from xml.etree import ElementTree

table = []
folder = "res"


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
        with open("first_output.xml", "w+", encoding="utf-8") as h:
            h.write(config)


def create_input_xml_file():
    # print(relation)
    run(folder)
    output_dic = {'er': {'relation': relation}}

    with open('res\\relation.json', 'w+') as json_file:
        json.dump(output_dic, json_file, indent=4, sort_keys=True)

    output_xml = xmltodict.unparse(output_dic, pretty=True)

    with open('res\\relation.xml', 'w+') as xml_file:
        xml_file.write(output_xml)



