from collections import defaultdict

def calculate_unigrams_and_bigrams(corpus):
    # Inicializar diccionarios para almacenar recuentos de unigramas y bigramas
    unigrams = defaultdict(int)
    bigrams = defaultdict(int)

    # Tokenización del corpus en palabras
    tokens = corpus.split()

    # Calcular recuentos de unigramas y bigramas
    prev_word = None
    for word in tokens:
        unigrams[word] += 1
        if prev_word is not None:
            bigrams[(prev_word, word)] += 1
        prev_word = word

    return unigrams, bigrams

def main():
    # Corpus de texto
    corpus = "<s> I am Sam </s> <s> Sam I am </s> <s> I am Sam </s> <s> I do not like green eggs and Sam </s>"

    # Calcular unigramas y bigramas
    unigrams, bigrams = calculate_unigrams_and_bigrams(corpus)

    # Imprimir recuentos de unigramas
    print("Unigrams:")
    for word, count in unigrams.items():
        print(f"{word}: {count}")

    # Imprimir recuentos de bigramas
    print("\nBigrams:")
    for bigram, count in bigrams.items():
        print(f"{bigram[0]} {bigram[1]}: {count}")

if __name__ == "__main__":
    main()