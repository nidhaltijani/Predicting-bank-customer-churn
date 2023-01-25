import streamlit as st 
import joblib 
import pandas as pd
features=['CreditScore', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
       'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Geography_Germany',
       'Geography_Spain']

def main():
    model=joblib.load(open("Random_forest_churn_model.pkl","rb"))
    st.title("Bank Customer Churn Prediction")
    credit_score=st.number_input("Credit Score")
    gender = st.selectbox(label='Gender', options=['Male','Female'])
    if gender=='Male':
        gender=0
    elif gender=='Female':
        gender=1
    age=st.slider("Age",0,100,18)
    tenure=st.slider("Tenure",0,10,0)
    balance=st.number_input("Enter your Balance")
    Num_prods=st.slider("Number of products",1,4,1)    
    hascr_card = st.selectbox(label='Owner of a Credit Card ?', options=['Yes', 'No'])
    if hascr_card =='Yes':
        hascr_card=1
    elif hascr_card == 'No':
        hascr_card=0
    
    active = st.selectbox(label=' Is this an active member ?', options=['Yes', 'No'])
    if active =='Yes':
        active=1
    elif active == 'No':
        active=0 
    
    salary= st.number_input("Enter the estimated salary")
    
    geography = st.selectbox(label='Gender', options=['France','Germany','Spain'])
    geography_ger=0
    geography_spa=0
    if geography=='France':
        geography_ger=0
        geography_spa=0
    elif geography=='Germany':
        geography_ger=1
        geography_spa=0
    elif geography=='Spain':
        geography_ger=0
        geography_spa=1   
    
    df_pred = pd.DataFrame({
        'CreditScore' : credit_score,
        'Gender' : gender,
        'Age' : age,
        'Tenure' : tenure,
        'Balance':balance,
        'NumOfProducts' :Num_prods,
        'HasCrCard' :hascr_card,
        'IsActiveMember':active,
        'EstimatedSalary':salary,
        'Geography_Germany':geography_ger,
        'Geography_Spain':geography_ger,
        
        },index=[0])
    submitted=st.button("Submit")
    if submitted:
        prediction=model.predict(df_pred)
        st.balloons()
        if prediction[0]==0:
            st.success('This customer is more likely to stay')
        else :
            st.success('This customer is more likely to churn')
        
        

if __name__=='__main__':
    main()
