import os
import numpy
import jieba
import re

def remove_tag(file):
    p = re.compile(r'<[^<]+>')
    lst = re.findall(p, liang_file)
    for i in lst:
        my_sum = i.count('<') + i.count('>')
        if my_sum != 2:
            print(i)
    with open('check.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lst))

    return re.sub(p, '', file)

def jieba_cut_write_file(file, dict_path, write_path):
    my_dict = jieba.load_userdict(dict_path)
    with open(write_path, 'w',encoding='utf-8') as f:
        lst = [ i for i in jieba.cut(file) ]
        f.write(' '.join(jieba.cut(file)).replace(' \n ', '\n'))

def text2sentence(file):
    lst = list()
    for sent in file.split('\n'):
        if sent == '\n':
            continue
        if '。' in sent:
            sent_lst = sent.split('。')
            [ lst.append(k+'。'.replace('　','')) for k in sent_lst if k != '']
        else:
            lst.append(sent)
    dialog_parttern = re.compile(r'「[^」]+」')
    file = '\n'.join([i.lstrip() for i in lst])
    file = file.replace('\n\n', '\n').replace('\n」','」\n').replace('\n)',')\n')
    for i in re.findall(dialog_parttern, file):
        if '\n' in i:
            new_sentence = i.replace('\n', '')
            file = file.replace(i, new_sentence)
    return file


nnlm_data_folder = os.listdir(os.getcwd() + '\\nnlm_data')

input_sample = nnlm_data_folder[0]
# input sample contains 6833 sentences
f  = open('./nnlm_data/{}'.format(input_sample),'r', encoding='utf-8').read()
print(f.count('\n'))

liang_file = open('./nnlm_data/{}'.format(nnlm_data_folder[1]), encoding='utf-8').read()
liang_sentence = text2sentence(liang_file)
liang_remove = remove_tag(liang_sentence)
#print(liang_remove)
jieba_cut_write_file(liang_remove, 'j.txt', 'liang.txt')


ming_gaoseng_file = open('./nnlm_data/{}'.format(nnlm_data_folder[2]), encoding='utf-8').read()
ming_gaoseng_sentence = text2sentence(ming_gaoseng_file)
ming_gaoseng_file_remove = remove_tag(ming_gaoseng_sentence)
#print(ming_gaoseng_file_remove)
jieba_cut_write_file(ming_gaoseng_file_remove, 'j.txt','ming.txt')


song_gaoseng_file = open('./nnlm_data/{}'.format(nnlm_data_folder[4]), encoding='utf-8').read()
song_gaoseng_sentence = text2sentence(song_gaoseng_file)
song_gaoseng_file_remove = remove_tag(song_gaoseng_sentence)
jieba_cut_write_file(ming_gaoseng_file_remove, 'j.txt','song.txt')
