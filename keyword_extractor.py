import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text.lower())
    keywords = set()

    for ent in doc.ents:
        keywords.add(ent.text)

    for token in doc:
        if token.pos_ == "NOUN" and len(token.text) > 4:
            keywords.add(token.text)

    return list(keywords)[:5]
