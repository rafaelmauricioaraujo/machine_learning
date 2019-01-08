# Utilizando a biblioteca de regressão linear do scikit learn para prever a expectativa de vida a partir do
# índice de massa corporal: IMC.

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_values, y_values)
