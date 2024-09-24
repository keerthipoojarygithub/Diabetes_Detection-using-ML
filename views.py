# detection/views.py
import os
import numpy as np
import joblib
from django.shortcuts import render
from django.conf import settings
from .forms import DiabetesForm

def welcome(request):
    return render(request, 'welcome.html')

# Load the model using joblib
model_path = os.path.join(settings.BASE_DIR, 'ap1/models/random_forest_classifier.pkl')
model = joblib.load(model_path)

def predict_diabetes(request):
    result = None
    reasons = []
    precautions = []

    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            data = np.array([[
                form.cleaned_data['pregnancies'],
                form.cleaned_data['glucose'],
                form.cleaned_data['bloodPressure'],
                form.cleaned_data['skinThickness'],
                form.cleaned_data['insulin'],
                form.cleaned_data['bmi'],
                form.cleaned_data['diabetesPedigreeFunction'],
                form.cleaned_data['age'],
            ]])
            prediction = model.predict(data)
            result = 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'

            # Add logic for reasons and precautionary measures
            if result == 'Diabetic':
                if form.cleaned_data['glucose'] > 140:
                    reasons.append("High glucose level")
                if form.cleaned_data['bmi'] > 30:
                    reasons.append("High BMI")
                if form.cleaned_data['bloodPressure'] > 80:
                    reasons.append("High blood pressure")
                if form.cleaned_data['age'] > 45:
                    reasons.append("Older age")

                # Precautionary measures
                precautions = [
                    "Maintain a healthy diet",
                    "Engage in regular physical activity",
                    "Monitor blood sugar levels regularly",
                    "Consult with a healthcare provider for regular checkups",
                    "Avoid smoking and limit alcohol consumption"
                ]
    else:
        form = DiabetesForm()

    return render(request, 'form.html', {'form': form, 'result': result, 'reasons': reasons, 'precautions': precautions})
