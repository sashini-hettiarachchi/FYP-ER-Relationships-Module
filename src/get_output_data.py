from utils import file_manipulation

relationship_dic_list = []


def get_relationship_list():
    global member1_name, member2_name, member1_cardinality, member1_primary_key, member2_cardinality, member2_primary_key

    root = file_manipulation.get_root_of_er_xml()
    for rel in root.findall('relation'):
        for member1 in rel.findall('member1'):
            member1_name = member1.get('name')
            member1_primary_key = member1.get('primary_key')
            member1_cardinality = member1.get('cardinality')

        for member2 in rel.findall('member2'):
            member2_name = member2.get('name')
            member2_primary_key = member2.get('primary_key')
            member2_cardinality = member2.get('cardinality')

        relationship_dic = {'relationship': rel.get('name'), 'cardinality': rel.get('type'),
                            'degree': rel.get('degree'), 'entity1': member1_name,
                            'entity1_cardinality': member1_cardinality, 'entity1_primary_key': member1_primary_key,
                            'entity2': member2_name, 'entity2_cardinality': member2_cardinality,
                            'entity2_primary_key': member2_primary_key}
        for member3 in rel.findall('member3'):
            member3_name = member3.get('name')
            relationship_dic['entity3'] = member3_name

        relationship_dic_list.append(relationship_dic)

    print(relationship_dic_list)
    return relationship_dic_list

# get_relationship_list()
