import nltk
import re
from utils.file_manipulation import get_root_of_input_xml
from pre_process.common_nlp import stopWords, text_into_sentence, sentences_into_word, lemmatizer

filtered_sentence_list = []
relationship_identified_sentence_list = []
sentence_list_has_entities = []
binary_relationship_dic_list = []
unary_relationship_dic_list = []
new_word_list = []


def find_entities(word):
    root = get_root_of_input_xml()
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

        if len(entity_list) >= 2:
            # Remove duplicates in entity list
            duplicate_removed_entity_list = list(set(entity_list))
            find_relationship(duplicate_removed_entity_list, sentence)


def find_relationship(entity_list, sentence):
    word_list = sentences_into_word(sentence)
    pos_tag_list = nltk.pos_tag(word_list)
    entity_and_index_list = []
    if len(entity_list) == 1:
        print("Unary", entity_list)
        # print(sentence)
    else:
        for data in pos_tag_list:
            for entity in entity_list:
                if data[0] == entity:
                    index = pos_tag_list.index(data)

                    entity_and_index_list.append({'member': entity, 'index': index})

                    if len(entity_and_index_list) == 2:
                        first_index = entity_and_index_list[0].get('index')
                        second_index = entity_and_index_list[1].get('index') + 1
                        first_member = entity_and_index_list[0].get('member')
                        second_member = entity_and_index_list[1].get('member')

                        regex_1_identify_entities = r"" + re.escape(first_member) + " (of each) " + re.escape(
                            second_member)
                        regex_2_identify_entities = r"" + re.escape(second_member) + " (of each) " + re.escape(
                            first_member)

                        regex_for_verb_tags = r"VB[GDPNZ]?"

                        temp_list = pos_tag_list[first_index: second_index]
                        relationship_list = []
                        count = 0
                        for data in temp_list:

                            if re.search(regex_for_verb_tags, data[1]):
                                relationship_list.append(data[0])
                                count = count + 1

                                if count < 2:
                                    relationship_identified_sentence_list.append(sentence)

                        if relationship_list:
                            if len(relationship_list) > 1:
                                relationship = relationship_list[0] + '_' + relationship_list[1]
                            else:
                                relationship = relationship_list[0]

                            member1 = entity_and_index_list[1].get('member')
                            member2 = entity_and_index_list[0].get('member')

                            relationship_dic = {'member1': member1,
                                                'relationship': relationship,
                                                'member2': member2}
                            binary_relationship_dic_list.append(relationship_dic)

                        elif re.search(regex_1_identify_entities, sentence, re.MULTILINE | re.IGNORECASE) or re.search(
                                regex_2_identify_entities, sentence,
                                re.MULTILINE | re.IGNORECASE):

                            member1 = entity_and_index_list[1].get('member')
                            member2 = entity_and_index_list[0].get('member')

                            relationship_dic = {'member1': member1,
                                                'relationship': "related_with",
                                                'member2': member2}
                            binary_relationship_dic_list.append(relationship_dic)

        print(binary_relationship_dic_list)
        return binary_relationship_dic_list


def removing_stopwords(words):
    for w in words:
        if w not in stopWords:
            filtered_sentence_list.append(w)
            return filtered_sentence_list


def find_attributes():
    root = get_root_of_input_xml()
    for child in root:
        temp_root = child
        if temp_root.get('name') == 'driver':
            for tempChild in temp_root:
                print(tempChild.attrib.get('name'))


# entity_combined_with_scenario()
