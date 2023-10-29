from math import exp
from lib.matrix import *
from lib.nlp import bow

import json
from random import choice

##Relu activation
def RelU(M):
    n, m = len(M), len(M[0])
    Y = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if M[i][j] >= 0:
                Y[i][j] = M[i][j]
    
    return Y

##softmax function
def Softmax(x):
    prob_sum = sum([exp(x[0][i]) for i in range(len(x[0]))])
    z = [exp(x[0][i]) / prob_sum for i in range(len(x[0]))]
    return z


with open('hyper_param.json') as f:
    param = json.load(f)

w1 = param["w1"]
b1 = param["b1"]
w2 = param["w2"]
b2 = param["b2"]
w3 = param["w3"]
b3 = param["b3"]

w1 = transpose(w1)
b1 = transpose(b1)
w2 = transpose(w2)
b2 = transpose(b2)
w3 = transpose(w3)
b3 = transpose(b3)


def chat(user_input):

    X = [bow(user_input)]
    X = transpose(X)

    Y1 = RelU(addition(multiply(w1, X), b1))
    Y2 = RelU(addition(multiply(w2, Y1), b2))
    Y3 = Softmax(transpose(addition(multiply(w3, Y2), b3)))

    with open("intense.json") as data_file:
        data = json.load(data_file)

    # print(Y3)
    ypred_class = [1 if i > 0.5 else 0 for i in Y3]
    # print(ypred_class)
    tag_index = ypred_class.index(1)
    return choice(data['intents'][tag_index]['responses'])
