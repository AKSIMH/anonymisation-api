import spacy
import sys

def load_models():
    """
    load the models from disk
    and put them in a dictionary
    Returns:
        dict: loaded models
    """

    models = {
        "en_sm": spacy.load("en_core_web_sm")
    #   "fr_sm": spacy.load("models/fr"),
    }
    print("models loaded from disk")


    return models


models = load_models()