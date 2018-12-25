import numpy as np

voc_file = np.load('./data/vocab.zh.txt')


print(voc_file.index('阿根廷'))


f = np.load('nnlm_word_embeddings.zh.npy')



# for j in f:
# 	print(j)