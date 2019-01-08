# Utilizando a biblioteca de regressão linear do scikit learn para prever a expectativa de vida a partir do
# índice de massa corporal: IMC.

# imports
import pandas as pd
from sklearn.linear_model import LinearRegression

bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')
print(bmi_life_data.shape)
print(bmi_life_data.head())

