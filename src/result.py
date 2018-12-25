import numpy as np

voc_file = np.load('./data/vocab.zh.txt')


#print(voc_file.index('阿根廷'))


f = np.load('nnlm_word_embeddings.zh.npy')

a = np.zeros(100).reshape(5,20)
b = np.random.uniform(0,1,(3, 50))

np.savetxt('array.csv', b, fmt='%.1f', delimiter=',')


# for j in f:
# 	print(j)


