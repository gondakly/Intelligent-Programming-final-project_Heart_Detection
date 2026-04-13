import pandas as pd
import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

#load the cleaned data
df = pd.read_csv('D:/downloads 2 imp/2ND TERM 3RD YEAR/Intelligent Programming/MAIN PROJECT/Data Cleaning/heart_Cleaned data.csv')

#Define The Input Features X And Target y
#Ensure target is removed from features
X = df.drop(columns=['target'])
y = df['target']
# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Train the Decision Tree
classifier = DecisionTreeClassifier(max_depth=3, random_state=42)
classifier.fit(X, y)
# saves your trained logic into a .joblib file
joblib.dump(classifier, 'D:/downloads 2 imp/2ND TERM 3RD YEAR/Intelligent Programming/MAIN PROJECT/Decison Tree (Model Train)/heart_disease_model.joblib')

#Evaluate the Model
y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1_Score = f1_score(y_test, y_pred)

print(f"Accuracy:  {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall:    {recall:.2f}")
print(f"F1 Score:  {f1_Score :.2f}")

print("Classification Report ")
print(classification_report(y_test, y_pred))