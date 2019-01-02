import numpy as np
from scipy import spatial
from numpy import dot
from numpy.linalg import norm


def get_s(v_1, v_2):
    v1_norm = sum([i*i for i in v_1]) ** 0.5
    v2_norm = sum([i*i for i in v_2]) ** 0.5
    abs_num = abs(dot(v_1, v_2))
    return abs_num / (v1_norm * v2_norm)


def get_cosine(vec1, vec2):
    # find cosine
    cosine = np.inner(vec1, vec2) / (norm(vec1) * norm(vec2))
    return cosine


voc_file = np.load('./data/vocab.zh.txt')
#print(voc_file[:100])


f = np.load('nnlm_word_embeddings.zh.npy')
#print(len(voc_file) == len(pypac))
print(len(voc_file) == len(f))


def get_similarity(word):
    word_index = voc_file.index(word)
    word_emb = f[word_index]

    result_lst = []
    for i in range(len(word_emb)):
        current_word = voc_file[i]
        current_word_emb = word_emb[i]
        #similarity = get_cosine(word_emb, current_word_emb)
        similarity = get_cosine(word_emb, current_word_emb)
        print(similarity)
        break
        #similarity = spatial.distance.cosine(word_emb, current_word_emb)
        #similarity = np.linalg.norm(word_emb - current_word_emb)
        #result_lst.append((current_word ,similarity))

    #return sorted(result_lst, key=lambda x:x[1], reverse=False)
def show(word, range=10):
    print('\nshowing top {} words related {}: '.format(word, range))
    for i in get_similarity(word)[:range+1]:
        print('    {}, {}'.format(i[0], i[1]))

get_similarity('遊方')

# my_word = '遊方'
# show(my_word, 10)
#
# my_word = '蔬食'
# show(my_word, 10)
#
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
#
