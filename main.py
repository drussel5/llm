from tokenizer import SimpleTokenizer
from vocabulary import genVocab

def main():
    vocabList = {"The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"}
    vocab = genVocab(vocabList)
    print("Vocabulary:")
    print(vocab)

    tok = SimpleTokenizer(vocab)

    # encoding example
    tokens = tok.encode("The dog lazy")
    print("Tokens:")
    print(tokens)

    # decoding example
    text = tok.decode(tokens)
    print("Text:")
    print(text)

if __name__ == "__main__":
    main()