import streamlit as st
import os
import pandas as pd
import joblib as jb

heading_style = '''
<div style="color:red;" align='center'>
<h1>Health Care </h1>
</div>
'''
def return_df(gender,
age,
hypertension,
heart_disease,
ever_married,
work_type,
Residence_type,
avg_glucose_level,
bmi,
smoking_status):
    kbn={
	'gender':[gender],
	'age':[age],
	'hypertension':[hypertension],
	'heart_disease':[heart_disease],
	'ever_married':[ever_married],
	'work_type':[work_type],
	'Residence_type':[Residence_type],
	'avg_glucose_level':[avg_glucose_level],
	'bmi':[bmi],
	'smoking_status':[smoking_status]
    }   
    final_df=pd.DataFrame(kbn)
    return final_df

@st.cache_resource()
def base_model():
    bmodel=jb.load(os.path.join('finalized_nb_model2.pkl'))
    return bmodel

st.markdown(heading_style, unsafe_allow_html=True)
gender=st.selectbox('select your gender',['Male','Female'])
age=st.number_input('enter your age',min_value=0)
heart_disease=st.slider('heartdisease',0,1,0)
hypertension=st.slider(' hypertension',0,1,0)
ever_married=st.selectbox('married?',['Yes','No'])
work_type=st.selectbox('select work_type',['Private	','Self-employed','Govt_job	'])
Residence_type=st.selectbox('select Residencetype',['urban','rural'])
avg_glucose_level=st.number_input('glucoselevel',min_value=0)
bmi=st.number_input('bmi',min_value=0)
smoking_status=st.selectbox('smoking status',['formerly smoked','never smoked','Unknown'])

df=return_df(gender,
age,
hypertension,
heart_disease,
ever_married,
work_type,
Residence_type,
avg_glucose_level,
bmi,
smoking_status)
if st.button('Submit'):
	model=base_model()
	preds=model.predict(df)
	predictions=preds[0]
	if predictions==1:
		st.write('stroke')
	elif predictions==0:
			st.write('No stroke')
	