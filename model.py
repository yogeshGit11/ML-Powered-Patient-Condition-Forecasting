import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('Healthcare-dataset.csv')

encoders = {}
for col in ['Gender', 'Blood Type', 'Admission Type', 'Medication', 'Test Results', 'Medical Condition']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

X = df[['Age', 'Gender', 'Blood Type', 'Billing Amount', 'Admission Type', 'Medication', 'Test Results']]
y = df['Medical Condition']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "model/model.pkl")
joblib.dump(encoders, "model/encoders.pkl")

print("Model & encoders saved successfully!")
