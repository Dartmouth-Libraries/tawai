import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
nlp = spacy.load("en_core_web_sm")

def get_text_data(txt: str):
    numtokens_split = len(txt.split())
    doc = nlp(txt)
    tokens = [tok.text for tok in doc]
    numtokens_spacy = len(tokens)

    #remove stop words
    filtered_tokens = [tok.text for tok in doc if not tok.is_stop]
    gpelist, personlist = [], []
    for ent in doc.ents:
        if ent.label_ == "GPE":
            gpelist.append(ent.text)
        elif ent.label_ == "PERSON":
            personlist.append(ent.text)

    return(numtokens_split, numtokens_spacy, gpelist, personlist, filtered_tokens)