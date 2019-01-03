import numpy as np
import time
import math


def load(voc_fname, word_embeddings_fname):
    """Load file name via repositories

    Args
    ----
        voc_fname: str
             Vocabulary repository
        word_embeddings_fname: str
             np array, word embeddings repository

    Returns
    -------
        voc_file: numpy.array
             An numpy array contain chinese character or words
        word_embeddings_file: numpy.array
             An numpy array contain vectors
    """
    voc_file = np.load('./data/vocab.zh.txt')
    word_embeddings_file = np.load('nnlm_word_embeddings.zh.npy')
    if len(voc_file) == len(word_embeddings_file):
        print("length are not the same!!!!")
    return voc_file, word_embeddings_file


def cos_sim_numpy(vector1, vector2):
    """Implement cosine similarity in the range between [-1, 1]

    Args
    ----
      vector1: Vector 1
      vector2: Vector 2

    Returns
    -------
      numerator / denominator : cosine similarity of two vectors


    """
    numerator = sum(vector1 * vector2)
    denominator = math.sqrt(sum(vector1**2) * sum(vector2**2))
    return numerator/denominator

def run_similar_lst(search_word):
    '''Generate a sorted word similarity list

    Args
    ----
      search_word: a wanted search word
    Returns
    -------
      lst: ['word1': '1.0' , 'word2': '0.2143902']
    '''
    word_ind = voc_file.index(search_word)
    target_vector = f[word_ind]

    lst = list()
    for v in range(len(f)):
        lst.append((voc_file[v], cos_sim_numpy(f[v], target_vector)))
    return sorted(lst, key=lambda x:x[1], reverse=True)

def show(word, topn=10):
    """Find the top-N most similar words
    """
    print('\nshowing top {} words related {}: '.format(topn, word))
    for i in run_similar_lst(word)[:topn]:
        print('    {}, {}'.format(i[0], i[1]))


def save(fname_prefix, str_obj):
    with open('{}_similar_test.txt'.format(fname_prefix), 'w', encoding='utf-8') as wf:
        wf.write(str_obj)


# Step 1 : load two files
voc_fname = './data/vocab.zh.txt'
word_embeddings_fname = 'nnlm_word_embeddings.zh.npy'

voc_file, f = load(voc_fname, word_embeddings_fname)
print(len(voc_file) == len(f))


# Step 2 : show top-N similarity
search_word = '受業'
start = time.time()

my_word = '遊方'
show(my_word, 5)


my_word = '蔬食'
show(my_word, 5)

end = time.time()
print('', end - start)


# my_word = '受業'
# show(my_word, 10)
#
# my_word = '誦經'
# show(my_word, 10)
#
# my_word = '涅槃'
# show(my_word, 10)
#
#
# my_word = '佛法'
# show(my_word, 10)

# Step 3 : save it if you need
