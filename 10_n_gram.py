from collections import defaultdict
import re
import random

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

def get_most_common_items(dictionary, n=10):
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:n]

def generate_random_sentence(bigrams):
    sentence = ["<s>"]
    prev_word = "<s>"
    while True:
        # Obtener todas las palabras que siguen a prev_word en los bigramas
        next_words = [word for (word1, word), count in bigrams.items() if word1 == prev_word]
        if not next_words:
            break
        # Elegir una palabra aleatoria de las palabras siguientes
        random_word = random.choice(next_words)
        if random_word == "</s>":
            break
        sentence.append(random_word)
        prev_word = random_word
    sentence.append("</s>")
    return " ".join(sentence)

def main():
    # Corpus 1: Texto aleatorio
    corpus1 = "The quick brown fox jumps over the lazy dog. The dog barks loudly."

    # Corpus 2: Muestra de un artículo de noticias
    corpus2 = """
    Los precios del petróleo cayeron en picada hoy después de las noticias sobre la crisis de Ucrania.
    La incertidumbre política en la región ha generado preocupaciones sobre la oferta de petróleo.
    Por otro lado, los analistas predicen que la demanda mundial de petróleo seguirá siendo fuerte.
    """

    # Calcular unigramas y bigramas para ambos corpus
    unigrams1, bigrams1 = calculate_unigrams_and_bigrams(corpus1)
    unigrams2, bigrams2 = calculate_unigrams_and_bigrams(corpus2)

    # Obtener los unigramas y bigramas más comunes para ambos corpus
    common_unigrams1 = get_most_common_items(unigrams1)
    common_unigrams2 = get_most_common_items(unigrams2)
    common_bigrams1 = get_most_common_items(bigrams1)
    common_bigrams2 = get_most_common_items(bigrams2)

    # Imprimir resultados
    print("Unigramas más comunes en el Corpus 1:")
    for word, count in common_unigrams1:
        print(f"{word}: {count}")

    print("\nUnigramas más comunes en el Corpus 2:")
    for word, count in common_unigrams2:
        print(f"{word}: {count}")

    print("\nBigramas más comunes en el Corpus 1:")
    for bigram, count in common_bigrams1:
        print(f"{bigram[0]} {bigram[1]}: {count}")

    print("\nBigramas más comunes en el Corpus 2:")
    for bigram, count in common_bigrams2:
        print(f"{bigram[0]} {bigram[1]}: {count}")

    # Generar oraciones aleatorias
    print("\nOración aleatoria del Corpus 1:")
    print(generate_random_sentence(bigrams1))

    print("\nOración aleatoria del Corpus 2:")
    print(generate_random_sentence(bigrams2))

if __name__ == "__main__":
    main()