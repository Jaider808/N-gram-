from collections import defaultdict
import re
import random
import math

def calculate_unigrams_and_bigrams(corpus):
    # Inicializar diccionarios para almacenar recuentos de unigramas y bigramas
    unigrams = defaultdict(int)
    bigrams = defaultdict(int)

    # Tokenización del corpus en palabras
    tokens = re.findall(r'\b\w+\b', corpus.lower())

    # Calcular recuentos de unigramas y bigramas
    prev_word = None
    for word in tokens:
        unigrams[word] += 1
        if prev_word is not None:
            bigrams[(prev_word, word)] += 1
        prev_word = word

    return unigrams, bigrams

def calculate_probability(word, prev_word, unigrams, bigrams):
    if prev_word is None:
        # Si no hay palabra anterior, usar unigrama
        if word in unigrams:
            return unigrams[word] / sum(unigrams.values())
        else:
            return 1 / sum(unigrams.values())  # Suavizado para palabras fuera del vocabulario
    else:
        # Si hay palabra anterior, usar bigrama
        if (prev_word, word) in bigrams and prev_word in unigrams:
            return bigrams[(prev_word, word)] / unigrams[prev_word]
        else:
            return 0  # Bigrama no presente en el corpus

def calculate_perplexity(test_corpus, unigrams, bigrams):
    # Tokenización del conjunto de prueba en palabras
    tokens = re.findall(r'\b\w+\b', test_corpus.lower())
    num_tokens = len(tokens)
    log_likelihood = 0

    prev_word = None
    for word in tokens:
        # Calcular la probabilidad logarítmica de cada palabra en el conjunto de prueba
        log_prob = math.log(calculate_probability(word, prev_word, unigrams, bigrams))
        log_likelihood += log_prob
        prev_word = word

    # Calcular la perplejidad
    perplexity = math.exp(-log_likelihood / num_tokens)
    return perplexity

def main():
    # Corpus de entrenamiento
    corpus = """
    The quick brown fox jumps over the lazy dog. The dog barks loudly.
    """

    # Corpus de prueba
    test_corpus = "The quick brown fox jumps over the lazy dog. The dog barks loudly."

    # Calcular unigramas y bigramas para el corpus de entrenamiento
    unigrams, bigrams = calculate_unigrams_and_bigrams(corpus)

    # Calcular perplejidad para el conjunto de prueba
    perplexity = calculate_perplexity(test_corpus, unigrams, bigrams)
    print(f"Perplejidad del conjunto de prueba: {perplexity}")

if __name__ == "__main__":
    main()