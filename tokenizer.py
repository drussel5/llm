import re


class SimpleTokenizer:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s, i in vocab.items()}

    def encode(self, str):
        preprocessed = re.split(r'\s', str)
        tokens = [self.str_to_int[s] for s in preprocessed]
        return tokens

    def decode(self, tokens):
        str = " ".join([self.int_to_str[id] for id in tokens])
        return str