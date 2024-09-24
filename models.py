# detection/models.py
from django.db import models

class DiabetesData(models.Model):
    pregnancies = models.IntegerField()
    glucose = models.IntegerField()
    bloodPressure = models.IntegerField()
    skinThickness = models.IntegerField()
    insulin = models.IntegerField()
    bmi = models.FloatField()
    diabetesPedigreeFunction = models.FloatField()
    age = models.IntegerField()
    result = models.CharField(max_length=20)

    def __str__(self):
        return f"Pregnancies: {self.pregnancies}, Glucose: {self.glucose}"
