import csv
import xml.etree.ElementTree as ET

row_list = []
FILL = "#dae8fc"
STROKE = "#6c8ebf"
ENTITY_SHAPE = 'rectangle'
ATTRIBUTE_SHAPE = 'ellipse'
RELATIONSHIP_SHAPE = 'rhombus'
MULTI_VALUE_SHAPE = 'doubleEllipse'
PRIMARY_KEY_SHAPE = 'ellipse;whiteSpace=wrap;html=1;align=center;fontStyle=4;'
DERIVED_SHAPE = 'ellipse;whiteSpace=wrap;html=1;align=center;dashed=1;'


def xml_input_handling():
    tree = ET.parse('res\\first_output.xml')
    root = tree.getroot()
    print(root)
    return root


def create_csv_file():
    with open('res\\er.csv', 'w+', newline='') as file:
        fieldnames = ["node", "fill", "stroke", "shape", "one", "many", "attri", "compo"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        root = xml_input_handling()
        relationship_dic = {}
        for rel in root.findall('relation'):
            relationship = rel.get('name')
            relationship_dic['node'] = relationship
            relationship_dic['shape'] = RELATIONSHIP_SHAPE
            relationship_dic['fill'] = FILL
            relationship_dic['stroke'] = STROKE
            writer.writerow(relationship_dic)
            print(relationship_dic)
        for entity in root.findall('entity'):
            entity_dic = {}
            car_one = []
            car_many = []
            entity_name = entity.get('name')
            entity_dic['node'] = entity_name
            entity_dic['shape'] = ENTITY_SHAPE
            entity_dic['fill'] = FILL
            entity_dic['stroke'] = STROKE
            print("entity", entity_name)
            for rel in root.findall('relation'):
                relationship = rel.get('name')
                for member1 in rel.findall('member1'):
                    member1_name = member1.get('name')
                    cardinality = member1.get('cardinality')
                    if member1_name == entity_name:
                        if cardinality == 'one':
                            car_one.append(relationship)
                        elif cardinality == 'many':
                            car_many.append(relationship)
                for member2 in rel.findall('member2'):
                    member2_name = member2.get('name')
                    cardinality = member2.get('cardinality')
                    if member2_name == entity_name:
                        if cardinality == 'one':
                            car_one.append(relationship)
                        elif cardinality == 'many':
                            car_many.append(relationship)
            entity_dic['one'] = ','.join(car_one)
            entity_dic['many'] = ','.join(car_many)
            writer.writerow(entity_dic)
            print(entity_dic)

        for entity in root.findall('entity'):
            entity_name = entity.get('name')
            comp = ''
            for attribute in entity.findall('attribute'):
                attribute_dic = {}
                type = attribute.get('type')
                value = attribute.get('value')
                attribute_name = attribute.get('name')
                attribute_dic['node'] = entity_name + "_" + attribute_name

                attribute_dic['fill'] = FILL
                attribute_dic['stroke'] = STROKE
                if value == 'primary_key':
                    attribute_dic['shape'] = PRIMARY_KEY_SHAPE
                elif type == 'multi-valued':
                    attribute_dic['shape'] = MULTI_VALUE_SHAPE
                elif type == 'derived':
                    attribute_dic['shape'] = DERIVED_SHAPE
                else:
                    attribute_dic['shape'] = ATTRIBUTE_SHAPE
                if type == 'composite_parent':
                    comp = entity_name + '_' + attribute_name

                if type == 'composite_child':
                    attribute_dic['compo'] = comp
                else:
                    attribute_dic['attri'] = entity_name

                writer.writerow(attribute_dic)
                print(attribute_dic)

def create_draw_text_file():
    create_csv_file()
    text_list = []
    with open('res\\er.csv', "r") as my_input_file:
        for line in my_input_file:
            # line = line.split(",", 2)
            text_list.append("".join(line))

    with open('res\\er.txt', "a") as my_output_file:
        for line in text_list:
            my_output_file.write("" + line)
        print('Successfully created ER file')

# create_draw_text_file()
