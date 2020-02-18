from utils import file_manipulation

relationship_dic_list = []


def get_relationship_list():
    global member1_name, member2_name

    root = file_manipulation.get_root_of_er_xml()
    for rel in root.findall('relation'):
        for member1 in rel.findall('member1'):
            member1_name = member1.get('name')
        for member2 in rel.findall('member2'):
            member2_name = member2.get('name')
        relationship_dic = {'relationship': rel.get('name'), 'cardinality': rel.get('type'),'entity1':member1_name,'entity2':member2_name}
        relationship_dic_list.append(relationship_dic)

    print(relationship_dic_list)
    return relationship_dic_list


# get_relationship_list()
