# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 16:25:19 2023

@author: 14237
"""

import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('D:/ML/HeartDisease_trained_model.sav', 'rb'))

    
input_data = (32.14,1,0,0,0,0,0,1,12,1,0,1,2,8,1,0,1)

#changing the input_data to numpyarray
input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
    print('The patient is not at risk of developing heart disease')
else:
    print('The patient is at risk of having developing disease')