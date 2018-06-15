import sys
import os
import jieba
import logging
import math
import gensim
import numpy as np
from scipy.spatial import distance
from pathlib import Path

def sentence_similarity(input1, input2, model = None):
    # Word2Vec Cosine distance
    if len(input1) == 0 or len(input2) == 0:
        if len(input1) == 0:
            return len(input2)
        else:
            return len(input1)

    if model == None:
        print('No Model passed into function, run word2Vec_generation.py')
        exit()

    # Sum up word vectors in sentence, average to get sentence vector
    input1_vector = np.ndarray(100)
    for element in input1:
        input1_vector = np.add(input1_vector, model[element])
    input1_vector = np.divide(input1_vector, len(input1)).ravel()

    input2_vector = np.ndarray(100)
    for element in input2:
        input2_vector = np.add(input2_vector, model[element])
    input2_vector = np.divide(input2_vector, len(input2)).ravel()

    # Return distance
    return distance.cosine(input1_vector, input2_vector)

def levenshtein_distance(input1 = [], input2 = []):
    if len(input1) == 0 or len(input2) == 0:
        if len(input1) == 0:
            return len(input2)
        else:
            return len(input1)

    # Input1 and Input2 as already Jieba segmented sentence
    # Jieba Default Logging set to DEBUG wtf dude
    l1 = len(input1)
    l2 = len(input2)

    matrix = np.zeros([l1 + 1, l2 + 1])

    for i in range(l1 + 1):
        matrix[i][0] = i

    for i in range(l2 + 1):
        matrix[0][i] = i

    for j in range(1, l2 + 1):
        for i in range(1, l1 + 1):
            # cell above:
            cellabove = matrix[i - 1][j] + 1
            # cell left plus:
            cellleft = matrix[i][j - 1] + 1
            # Cost
            cost = 0 if input1[i - 1] == input2[j - 1] else 1
            cost += matrix[i-1][j-1]
            matrix[i][j] = min(cellabove, cellleft, cost)
    return matrix[l1][l2]

def similarity(input1, input2, alpha = 0.75, model = None):
    if model == None:
        model = load_model()
    sentence1 = jieba.lcut(input1)
    sentence2 = jieba.lcut(input2)

    levdis = 2/(math.exp(levenshtein_distance(sentence1, sentence2)/1.5 - 4) + 1) - 1
    word2vec = sentence_similarity(sentence1, sentence2, model = model)
    return alpha * word2vec + (1 - alpha) * levdis

def load_model():
    model_str_path = os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))) + '/' + 'data/Model/gensimWord2Vec.bin'
    model_path = Path(model_str_path)
    if model_path.is_file():
        print('Loading Existing Model')
        model = gensim.models.Word2Vec.load(model_str_path)
    else:
        print('No Model found, run word2Vec_generation.py')
        exit()
    return model

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Please call the function by python Levenshtein.py arg1 arg2')
    else:
        model = load_model()
        sim_value = similarity(sys.argv[1], sys.argv[2], model = model)
        print('Input1: {}, Input2: {}, simValue = {}'.format(
            sys.argv[1], sys.argv[2], sim_value))