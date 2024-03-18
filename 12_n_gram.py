def calculate_unigram_probability(symbol_counts, total_count):
    return symbol_counts / total_count

def calculate_joint_probability(test_set, unigram_probabilities):
    joint_probability = 1
    for symbol in test_set:
        joint_probability *= unigram_probabilities[symbol]
    return joint_probability

def calculate_perplexity(joint_probability, test_set_length):
    return pow(1 / joint_probability, 1 / test_set_length)

def main():
    # Símbolos en el conjunto de entrenamiento
    training_set = [0] * 91 + list(range(1, 10))

    # Símbolos en el conjunto de prueba
    test_set = [0, 0, 0, 0, 0, 3, 0, 0, 0, 0]

    # Conteo de símbolos en el conjunto de entrenamiento
    symbol_counts = {symbol: training_set.count(symbol) for symbol in set(training_set)}

    # Total de símbolos en el conjunto de entrenamiento
    total_count = len(training_set)

    # Calcular las probabilidades de unigrama
    unigram_probabilities = {symbol: calculate_unigram_probability(count, total_count) for symbol, count in symbol_counts.items()}

    # Calcular la probabilidad conjunta del conjunto de prueba
    joint_probability = calculate_joint_probability(test_set, unigram_probabilities)

    # Calcular la perplejidad
    perplexity = calculate_perplexity(joint_probability, len(test_set))

    print("Perplejidad del unigrama para el conjunto de prueba:", perplexity)

if __name__ == "__main__":
    main()