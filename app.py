# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 21:50:01 2024

@author: Ayush kumar chaudhary
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Smart Carezone",
                   layout="wide",
                   page_icon="hospital")


# loading saved model
dibetes = pickle.load(open("D:/Smart Healthcare System for Disease Prediction/Multiple Disease Prediction System/saved model/dibetes_model.sav",'rb'))

heart_disease_model = pickle.load(open("D:/Smart Healthcare System for Disease Prediction/Multiple Disease Prediction System/saved model/heart_model.sav",'rb'))

parkinson = pickle.load(open("D:/Smart Healthcare System for Disease Prediction/Multiple Disease Prediction System/saved model/parkinsons_model.sav",'rb'))

Breast_cancer = pickle.load(open("D:/Smart Healthcare System for Disease Prediction/Multiple Disease Prediction System/saved model/Breast_Cancer.sav",'rb'))





# sidebarfor navigate

with st.sidebar:
    
    selected =  option_menu("Smart Carezone for Disease Prediction",
                            
                            
                            ['Diabetes Prediction',
                             'Heart Disease Prediction',
                             'Parkinsons Prediction',
                             'Breast Cancer Prediction'],
                            
                            menu_icon='hospital-fill',
                            icons = ['activity','heart','person','lungs-fill'],
                            default_index=0)
    

    
    
    
# Diabetes Prediction page
if(selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    

     
    # getting the input data from the user
    # columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
        
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness vValue')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value ')
        
    with col2:
        Age = st.text_input('Age of the Person')
        
        
    

    
    
    # code for Prediction
    diab_dignosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_dignosis =  dibetes.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_dignosis[0]==1):
            diab_dignosis = 'The Person is Diabetic'
            
        else:
            diab_dignosis = 'The Person is not Diabetic'
            
            
    st.success(diab_dignosis)
    
    
    
    
    
    
    
    
# Heart Prediction Page 
# columns for input fields   
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    
    # getting the input data from the user
    # columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of the Person')
        
    with col2:
        sex = st.text_input('sex')
        
    with col3:
        cp = st.text_input('Chest pain types')
        
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum cholestoral in mg/dl')
    
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic result')
        
    with col2:
        thalach = st.text_input('Maximum Heart rate achieved  ')
    
    with col3:
        exang = st.text_input('Exercise Induced Angins')
    
    with col1:
        oldpeak = st.text_input('ST depression induced Angins')
    
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flyourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = Fixed defact; 2 = reversable defect')
        
        
        
    # code for Prediction
    heart_dignosis = ''
    # Creating a button for prediction
    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to numeric types
            inputs = [
                int(age), int(sex), int(cp), float(trestbps), float(chol),
                int(fbs), int(restecg), float(thalach), int(exang),
                float(oldpeak), int(slope), int(ca), int(thal)
            ]

            # Make prediction
            prediction = heart_disease_model.predict([inputs])

            if prediction[0] == 1:
                heart_diagnosis = 'The Person is having heart disease'
            else:
                heart_diagnosis = 'The Person does not have any heart disease'

        except ValueError:
            heart_diagnosis = "Please enter valid numeric inputs for all fields."

    st.success(heart_dignosis)
    
    
    
    
    
    
    

# columns for input fields
# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    # Input fields in columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")

    with col1:
        Shimmer = st.text_input("MDVP:Shimmer")
    with col2:
        HNR = st.text_input("HNR")
    with col3:
        RPDE = st.text_input("RPDE")
    with col4:
        DFA = st.text_input("DFA")
        
     # code for Prediction
    prediction = ''

    if st.button("Parkinson's Test Result"):
        prediction= parkinson.predict([[float(fo), float(fhi), float(flo), float(Jitter_percent),
                                 float(Shimmer), float(HNR), float(RPDE), float(DFA)]])
        

        if prediction[0] == 1:
            st.success("The person has Parkinson's disease")
        else:
            st.success("The person does not have Parkinson's disease")

      

    st.success(prediction)

    

    
# Breast Cancer Prediction page
# columns for input fields
if selected == 'Breast Cancer Prediction':
    # Page title
    st.title("Breast Cancer Prediction using ML")

    # Columns for input fields
    col1, col2 = st.columns(2)

    # Collect user inputs with unique keys
    with col1:
        mean_radius = st.text_input("Mean Radius")
           
    with col2:
        mean_texture = st.text_input('mean texture')

    with col1:
        mean_perimeter = st.text_input('mean perimeter')

    with col2:
        mean_area = st.text_input('mean area')
        
    with col1:
            mean_concavity = st.text_input("mean concavity")
            
            
     # code for Prediction
    cancer_diagnosis = ''
           
            

     # creating a button for Prediction    
    if st.button("Breast Cancer's Test Result"):
                cancer_diagnosis = Breast_cancer.predict([[ float(mean_radius), float(mean_texture), float(mean_perimeter), float(mean_area),
                                                          float(mean_concavity)]])



                if (cancer_diagnosis[0] == 1):
                      cancer_diagnosis = "The Breast Cancer is Benign"
                else:
                    cancer_diagnosis = "The Breast Cancer is Malignant"

    st.success(cancer_diagnosis)




  


     
      
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    