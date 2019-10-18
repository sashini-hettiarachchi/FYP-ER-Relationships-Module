import xml.etree.ElementTree as ET
import nltk
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer

lemmatizer = nltk.WordNetLemmatizer()

filtered_sentence_list = []
relationship_identified_sentence_list = []
sentence_list_has_entities = []
binary_relationship_dic_list = []
unary_relationship_dic_list = []

# open input text scenario
text_file = open("data\\input_text.txt", "r")
stopWords = set(stopwords.words('english'))

if text_file.mode == 'r':
    # Read the scenario and covert that text file into lowercase
    input_text_load = text_file.read()
    input_text = input_text_load.lower()
    # print(input_text)

new_word_list = []


# Read input XML file
def xml_input_handling():
    tree = ET.parse("data\\input_xml.xml")
    root = tree.getroot()
    return root


def find_entities(word):
    root = xml_input_handling()
    for entity_ref in root.findall('entity'):
        entity = entity_ref.get('name')
        # print(entity)
        entity_singular = lemmatizer.lemmatize(entity)
        word_singular = lemmatizer.lemmatize(word)
        if word == entity or word == entity_singular or word_singular == entity_singular:
            return word


def entity_combined_with_scenario():
    sentences = text_into_sentence()
    for sentence in sentences:
        entity_list = []
        word_list = nltk.word_tokenize(sentence)
        # print(sentence)
        for word in word_list:
            word_new = find_entities(word)
            if word_new is not None:
                sentence_list_has_entities.append(sentence)
                entity_list.append(word_new)
        # print(entity_list)

        if len(entity_list) >= 2:
            # print(entity_list)
            new_entity_list = list(set(entity_list))
            # print("remove duplicates", entity_list)
            # print(sentence)
            find_relationship(new_entity_list, sentence)


def find_relationship(entity_list, sentence):
    word_list = sentences_into_word(sentence)
    pos_tag_list = nltk.pos_tag(word_list)
    # print(sentence)
    entity_and_index_list = []
    # if len(entity_list) == 2 or len(entity_list) == 4 or len(entity_list) == 3:
    if len(entity_list) == 1:
        print("Unary", entity_list)
        print(sentence)
    else:
        for data in pos_tag_list:
            for entity in entity_list:
                # print(data[0])
                # print(entity_list)
                if data[0] == entity:
                    # print(entity)
                    # member_name = 'member' + str(entity_list.index(entity) + 1)
                    index = pos_tag_list.index(data)
                    # entity_and_index_list.append({member_name: entity, 'index': index})
                    entity_and_index_list.append({'member': entity, 'index': index})
                    # print(entity_and_index_list)
                    # print(sentence)
                    if len(entity_and_index_list) == 2:
                        first_index = entity_and_index_list[0].get('index')
                        second_index = entity_and_index_list[1].get('index') + 1
                        first_member = entity_and_index_list[0].get('member')
                        second_member = entity_and_index_list[1].get('member')
                        regex_1 = r"" + re.escape(first_member) + " (of each) " + re.escape(second_member)
                        regex_2 = r"" + re.escape(second_member) + " (of each) " + re.escape(first_member)

                        # matches = re.finditer(regex_1, sentence, re.MULTILINE | re.IGNORECASE)
                        # if matches:
                        #     print("x")
                        # print(entity_and_index_list)
                        # print(first_index , second_index)
                        temp_list = pos_tag_list[first_index: second_index]
                        relationship_list = []
                        count = 0
                        for data in temp_list:

                            # print(data[0])
                            if data[1] == 'VBG' or data[1] == 'VBD' or data[1] == 'VB' or data[1] == 'VBP' or data[
                                1] == 'VBN' or data[1] == 'VBZ':
                                relationship_list.append(data[0])
                                count = count + 1

                                if count < 2:
                                    # print(sentence)
                                    relationship_identified_sentence_list.append(sentence)

                        if relationship_list:
                            if len(relationship_list) > 1:
                                relationship = relationship_list[0] + '_' + relationship_list[1]
                            else:
                                relationship = relationship_list[0]
                            # if entity_and_index_list[0].get('member1') == None:
                            #     member1 = entity_and_index_list[1].get('member1')
                            #     member2 = entity_and_index_list[0].get('member2')
                            # else:
                            #     member1 = entity_and_index_list[0].get('member1')
                            #     member2 = entity_and_index_list[1].get('member2')

                            member1 = entity_and_index_list[1].get('member')
                            member2 = entity_and_index_list[0].get('member')

                            relationship_dic = {'member1': member1,
                                                'relationship': relationship,
                                                'member2': member2}
                            binary_relationship_dic_list.append(relationship_dic)

                        elif re.search(regex_1, sentence, re.MULTILINE | re.IGNORECASE) or re.search(regex_1, sentence,
                                                                                                     re.MULTILINE | re.IGNORECASE):
                            # print(sentence)

                            member1 = entity_and_index_list[1].get('member')
                            member2 = entity_and_index_list[0].get('member')

                            relationship_dic = {'member1': member1,
                                                'relationship': "related_with",
                                                'member2': member2}
                            binary_relationship_dic_list.append(relationship_dic)

        # print(binary_relationship_dic_list)
        return binary_relationship_dic_list


def get_relationship_list():
    # print(relationship_dic_list)
    return binary_relationship_dic_list


def find_relationship_without_verb():
    temp1 = sentence_list_has_entities
    # z= len(temp1)
    temp2 = relationship_identified_sentence_list
    # s= len(temp2)
    # x = list(set(temp1) - set(temp2))
    # p=len(x)
    # print(z, s ,p ,x)
    temp3 = [item for item in temp1 if item not in temp2]
    print(temp3)


def removing_stopwords(words):
    for w in words:
        if w not in stopWords:
            filtered_sentence_list.append(w)
            return filtered_sentence_list


def text_into_sentence():
    nltk.sent_tokenize(input_text)
    return nltk.sent_tokenize(input_text)


def sentences_into_word(sentence):
    word = nltk.word_tokenize(sentence)
    return word

def find_attributes():
    root = xml_input_handling()
    for child in root:
        temp_root = child
        if temp_root.get('name') == 'driver':
            for tempChild in temp_root:
                print(tempChild.attrib.get('name'))


# sentences_into_word()
# text_pos_tagging()
entity_combined_with_scenario()
get_relationship_list()
# find_relationship_without_verb()
# find_attributes()
