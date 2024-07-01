import streamlit as st

def levenshtein_distance(token1, token2):
    dist = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]
    for i in range(len(token1) + 1):
        dist[i][0] = i
    for i in range(len(token2) + 1):
        dist[0][i] = i

    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if (token1[i - 1] == token2[j - 1]):
                dist[i][j] = dist[i - 1][j - 1]
            else:
                dist[i][j] = min([dist[i][j - 1], dist[i - 1]
                                 [j], dist[i - 1][j - 1]]) + 1

    return dist[len(token1)][len(token2)]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab(file_path='./data/vocab.txt')


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):

        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)

        # sorted by distance
        sorted_distences = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(sorted_distences)


if __name__ == "__main__":
    # main()
    print(levenshtein_distance("elmets", "elements"))
