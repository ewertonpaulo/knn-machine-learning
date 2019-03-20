import pandas as pd
import csv



def dataframe(filename):
    treinamento = pd.read_csv(filename, sep=",")
    df = pd.DataFrame(treinamento)
    return df

def train_test_split(filename):
    df = dataframe(filename)
    return df

def data_to_validate(df):
    x = []
    for index, df in df.iterrows():
        x.append([df['sepallength'], df['sepalwidth'], df['petallength'], df['petalwidth']])
    return x

def validacao(filename):
    df = dataframe(filename)
    return data_to_validate(df)

def rotulos_testes(filename):
    with open(filename, 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
    return dataset
