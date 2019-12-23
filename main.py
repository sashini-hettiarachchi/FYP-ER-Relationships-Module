from src.features import identify_relationship
from src.features import find_cardinality
from src.features import create_er_xml_file
from src.features import map_er_to_relational_schema
from src.features import draw_er


def create_er_diagram_xml_file():
    identify_relationship.entity_combined_with_scenario()
    find_cardinality.find_cardinality()
    create_er_xml_file.create_output_xml_file()


def create_relational_schema():
    map_er_to_relational_schema.build_output_xml_file()


def create_er_diagram_text_file():
    draw_er.create_draw_text_file()


def run():
    try:
        create_er_diagram_xml_file()
    except BaseException as e:
        print("Er Diagram XML file creation error", e)
        return e
    try:
        create_relational_schema()
    except BaseException as e:
        print("Relational Schema creation error", e)
        return e
    try:
        create_er_diagram_text_file()
    except BaseException as e:
        print("Er Diagram text file creation error", e)
        return e


run()
