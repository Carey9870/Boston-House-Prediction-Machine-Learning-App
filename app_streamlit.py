# to run type - streamlit run app-streamlit.py

import streamlit as st
import pickle

pickled_model = open('reg_grid.pkl', mode='rb')
classifier = pickle.load(pickled_model)

def house_prices_prediction(CRIM,	ZN,	INDUS,	CHAS,	NOX,	RM,	AGE,	DIS,	RAD,	TAX,	PTRATIO,	B,	LSTAT ):
    prediction = classifier.predict([[CRIM,	ZN,	INDUS,	CHAS,	NOX,	RM,	AGE,	DIS,	RAD,	TAX,	PTRATIO,	B,	LSTAT]])
    print(prediction)
    return prediction

def main():
    st.title('House Prices Prediction')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> Streamlit House Price Prediction ML App </h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    CRIM = st.text_input("CRIM", "")
    ZN = st.text_input("ZN", "")
    INDUS = st.text_input("INDUS", "")
    CHAS = st.text_input("CHAS", "")
    NOX = st.text_input("NOX", "")
    RM = st.text_input("RM", "")
    AGE = st.text_input("AGE", "")
    DIS = st.text_input("DIS", "")
    RAD = st.text_input("RAD", "")
    TAX = st.text_input("TAX", "")
    PTRATIO = st.text_input("PTRATIO", "")
    B = st.text_input("B", "")
    LSTAT = st.text_input("LSTAT", "")
    
    result = ""
    
    if st.button("Predict"):
        result = house_prices_prediction(CRIM,	ZN,	INDUS,	CHAS,	NOX,	RM,	AGE,	DIS,	RAD,	TAX,	PTRATIO,	B,	LSTAT)
    st.success('The output the house prices are\t {}'.format(result))

if __name__ == "__main__":
    main()