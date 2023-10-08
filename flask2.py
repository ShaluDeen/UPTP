import joblib

# Load the trained model and label encoders
model = joblib.load('disease_prediction_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')
disease_encoder = joblib.load('disease_encoder.pkl')

# Function to predict disease based on user input
def predict_disease(symptoms):
    # Create a dictionary to map user inputs to label encoders
    input_map = {
        'Fever': 'Fever',
        'Cough': 'Cough',
        'Fatigue': 'Fatigue',
        'Difficulty Breathing': 'Difficulty Breathing',
        'Age': 'Age',  # No encoding needed for 'Age'
        'Gender': 'Gender',
        'Blood Pressure': 'Blood Pressure',
        'Cholesterol Level': 'Cholesterol Level',
        'Outcome Variable': 'Outcome Variable'
    }

    # Encode user inputs using label encoders (except for 'Age')
    encoded_symptoms = []
    for input_name, input_value in symptoms.items():
        if input_name != 'Age':
            encoder = label_encoders[input_map[input_name]]
            # Handle the problematic label 'No ' by replacing it with 'No'
            if input_name in ('Fever', 'Cough', 'Fatigue', 'Difficulty Breathing'):
                input_value = input_value.strip()  # Remove leading/trailing spaces
            encoded_value = encoder.transform([input_value])[0]
            encoded_symptoms.append(encoded_value)
        else:
            encoded_symptoms.append(input_value)

    # Make a prediction using the model
    prediction = model.predict([encoded_symptoms])[0]

    # Use label encoders to map the disease code to its label
    disease_label = disease_encoder.inverse_transform([prediction])[0]

    return disease_label

# Function to collect user input
def get_user_input():
    symptoms = {}
    symptoms['Fever'] = input("Fever (Yes/No): ")
    symptoms['Cough'] = input("Cough (Yes/No): ")
    symptoms['Fatigue'] = input("Fatigue (Yes/No): ")
    symptoms['Difficulty Breathing'] = input("Difficulty Breathing (Yes/No): ")
    symptoms['Age'] = int(input("Age (in years): "))  # No encoding needed for 'Age'
    symptoms['Gender'] = input("Gender (Male/Female): ")
    symptoms['Blood Pressure'] = input("Blood Pressure (Normal/High): ")
    symptoms['Cholesterol Level'] = input("Cholesterol Level (Normal/High): ")
    symptoms['Outcome Variable'] = input("Outcome Variable (Positive/Negative): ")
    return symptoms

def main():
    print("Welcome to the Disease Prediction Tool!")

    while True:
        try:
            symptoms = get_user_input()
            predicted_disease = predict_disease(symptoms)
            print(f"The predicted disease is: {predicted_disease}\n")
        except KeyboardInterrupt:
            print("\nThank you for using the Disease Prediction Tool!")
            break

if __name__ == '__main__':
    main()
