from csv_handler import train_test_split
import csv_handler as cv
import knn

treinamento = 'aprendizagemdemaquina/treinamento.csv'
teste = 'aprendizagemdemaquina/teste.csv'
r = 'aprendizagemdemaquina/rotulos-teste.txt'
train = cv.train_test_split(treinamento)

train = knn.data_to_list(train)
validate = cv.validacao(teste)

predic = []
rotulos = []

for i in cv.rotulos_testes(r):
    rotulos.append(float(i[0]))

k = 2

for x in range(len(validate)):
    vizinhos = knn.get_vizinhos(train, validate[x], k)
    resultado = knn.resposta(vizinhos)
    predic.append(resultado)
    print(resultado)

print('Precisao: %f' %knn.precisao(rotulos, predic))