# Related to Lecture 12

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def marks_prediction(x_value):
    x = pd.read_csv('D:\ML Course\After_Lecture11\Linear_X_Train.csv')
    y = pd.read_csv('D:\ML Course\After_Lecture11\Linear_Y-Train.csv')

    x = x.values
    y = y.values.ravel()  # Flatten y to 1D

    model = LinearRegression()
    model.fit(x, y)
    
    x_test = np.array([[float(x_value)]])  # Ensure float and 2D
    return model.predict(x_test)[0]
