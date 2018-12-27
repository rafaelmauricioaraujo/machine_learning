import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

data = pd.read_csv('data.csv')
print(data.head())

X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

print(X)
print(y)

#regressão logística
classifier1 = LogisticRegression()

#redes neurais
classifier2 = MLPClassifier()

#árvores de decisao
classifier3 = GradientBoostingClassifier()

#SVM: máquina de vetores de suporte
classifier4 = SVC(C=1.0, kernel='poly', degree=3, gamma='auto_deprecated')

#utilizando os dados do 'data.csv' para um exemplo de regressão logística
classifier1.fit(X, y)

#utilizando os dados do 'data.csv' para um exemplo de máquina de vetores de suporte
