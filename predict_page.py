import streamlit as st
import pickle
import numpy as np

# ✅ Use new Streamlit caching method
@st.cache_data
def load_model():
    with open("saved_steps.pkl", "rb") as file:
        data = pickle.load(file)
    return data

# Load model and encoders
data = load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("🧑‍💻 Employee Salary Prediction")

    st.write("### Please provide the following information to estimate your salary:")

    # ✅ Use the same labels the model was trained on
    countries = le_country.classes_
    education_levels = le_education.classes_

    country = st.selectbox("🌍 Country", countries)
    education = st.selectbox("🎓 Education Level", education_levels)
    experience = st.slider("🧰 Years of Experience", 0, 50, 3)

    ok = st.button("💰 Calculate Salary")
    if ok:
        try:
            # Create input and encode
            X = np.array([[country, education, experience]])
            X[:, 0] = le_country.transform(X[:, 0])
            X[:, 1] = le_education.transform(X[:, 1])
            X = X.astype(float)

            # Predict
            salary = regressor.predict(X)
            st.subheader(f"🤑 The estimated salary is **${salary[0]:,.2f}**")
        except ValueError as e:
            st.error(f"Error: {e}")
