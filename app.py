import Orange
import pickle
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import numpy as np

model_widow = pickle.load(open("models/widowpension.pkcls", "rb"))
model_disability = pickle.load(open("models/disabilitypension.pkcls", "rb"))
model_pmuy = pickle.load(open("models/pmuy.pkcls", "rb"))
model_oldage = pickle.load(open("models/oldage.pkcls", "rb"))
model_suraksha = pickle.load(open("models/surakshabima.pkcls", "rb"))
model_kisansamman = pickle.load(open("models/kisaansamman.pkcls", "rb"))
model_krishisinch = pickle.load(open("models/krishisinch.pkcls", "rb"))
model_kisancreditcard = pickle.load(open("models/kisaancreditcard.pkcls", "rb"))
model_financialassistance = pickle.load(open("models/financialassistance.pkcls", "rb"))
model_agriclinic = pickle.load(open("models/agriclinic.pkcls", "rb"))
model_brambedkar = pickle.load(open("models/brambedkar.pkcls", "rb"))
model_deendayal = pickle.load(open("models/deendayal.pkcls", "rb"))
model_pmkvy = pickle.load(open("models/pmkvy.pkcls", "rb"))
model_agnipath = pickle.load(open("models/agnipath.pkcls", "rb"))
model_pmayg = pickle.load(open("models/pmayg.pkcls", "rb"))


def preprocess_gender(gender):
    if gender == 'Male':
        return 1
    elif gender == 'Female':
        return 2
    else:
        return 0


def preprocess_disability(disability):
    if disability == 'Yes':
        return 1
    elif disability == 'No':
        return 2
    else:
        return 0


def preprocess_student(student):
    if student == 'Yes':
        return 1
    elif student == 'No':
        return 2
    else:
        return 0


def preprocess_employment(employment):
    if employment == 'Government Employed':
        return 1
    elif employment == 'Self Employed':
        return 2
    elif employment == 'Unemployed':
        return 3
    else:
        return 0


def preprocess_farmer(farmer):
    if farmer == 'Yes':
        return 1
    elif farmer == 'No':
        return 2
    else:
        return 0


def preprocess_bpl(bpl):
    if bpl == 'Yes':
        return 1
    elif bpl == 'No':
        return 2
    else:
        return 0


def preprocess_area(area):
    if area == 'Urban':
        return 1
    elif area == 'Rural':
        return 2
    else:
        return 0


def preprocess_marriage_status(marriage_status):
    if marriage_status == 'Married':
        return 1
    elif marriage_status == 'Un-Married':
        return 2
    elif marriage_status == 'Divorced':
        return 3
    else:
        return 0


def main():
    st.title('Government Scheme Eligibility Prediction')
    st.write('Enter the user details to predict the eligibility for government schemes.')

    gender = st.selectbox('Gender', ['Male', 'Female'])
    age = st.number_input('Age', min_value=1)
    disability = st.radio('Are You Disabled?', ['Yes', 'No'])
    student = st.radio('Are You A Student?', ['Yes', 'No'])
    employment = st.selectbox('Employment status', ['Governmnent Employed', 'Self Employed', 'Unemployed'])
    farmer = st.radio('Are You A Farmer?', ['Yes', 'No'])
    bpl = st.radio('Does Your Family Have a BPL Card?', ['Yes', 'No'])
    familyincome = st.number_input('Your Family Income (Annual)', min_value=0)
    disability_percentage = st.number_input('Enter Your Disability Percentage (If not disabled, just enter 0)', min_value=0)
    area = st.selectbox('Which Area Do You Live In?', ['Urban', 'Rural'])
    marriage_status = st.selectbox('Your Marital Status', ['Married', 'Un-Married', 'Divorced'])

    if st.button('Predict Eligibility'):
        # Preprocess user inputs
        gender = preprocess_gender(gender)
        disability = preprocess_disability(disability)
        student = preprocess_student(student)
        employment = preprocess_employment(employment)
        farmer = preprocess_farmer(farmer)
        bpl = preprocess_bpl(bpl)
        area = preprocess_area(area)
        marriage_status = preprocess_marriage_status(marriage_status)

        # Prepare the input data
        input_data = np.array([[gender, age, disability, student, employment, farmer, bpl, familyincome, disability_percentage, area, marriage_status]])

        # Make predictions using the trained models
        predictions_widow = model_widow.predict(input_data)
        predictions_disability = model_disability.predict(input_data)
        pred_pmuy = model_pmuy.predict(input_data)
        pred_suraksha = model_suraksha.predict(input_data)
        pred_oldage = model_oldage.predict(input_data)
        pred_kisansamman = model_kisansamman.predict(input_data)
        pred_krishisinch = model_krishisinch.predict(input_data)
        pred_kisancard = model_kisancreditcard.predict(input_data)
        pred_agriclinic = model_agriclinic.predict(input_data)
        pred_brambedkar = model_brambedkar.predict(input_data)
        pred_deendayal = model_deendayal.predict(input_data)
        pred_financial = model_financialassistance.predict(input_data)
        pred_pmkvy = model_pmkvy.predict(input_data)
        pred_agnipath = model_agnipath.predict(input_data)
        pred_pmayg = model_pmayg.predict(input_data)

        # Display the predicted schemes
        st.subheader('You may be eligible for:')
        if predictions_widow[0] == 1:
            st.write('Widow Women Pension Scheme (Haryana)')

        if predictions_disability[0] == 1:
            st.write('Disability Pension Scheme (Haryana)')

        if pred_pmuy[0] == 1:
            st.write('Pradhan Mantri Ujjwala Yojana (PMUY) (Central)')

        if pred_oldage[0] == 1:
            st.write('OLD AGE SAMMAN ALLOWANCE SCHEME (Haryana)')

        if pred_suraksha[0] == 1:
            st.write('Pradhan Mantri Suraksha Bima Yojana (Central)')

        if pred_kisansamman[0] == 1:
            st.write('Pradhan Mantri Kisan Samman Nidhi (Central)')

        if pred_krishisinch[0] == 1:
            st.write('Pradhan Mantri Krishi Sinchayee Yojana: Per Drop More Crop (Central)')

        if pred_kisancard[0] == 1:
            st.write('Kisan Credit Card (Central)')

        if pred_agriclinic[0] == 1:
            st.write('Agri-Clinics And Agri-Business Centres Scheme (Central)')

        if pred_deendayal[0] == 1:
            st.write('Deen Dayal Upadhyay Grameen Kaushalya Yojana (Central)')

        if pred_brambedkar[0] == 1:
            st.write('Dr. B.R. Ambedkar Awas Navinikarn Yojana (Haryana)')

        if pred_financial[0] == 1:
            st.write('Financial Assistance Scheme For Higher Competitive/ Entrance Examination To Scheduled Castes/ Backward Classes Students (Haryana)')

        if pred_pmkvy[0] == 1:
            st.write('Pradhan Mantri Kaushal Vikas Yojana (Central)')

        if pred_pmayg[0] == 1:
            st.write('Pradhan Mantri Awaas Yojana Gramin (PMAYG) (Central)')

        if pred_agnipath[0] == 1:
            st.write('Agnipath Yojana (Central)')


if __name__ == '__main__':
    main()
