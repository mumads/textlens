import spacy
nlp = spacy.load("en_core_web_sm")

def analyze_text(text: str):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    pos = [{"text": token.text, "pos": token.pos_} for token in doc]
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {
        "tokens": tokens,
        "parts_of_speech": pos,
        "named_entities": entities
    }
