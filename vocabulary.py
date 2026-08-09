def genVocab(strings):
    vocab = {}
    i = 0
    # add new words to the vocabulary
    for str in strings:
        #vocab.setdefault(str, abs(hash(str)))
        vocab.setdefault(str, i)
        i += 1

    return vocab
