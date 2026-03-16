import spacy

nlp = spacy.load("en_core_web_sm")

def extract_dates(text):

    doc = nlp(text)

    dates = []

    for ent in doc.ents:
        if ent.label_ == "DATE":
            dates.append(ent.text)

    return dates