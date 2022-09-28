import nltk
import numpy as np

# corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
# corpus = nltk.word_tokenize(corpus.lower())



def make_dictionary(sentence, corpus, n):
    """
    The function takes in a sentence, a corpus, and a number of words to look back on. It then creates a
    dictionary of the words that follow the sentence, and returns the most common word. If there are no
    words that follow the sentence, it will look back one less word, and so on. If it can't find any
    words that follow the sentence, it will randomly choose a word from the corpus
    
    :param sentence: a list of words
    :param corpus: the corpus you want to use
    :param n: the n-gram size
    :return: A list of words that make up a sentence.
    """
    dic = {}
    lst = []
    # start = sentence[-(n-1):]
    for i in range(0, len(corpus)):
        section = corpus[i : i + (n - 1)]
        if section == sentence[-(n - 1) :]:
            next = corpus[i + (n - 1)]
            lst.append(next)
    for item in lst:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    return dic


def backoff(original, matching, n):
    """
    If the dictionary is empty, decrease n by 1 and try again. If the dictionary is not empty, return
    the key with the highest value
    
    :param original: the original word
    :param matching: a list of words that match the original word
    :param n: the number of words to consider in the context
    :return: the most common word in the dictionary.
    """
    while n > 1:
        dictionary = make_dictionary(original, matching, n)
        if dictionary == {}:
            n -= 1
        elif dictionary != {}:
            return max(dictionary, key=dictionary.get)
    return np.random.choice(matching)


def next_word(original, matching, n):
    """
    If the dictionary has only one key, return that key. Otherwise, return the key with the highest
    value
    
    :param original: the original string
    :param matching: the list of words that match the original word
    :param n: the number of words to look at
    :return: The next word in the sequence.
    """
    dictionary = make_dictionary(original, matching, n)
    if len(dictionary) == sum(dictionary.values()):
        return next(iter(dictionary))
    else:
        return max(dictionary, key=dictionary.get)


def finish_sentence(sentence, n, corpus, deterministic=False):
    """
    It takes a sentence, a corpus, and an n-gram size, and returns a sentence that is finished with a
    period, question mark, or exclamation point
    
    :param sentence: a list of words
    :param n: the number of words to look at in the corpus
    :param corpus: a list of strings, each string is a sentence
    :param deterministic: if True, the sentence will be finished using the next_word function. If False,
    the sentence will be finished using the backoff function, defaults to False (optional)
    :return: A list of words that make up a sentence.
    """
    final_lst = sentence
    while final_lst[-1] not in "?!." and len(final_lst) < 15:
        if deterministic == True:
            final_lst.append(next_word(sentence, corpus, n))
        elif deterministic == False:
            final_lst.append(backoff(sentence, corpus, n))
    return final_lst
