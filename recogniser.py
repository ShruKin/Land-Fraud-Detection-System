from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os

java_path = r"C:\Program Files (x86)\Java\jre1.8.0_241\bin\java.exe"
os.environ['JAVAHOME'] = java_path
english_tagger= StanfordNERTagger('stanford-ner-2018-10-16\\classifiers\\english.all.3class.distsim.crf.ser.gz','stanford-ner-2018-10-16\\stanford-ner.jar')

infile = open("sample.txt","r")
my_list = [i.split('\t')[0] for i in infile.readlines()]
print(my_list)
list2 = list()
for text in my_list:
    list2.append(word_tokenize(text))
print(list2)
op= english_tagger.tag_sents(list2)
print(op)


