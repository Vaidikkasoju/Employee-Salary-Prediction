# 💰 Employee Salary Prediction Web App

This project is a **Streamlit-based web application** that predicts the salary of software professionals based on **Country**, **Education Level**, and **Years of Experience**. It also provides an interactive dashboard to **explore salary trends** from the Stack Overflow Developer Survey.

---

## 🚀 Features

- 🔍 **Explore Page** : Visualize mean salaries by country and years of experience
- 🤖 **Predict Page** : Estimate your salary using a machine learning regression model
- 📊 Interactive UI powered by **Streamlit**
- 🧠 Model trained using real-world survey data

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend/ML**: Python, Scikit-learn, Pandas, Matplotlib
- **Deployment**: Local or Streamlit Cloud
- **Data Source**: Stack Overflow Developer Survey (CSV)

---

**🔎 How It Works**
DATA LOADING AND CLEANING
- Filters full-time employees
- Removes missing and outlier salaries
- Standardizes education and experience fields

Dataset - https://drive.google.com/file/d/1zEQSOp1AFCVNUZ7Q3sHAf-47_30OWvxf/view?usp=sharing

MODEL TRAINING (salary_prediction.ipynb)
- Encodes categorical features using LabelEncoder
- Trains a regression model on cleaned data
- Saves model and encoders in saved_steps.pkl

WEB APPLICATION
- **app.py** runs the main Streamlit app
- **explore_page.py** shows salary insights
- **predict_page.py** takes user input, transforms it, and predicts salary

## 📁 Project Structure

```bash
.
├── app.py                  # Main entry point with sidebar navigation
├── explore_page.py         # EDA visualizations
├── predict_page.py         # ML input and prediction interface
├── salary_prediction.ipynb # Model training notebook
├── saved_steps.pkl         # Pickled model and label encoders
├── survey_results_public.csv  # Source data file
└── README.md               # Project documentation
