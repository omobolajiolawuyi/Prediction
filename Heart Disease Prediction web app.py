# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:21:50 2023

@author: 14237
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('D:/ML/trained_model.sav', 'rb'))

#creating a function for prediction

def heart_disease_prediction(input_data):
    
  

    #changing the input_data to numpyarray
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The patient does not have a heart disease'
    else:
        return 'The patient has heart a disease'
    

    
    
    
def main ():
    
    
    #giving it a title
    st.title('Heart Disease Prediction based on Test Results')
    
    #getting the input data from the user
    
    age = st.text_input('Age of the patient in years')
    sex = st.text_input(' Sex of the patient: Male=1, Female=0')
    cp = st.text_input('Chest Pain type: 1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic')
    trestbps = st.text_input('Resting blood pressure (in mm Hg)')
    chol = st.text_input('Cholesterol in mg/dl fetched via BMI sensor')
    fbs = st.text_input('Fasting blood sugar > 120 mg/dl') 
    restecg = st.text_input('Resting electrocardiographic results: 0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes criteria')
    thalach = st.text_input('Maximum heart rate achieved')
    exang = st.text_input('Exercise-induced angina: Yes=1, No=0') 
    oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    slope = st.text_input('The slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)')
    ca = st.text_input('Number of major vessels (0-3)') 
    thal =st.text_input('A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)')
    
    
    #code forr Prediction
    Diagnosis = ''
    
    #creating a button for Prediction
    
    if st.button('Heart Disease Prognosis'):
        Diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
        st.write(Diagnosis)
        
        
if __name__== '__main__':
     main()   



#loading the saved model
loaded_model = pickle.load(open('D:/ML/HeartDisease_trained_model.sav', 'rb'))

    
#creating a function for prediction

def heart_disease_risk(input_data):

    #changing the input_data to numpyarray
    input_data_as_numpy_array = np.asarray(input_data)
    
    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return('The patient is not at risk of developing a heart disease')
    else:
        return('The patient is at risk of having a developing disease')
    
    
def main ():
    
    #giving it a title
    st.title('Heart Disease Risk Prediction based on Lifestyle')
    
    #getting the input data from the user
    
    BMI = st.text_input('Body Mass Index')
    Smoking = st.text_input('Have you smoked at least 100 cigarettes in your entire life? Yes=1, No=0')
    AlcoholDrinking= st.text_input('Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week (Heavy Drinker=1, Light Drinker=0)')
    Stroke= st.text_input('Ever told you had a stroke? Yes=1, No=0')
    PhysicalHealth = st.text_input('For how many days during the past 30 days was your physical health not good? (0-30 days)')
    MentalHealth= st.text_input('For how many days during the past 30 days was your mental health not good? (0-30 days)') 
    DiffWalking = st.text_input('Do you have serious difficulty walking or climbing stairs? Yes=1, No=0')
    Sex= st.text_input('Are you male or female? Male=1, Female=0' )
    AgeCategory= st.text_input('Input age category value: 18-24=1, 25-29=2, 30-34=3, 35-39=4, 40-44=5, 45-49=6, 50-54=7, 55-59=8, 60-64=9, 65-69=10, 70-74=11, 75-79=12, 80 or older=13') 
    Race= st.text_input('Input race/ethnicity value: White=1, Black=2, Asian=3, American Indian/Alaskan Native=4, Hispanic=5, Other=6')
    Diabetic= st.text_input('Ever told you had diabetes?: Yes=1, No=0, Yes (during pregnancy)=1')
    PhysicalActivity= st.text_input('Done physical activity or exercise during the past 30 days other than their regular job: Yes=1, No=0') 
    GenHealth= st.text_input('Would you say that in general your health is... Excellent=1, Very good=2, Good=3, Fair=4, Poor=5')              
    SleepTime = st.text_input('On average, how many hours of sleep do you get in a 24-hour period? (1-24)') 
    Asthma= st.text_input('Ever told you had asthma? Yes=1, No=0') 
    KidneyDisease = st.text_input('Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease? Yes=1, No=0') 
    SkinCancer= st.text_input('Ever told you had skin cancer? Yes=1, No=0') 

    
    #code for Prediction
    Risk = ''
    
    #creating a button for Risk
    
    if st.button('Heart Disease Risk'):
        Risk = heart_disease_risk([BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory, Race, Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer])
        
        st.write(Risk)
    
if __name__== '__main__':
    main()
        
        
        
        
    
