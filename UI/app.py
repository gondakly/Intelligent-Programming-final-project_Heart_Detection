import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from experta import KnowledgeEngine, Rule, Fact, MATCH, TEST
import joblib

# CSS & UI ENHANCEMENT
st.set_page_config(page_title="Heart Risk Expert System", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    h1 { color: #2c3e50; font-family: 'Arial', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

#STEP 3: EXPERTA RULE-BASED SYSTEM
class HeartDiseaseExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.risk = "Moderate"

    @Rule(Fact(cholesterol=MATCH.c), Fact(age=MATCH.a), TEST(lambda c, a: c > 240 and a > 50))
    def rule1(self): self.risk = "High"

    @Rule(Fact(bp=MATCH.b), Fact(smoking=True), TEST(lambda b: b > 140))
    def rule2(self): self.risk = "High"

    @Rule(Fact(exercise=True), Fact(bmi=MATCH.bmi), TEST(lambda bmi: bmi < 25))
    def rule3(self): self.risk = "Low"

    @Rule(Fact(chest_pain=True), Fact(max_hr=MATCH.hr), TEST(lambda hr: hr > 170))
    def rule4(self): self.risk = "High"

    @Rule(Fact(age=MATCH.a), TEST(lambda a: a < 30))
    def rule5(self): self.risk = "Low"

    @Rule(Fact(smoking=True), Fact(diabetes=True))
    def rule6(self): self.risk = "High"

    @Rule(Fact(family_history=True), Fact(age=MATCH.a), TEST(lambda a: a > 45))
    def rule7(self): self.risk = "High"

    @Rule(Fact(cholesterol=MATCH.c), TEST(lambda c: c < 150))
    def rule8(self): self.risk = "Low"

    @Rule(Fact(bp=MATCH.b), TEST(lambda b: b < 110))
    def rule9(self): self.risk = "Low"

    @Rule(Fact(bmi=MATCH.bmi), TEST(lambda bmi: bmi > 30))
    def rule10(self): self.risk = "High"

    def get_risk(self): return self.risk

# APP LOGIC
st.title("Heart Disease Diagnostic Suite")
st.markdown("### Hybrid Expert System and Machine Learning Analysis")

uploaded_file = st.sidebar.file_uploader("Upload Heart Disease CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    tabs = st.tabs(["Processing and Viz", "Decision Tree", "Expert System", "Comparison"])

    # STEP 1 & 2: DATA PROCESSING
    with tabs[0]:
        st.header("Step 1 and 2: Data Engineering")
        df = df.fillna(df.median(numeric_only=True))
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Cleaned Data Preview:**")
            st.dataframe(df.head())
        
        with col2:
            st.write("**Correlation Heatmap:**")
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(df.corr(), annot=True, cmap="Blues", fmt=".2f")
            st.pyplot(fig)

    # STEP 4: DECISION TREE & PREDICTION
    with tabs[1]:
        st.header("Step 4: Decision Tree Model")
        
        # Prepare Data
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
        X_encoded = pd.get_dummies(X)
        X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
        
        # Model Training
        depth = st.slider("Max Tree Depth", 1, 20, 5)
        dt = DecisionTreeClassifier(max_depth=depth)
        dt.fit(X_train, y_train)
        
        # Metrics
        y_pred = dt.predict(X_test)
        st.metric("Model Accuracy", f"{accuracy_score(y_test, y_pred):.2%}")

        # NEW: LIVE PREDICTION INPUT SECTION
        st.markdown("---")
        st.subheader("Model Prediction Input")
        st.write("Enter patient data below to get a prediction from the Decision Tree.")
        
        input_data = {}
        cols = st.columns(3)
        
        # Dynamically create inputs based on original columns
        for i, col in enumerate(X.columns):
            with cols[i % 3]:
                if X[col].dtype == 'object' or X[col].nunique() < 5:
                    input_data[col] = st.selectbox(f"{col}", options=df[col].unique())
                else:
                    input_data[col] = st.number_input(f"{col}", value=float(df[col].mean()))

        if st.button("Predict with Decision Tree"):
            # Convert user input to DataFrame
            input_df = pd.DataFrame([input_data])
            # Apply same One-Hot Encoding
            input_encoded = pd.get_dummies(input_df)
            # Reindex to match training columns (fills missing dummy columns with 0)
            input_final = input_encoded.reindex(columns=X_train.columns, fill_value=0)
            
            prediction = dt.predict(input_final)[0]
            probability = dt.predict_proba(input_final)
            
            res_color = "red" if prediction == 1 else "green"
            st.markdown(f"#### Predicted Result: <span style='color:{res_color}'>{'Positive' if prediction == 1 else 'Negative'}</span>", unsafe_allow_html=True)
            st.write(f"Confidence: {np.max(probability):.2%}")

    #STEP 3: EXPERT SYSTEM
    with tabs[2]:
        st.header("Step 3: Experta Inference Engine")
        with st.form("expert_form"):
            c1, c2, c3 = st.columns(3)
            age = c1.number_input("Age", 1, 100, 45)
            chol = c2.number_input("Cholesterol", 100, 500, 200)
            bp = c3.number_input("Blood Pressure", 80, 200, 120)
            smoke = st.checkbox("Smoker")
            exercise = st.checkbox("Regular Exercise")
            submit = st.form_submit_button("Run Expert Inference")
            
            if submit:
                engine = HeartDiseaseExpert()
                engine.reset()
                engine.declare(Fact(age=age), Fact(cholesterol=chol), Fact(bp=bp), 
                               Fact(smoking=smoke), Fact(exercise=exercise))
                engine.run()
                st.markdown(f"### Expert Risk Level: {engine.get_risk()}")

    # STEP 5: COMPARISON
    with tabs[3]:
        st.header("Step 5: System Comparison")
        st.write("**Model Explainability (Tree Visualization):**")
        fig, ax = plt.subplots(figsize=(12, 8))
        plot_tree(dt, feature_names=X_train.columns, filled=True, max_depth=3, class_names=['Negative', 'Positive'])
        st.pyplot(fig)

else:
    st.warning("Please upload a CSV file to begin.")