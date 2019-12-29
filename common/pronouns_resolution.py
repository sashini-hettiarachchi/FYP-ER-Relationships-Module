import spacy
nlp = spacy.load('en_core_web_sm')
import neuralcoref

neuralcoref.add_to_pipe(nlp,greedyness=0.52)
doc = nlp("Students enroll courses. They follow some lectures. ")
print(doc._.coref_resolved)
