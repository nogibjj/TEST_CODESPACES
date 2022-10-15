import nltk
import numpy as np
from viterbi import viterbi


def getWordTag(_corpus):
    """
    > It takes a corpus and returns a list of unique words and a list of unique tags

    :param _corpus: The corpus of sentences
    """
    word_map = []
    tag_map = []
    # get all the unique words and tags
    for sentence in _corpus:
        for WordTag in sentence:
            word_map.append(WordTag[0])
            tag_map.append(WordTag[1])
            pass
        pass

    word_map = sorted(set(word_map))
    tag_map = sorted(set(tag_map))
    word_map.append("OOV")

    return word_map, tag_map


def genMatrix(_corpus, wordMap, tagMap):
    """
    The function takes in a corpus, a wordMap, and a tagMap. It then generates a state matrix, an
    observation matrix, and an initial state distribution

    :param _corpus: the corpus of the training data
    :param wordMap: a list of unique words in the corpus
    :param tagMap: a list of all the tags in the corpus
    :return: matState: the transition matrix
        matObs: the observation matrix
        initState: the initial state distribution
    """
    matState = np.zeros((len(tagMap), len(tagMap)))
    matObs = np.zeros((len(tagMap), len(wordMap)))
    initState = np.zeros(len(tagMap))

    for sentence in _corpus:
        for tWordTag_first, tWordTag_second in zip(sentence[:-1], sentence[1:]):

            matState[
                tagMap.index(tWordTag_first[1]),  # row
                tagMap.index(tWordTag_second[1]),  # col
            ] += 1

        for tWordtag in sentence:
            matObs[
                tagMap.index(tWordtag[1]),  # row
                wordMap.index(tWordtag[0]),  # col
            ] += 1
        initState[tagMap.index(sentence[0][1])] += 1

    # smoothing
    matState += 1
    matObs += 1
    initState += 1

    # normalize matrix
    matState = matState / np.sum(matState, axis=1, keepdims=True)
    matObs = matObs / np.sum(matObs, axis=1, keepdims=True)
    initState = initState / np.sum(initState, axis=0, keepdims=True)

    return matState, matObs, initState


def predict(new_sentences, mat_state, mat_obs, init_state, wordMap, tagMap):
    """
    It takes in a list of sentences, the transition matrix, the observation matrix, the initial state,
    the word map, and the tag map

    :param new_sentences: list of sentences to be tagged
    :param mat_state: transition matrix
    :param mat_obs: The observation matrix
    :param init_state: The initial state probabilities
    :param wordMap: a dictionary mapping words to indices
    :param tagMap: A dictionary mapping each tag to a unique integer
    :return: the viterbi_outs which is a list of lists. Each list contains the predicted tags for the
    corresponding sentence.
    """
    total_right, total_len = 0, 0
    viterbi_outs = [None] * len(new_sentences)
    correct_solns = [None] * len(new_sentences)
    print(f'{"INPUT":>25}', f'{"ANSWER":>25}', f'{"INFERENCE":>25}', f'{"CORRECT"}')

    for i, sentence in enumerate(new_sentences):
        obs = [
            wordMap.index(tWordtag[0]) if tWordtag[0] in wordMap else (len(wordMap) - 1)
            for tWordtag in sentence
        ]
        viterbi_outs[i], prob = viterbi(obs, init_state, mat_state, mat_obs)
        viterbi_outs[i] = [tagMap[j] for j in viterbi_outs[i]]
        correct_solns[i] = [tWordtag[1] for tWordtag in sentence]
        total_right += evaluation(
            [i[0] for i in sentence], correct_solns[i], viterbi_outs[i]
        )
        total_len += len(sentence)
        pass

    print("Overall Accuracy: " + str(round(100 * total_right / total_len, 2)) + "%")
    return viterbi_outs

def evaluation(sentence, correct, ours):
    """
    It takes in a sentence, the correct solution, and the predicted solution. It then prints the
    results and returns the number of correct predictions

    :param sentence: the sentence
    :param correct: the correct solution
    :param ours: the predicted solution
    :return: the number of correct predictions
    """
    right = 0
    for word, correct_tag, our_tag in zip(sentence, correct, ours):
        print(f'{word:>25}', f'{correct_tag:>25}', f'{our_tag:>25}', f'{correct_tag == our_tag}')
        if correct_tag == our_tag:
            right += 1
    return right


if __name__ == "__main__":
    nltk.download("brown")
    nltk.download("universal_tagset")
    corpus = nltk.corpus.brown.tagged_sents(tagset="universal")[:10000]
    wordMap, tagMap = getWordTag(corpus)
    mat_state, mat_obs, init_state = genMatrix(corpus, wordMap, tagMap)
    corpus_test = nltk.corpus.brown.tagged_sents(tagset="universal")[10150:10153]
    predictions = predict(corpus_test, mat_state, mat_obs, init_state, wordMap, tagMap)
