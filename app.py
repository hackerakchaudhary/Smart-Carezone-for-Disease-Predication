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

parkinson = pickle.load(open("D:/Smart Healthcare System for Disease Prediction/Multiple Disease Prediction System/saved model/parkinson_model.sav",'rb'))

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
    
    
    
    
    
    
    
    
# Parkinsons Prediction page
if (selected =='Parkinsons Prediction'):
    
   
    #page title
    st.title('Parkinsons Prediction using ML')
    
    
    # getting the input data from the user
    # columns for input fields
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')
        
        

    # code for Prediction
    parkinsons_diagnosis = ''
    
    

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_diagnosis = parkinson.predict([[float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]])



        if (parkinsons_diagnosis[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    
    
    
    
    
# Breast Cancer Prediction page
if selected == 'Breast Cancer Prediction':
    # Page title
    st.title("Breast Cancer Prediction using ML")

    # Columns for input fields
    col1, col2, col3, col4, col5 = st.columns(5)

    # Collect user inputs with unique keys
    with col1:
        mean_radius = st.text_input("Mean Radius")
           
    with col2:
        mean_texture = st.text_input('mean texture')

    with col3:
        mean_perimeter = st.text_input('mean perimeter')

    with col4:
        mean_area = st.text_input('mean area')

    with col5:
        mean_smoothness = st.text_input('mean smoothness')

    with col1:
        mean_compactness = st.text_input('mean compactness')
        
    with col2:
            mean_concavity = st.text_input("mean concavity")
               
    with col3:
            mean_concave_points = st.text_input('mean concave point')

    with col4:
            mean_symmetry = st.text_input('mean_symmetry')

    with col5:
            mean_fractal_dimension = st.text_input('mean_fractal_dimension')

    with col1:
            radius_error = st.text_input('radius_error')
            
    with col2:
            texture_error = st.text_input('texture_error')
    
    with col3:
            perimeter_error = st.text_input("perimeter error")
               
    with col4:
            area_error = st.text_input('area_error')

    with col5:
            smoothness_error = st.text_input('smoothness_error')

    with col1:
            compactness_error = st.text_input('compactness_error')

    with col2:
            concavity_error = st.text_input('concavity_error')
            
    with col3:
            concave_points_error = st.text_input('concave_points_error')
            
    with col4:
            symmetry_error = st.text_input("symmetry_error")
               
    with col5:
            fractal_dimension_error = st.text_input('fractal_dimension_error')

    with col1:
            worst_radius = st.text_input('worst_radius')

    with col2:
            worst_texture = st.text_input('worst_texture')

    with col3:
            worst_perimeter = st.text_input('worst_perimeter')
            
    with col4:
            worst_area = st.text_input('worst_area')      
            
    with col5:
            worst_smoothness = st.text_input("worst_smoothness")
               
    with col1:
            worst_compactness = st.text_input('worst_compactness')

    with col2:
            worst_concavity = st.text_input('worst_concavity')

    with col3:
            worst_concave_points = st.text_input('worst_concave_points')

    with col4:
            worst_symmetry = st.text_input('worst_symmetry')
            
    with col5:
            worst_fractal_dimension = st.text_input('worst_fractal_dimension') 
            
            
     # code for Prediction
    cancer_diagnosis = ''
           
            

     # creating a button for Prediction    
    if st.button("Breast Cancer's Test Result"):
                cancer_diagnosis = Breast_cancer.predict([[ float(mean_radius), float(mean_texture), float(mean_perimeter), float(mean_area),
                                                         float(mean_smoothness), float(mean_compactness), float(mean_concavity),
                                                         float(mean_concave_points), float(mean_symmetry), float(mean_fractal_dimension),
                                                         float(radius_error), float(texture_error), float(perimeter_error), float(area_error),
                                                         float(smoothness_error), float(compactness_error), float(concavity_error),
                                                         float(concave_points_error), float(symmetry_error), float(fractal_dimension_error),
                                                         float(worst_radius), float(worst_texture), float(worst_perimeter), float(worst_area),
                                                         float(worst_smoothness), float(worst_compactness), float(worst_concavity),
                                                         float(worst_concave_points), float(worst_symmetry), float(worst_fractal_dimension)]])



                if (cancer_diagnosis[0] == 1):
                      cancer_diagnosis = "The Breast Cancer is Benign"
                else:
                    cancer_diagnosis = "The Breast Cancer is Malignant"

    st.success(cancer_diagnosis)




  


     
      
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    