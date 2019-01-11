# Utilizando a biblioteca de regressão linear do scikit learn para prever a expectativa de vida a partir do
# índice de massa corporal: IMC.

# imports
import pandas as pd
from sklearn.linear_model import LinearRegression

# importando dados para alimentar o modelo
bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')

# criando um modelo
bmi_life_model = LinearRegression()
bmi_life_model.fit(bmi_life_data[['BMI']], bmi_life_data[['Life expectancy']])

# fazendo previsões
laos_life_exp = bmi_life_model.predict([21.07931])
print(laos_life_exp)
