# detection/forms.py
from django import forms

class DiabetesForm(forms.Form):
    pregnancies = forms.IntegerField(label='Pregnancies', min_value=0)
    glucose = forms.IntegerField(label='Glucose', min_value=0)
    bloodPressure = forms.IntegerField(label='Blood Pressure', min_value=0)
    skinThickness = forms.IntegerField(label='Skin Thickness', min_value=0)
    insulin = forms.IntegerField(label='Insulin', min_value=0)
    bmi = forms.FloatField(label='BMI', min_value=0)
    diabetesPedigreeFunction = forms.FloatField(label='Diabetes Pedigree Function', min_value=0)
    age = forms.IntegerField(label='Age', min_value=0)

