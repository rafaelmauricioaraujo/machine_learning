# Import, read, and split data
import pandas as pd
import numpy as np
# Imports
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

data = pd.read_csv('data2.csv')
X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

# Fix random seed
np.random.seed(55)

# TODO: Uncomment one of the three classifiers, and hit "Test Run"

# Logistic Regression
estimator = LogisticRegression()

# Decision Tree
# estimator = GradientBoostingClassifier()

# Support Vector Machine
# estimator = SVC(kernel='rbf', gamma=1000)
