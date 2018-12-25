import numpy as np
from scipy import spatial

voc_file = np.load('./data/vocab.zh.txt')
#print(voc_file[:100])


f = np.load('nnlm_word_embeddings.zh.npy')
#print(len(voc_file) == len(f))

def get_similarity(word):
    word_index = voc_file.index(word)
    word_emb = f[word_index]


    result_lst = []
    for i in range(len(word_emb)):
        current_word = voc_file[i]
        current_word_emb = word_emb[i]
        # similarity = 1 - spatial.distance.cosine(word_emb, current_word_emb)
        similarity = np.linalg.norm(word_emb - current_word_emb)
        result_lst.append((current_word ,similarity))

    return sorted(result_lst, key=lambda x:x[1], reverse=False)


def show(word, range=10):
    print('\nshowing top {} words related {}: '.format(word, range))
    for i in get_similarity(word)[:range+1]:
        print('    {}, {}'.format(i[0], i[1]))




my_word = '中國'
show(my_word, 5)


my_word = '美國'
show(my_word, 5)

my_word = '合作'
show(my_word, 5)

my_word = '問題'
show(my_word, 5)


my_word = '關系'
show(my_word, 5)

