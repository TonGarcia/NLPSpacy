import spacy

# nlp = spacy.load("pt_core_news_sm")
# nlp = spacy.load("en_core_web_sm")           # load model package "en_core_web_sm"
# nlp = spacy.load("/path/to/en_core_web_sm")  # load package from a directory

nlp = spacy.load("en")                       # load model with shortcut link "en"
doc = nlp("This is a sentence.")
