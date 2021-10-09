import spacy
nlp=spacy.load('en_core_web_sm')
with open ("book.txt","r") as f:
    text=f.read()
    chapters=text.split("CHAPTER ")[1:]
chapter1=chapters[0]
doc=nlp(chapter1)
sentences=list(doc.sents)
print(sentences[1])