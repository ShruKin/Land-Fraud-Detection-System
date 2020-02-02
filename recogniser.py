import os
java_path = r"C:\Program Files (x86)\Java\jre1.8.0_241\bin\java.exe"
os.environ['JAVAHOME'] = java_path

import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize, sent_tokenize

# gz_path = r'stanford-ner-2018-10-16\classifiers\english.all.3class.distsim.crf.ser.gz'
stanford_dir = r'stanford-ner-2018-10-16'
gz_path = stanford_dir + r'\classifiers\english.muc.7class.distsim.crf.ser.gz'
jar_path = stanford_dir + r'\stanford-ner.jar'
st = StanfordNERTagger(gz_path, jar_path)

with open(r'outfiles\infile.txt', 'r') as f:
    text = f.read()
print(text)

net_words = []
net_NER_tagged = []
net_POS_tagged = []

sentences = sent_tokenize(text)
for s in sentences:
    words = word_tokenize(s)
    net_words.append(words)

    NER_tagged = st.tag(words)
    net_NER_tagged.append(NER_tagged)

    pos_tagged = nltk.pos_tag(words)
    net_POS_tagged.append(pos_tagged)


net_words = [flat for nested_list in net_words for flat in nested_list]
net_NER_tagged = [flat for nested_list in net_NER_tagged for flat in nested_list]
net_POS_tagged = [flat for nested_list in net_POS_tagged for flat in nested_list]

# print(net_NER_tagged)
# print(net_POS_tagged)

net_classified = list(zip(net_words, [item[1] for item in net_POS_tagged], [item[1] for item in net_NER_tagged]))

print(net_classified)


with open(r'outfiles\outfile.txt', 'w') as f:
    for n in net_classified:
        f.writelines(f"{n[0]} {n[1]} {n[2]}\n")