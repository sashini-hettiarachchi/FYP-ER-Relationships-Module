from relationship import relationship_dic_list
# from pattern.en import pluralize, singularize,conjugate, lemma, lexeme
import nltk
import inflect

one_to_one_relationship_list = []
one_to_many_relationship_list = []
many_to_many_relationship_list = []

p = inflect.engine()

lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.PorterStemmer()

# print(relationship_dic_list)
text_file = open("data\\input1_text.txt", "r")

if text_file.mode == 'r':
    # Read the scenario and covert that text file into lowercase
    input_text_load = text_file.read()
    input_text = input_text_load.lower()
    # print(input_text)


def text_into_sentence():
    return nltk.sent_tokenize(input_text)


def sentences_into_word(sentence):
    word = nltk.word_tokenize(sentence)
    return word


def get_sentences_match_with_entities(member1, member2):
    sentence_list = text_into_sentence()
    matching_sentences_list = []
    for sentence in sentence_list:
        # print(sentence)
        word_list = sentences_into_word(sentence)
        nouns_list = get_nouns_list(word_list)
        # print(nouns_list)
        # print(word_list)
        for noun in nouns_list:
            if noun == member1:
                index_of_first_member = nouns_list.index(noun)
                new_noun_list = nouns_list[index_of_first_member + 1:]
                for second_noun in new_noun_list:
                    if second_noun == member2:
                        matching_sentences_list.append(sentence)
                        # print(matching_sentences_list)
        for noun in nouns_list:
            if noun == member2:
                index_of_first_member = nouns_list.index(noun)
                new_noun_list = nouns_list[index_of_first_member + 1:]
                for second_noun in new_noun_list:
                    if second_noun == member1:
                        matching_sentences_list.append(sentence)
                        # print(matching_sentences_list)

    return matching_sentences_list


def get_nouns_list(sentence):
    pos_tag_list = nltk.pos_tag(sentence)
    noun_list = []
    # print(pos_tag_list)
    for data in pos_tag_list:
        if data[1] == 'NN' or data[1] == 'NNS':
            noun_list.append(data[0])
    # print(noun_list)
    return noun_list


def find_one_to_one():
    for dic in relationship_dic_list:
        # print(dic)

        member1 = dic.get('member1')
        member2 = dic.get('member2')

        # print(member1, member2)

        member1_tokenize = nltk.word_tokenize(member1)
        member2_tokenize = nltk.word_tokenize(member2)

        member_1_tag = nltk.pos_tag(member1_tokenize)
        member_2_tag = nltk.pos_tag(member2_tokenize)

        # print("member1 tokenize: ", member_1_tag)
        # print("member2 tokenize: ", member_2_tag)

        # singular_member1 = singularize(member1)
        # singular_member2 = singularize(member2)

        singular_member1 = lemmatizer.lemmatize(member1)

        # print(singular_member1, singular_member2)

        sentence_list = get_sentences_match_with_entities(member1, member2)
        # print(sentence_list)

        relationship = dic.get('relationship')
        # print(relationship)

        new_relationship_list = relationship.split('_')

        # pos_tag_relationship = nltk.pos_tag(new_relationship_list)
        # print(pos_tag_relationship)

        if len(new_relationship_list) > 1:
            correct_relationship = new_relationship_list[1]

        else:
            correct_relationship = new_relationship_list[0]

        # print(correct_relationship)
        # text = nltk.word_tokenize(correct_relationship)
        # print(nltk.pos_tag(text))
        relationship_lem = lemmatizer.lemmatize(correct_relationship, pos="v")
        # relationship_stem = stemmer.stem(correct_relationship)
        # print("Relationship stem : " ,relationship_stem)
        # print("Relationship lem : ", relationship_lem)

        sentence_set = list(set(sentence_list))

        for sentence in sentence_set:
            text = nltk.word_tokenize(sentence)
            # print(sentence)
            pos_tag_list = nltk.pos_tag(text)
            # print(nltk.pos_tag(pos_tag_list))
            for word_pair in pos_tag_list:
                if word_pair[1] == 'VBZ':
                    # print("word: ", word_pair[0])
                    word_stem = lemmatizer.lemmatize(word_pair[0], pos="v")
                    # print("word_stem: ", word_stem)
                    if word_stem == relationship_lem:
                        # print("may be one to one: ", relationship_lem)

                        if member_1_tag[0][1] == 'NN' and member_2_tag[0][1] == 'NN':
                            one_to_one_relationship_list.append(
                                {'member1': member1, 'member2': member2, 'relationship': relationship})
                            # print(member1, member2, relationship_lem)
                            # print("--------------------------------------------")

                if word_pair[1] == 'VBN':
                    if new_relationship_list[0] == 'is':
                        if member_1_tag[0][1] == 'NN' and member_2_tag[0][1] == 'NN':
                            one_to_one_relationship_list.append(
                                {'member1': member1, 'member2': member2, 'relationship': relationship})
                            # print(member1, member2, relationship)
                            # print("--------------------------------------------")

    print(one_to_one_relationship_list)


def find_one_to_many():
    for dic in relationship_dic_list:
        # print(dic)

        member1 = dic.get('member1')
        member2 = dic.get('member2')


find_one_to_one()
