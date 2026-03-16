import spacy

nlp = spacy.load("en_core_web_sm")

stakeholders = [
"government",
"citizens",
"farmers",
"companies",
"students",
"workers"
]

def detect_stakeholders(text):

    found = []

    for s in stakeholders:
        if s in text.lower():
            found.append(s)

    return list(set(found))