import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
data = pd.read_csv("C:/Users/Shalu Deen/Documents/Prediction/Symptoms.csv")

# Encode categorical variables into numerical values
label_encoders = {}
categorical_cols = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 'Gender', 'Blood Pressure', 'Cholesterol Level', 'Outcome Variable']

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Encode the 'Disease' column
disease_encoder = LabelEncoder()
data['Disease'] = disease_encoder.fit_transform(data['Disease'])

# Split the dataset into features and target
X = data.drop('Disease', axis=1)
y = data['Disease']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a machine learning model (Random Forest, for example)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model on the test data
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model for later use
joblib.dump(model, 'disease_prediction_model.pkl')

# Save the label encoders for later use (to decode predictions)
joblib.dump(label_encoders, 'label_encoders.pkl')

# Save the 'Disease' label encoder
joblib.dump(disease_encoder, 'disease_encoder.pkl')
