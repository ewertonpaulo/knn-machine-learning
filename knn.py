from operator import itemgetter
from math import sqrt
from csv_handler import train_test_split

def euclidean_distancia(text, prredc, length):
    distancia = 0
    for x in range(length):
        distancia += (text[x] - prredc[x])**2
    return sqrt(distancia)

def get_vizinhos(train, test, k):
    distancia = []
    tamanho = len(test)-1
    for x in range(len(train)):
        euc = euclidean_distancia(test, train[x], tamanho)
        distancia.append([train[x], euc])

    distancia.sort(key=itemgetter(1))
    vizinhos = []
    for x in range(k):
        vizinhos.append(distancia[x][0])
    return vizinhos

def resposta(vizinhos):
    votos = {}
    for x in range(len(vizinhos)):
        resposta = vizinhos[x][-1]
        if resposta in votos:
            votos[resposta]+=1
        else:
            votos[resposta] = 1
    votos_ordenados = sorted(votos.items(), key=itemgetter(1), reverse=True)
    return votos_ordenados[0][0]

def data_to_list(df):
    x = []
    for index, df in df.iterrows():
        x.append([df['sepallength'], df['sepalwidth'], df['petallength'], df['petalwidth'], df['label']])
    return x

def data_to_validate(df):
    x = []
    for index, df in df.iterrows():
        x.append([df['sepallength'], df['sepalwidth'], df['petallength'], df['petalwidth']])
    return x[0].split(",")

def precisao(validate, predict): 
    goal = 0
    quant = len(validate)
    for x in range(quant):
        if float(validate[x]) == predict[x]: 
            goal = goal + 1
    return (goal/float(quant)*100)