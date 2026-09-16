from django.db import models

class Prediction(models.Model):
    WBC = models.FloatField()
    LYM_percentage = models.FloatField()
    NEUT_percentage = models.FloatField()
    LYM_number = models.FloatField()
    NEUT_number = models.FloatField()
    RBC = models.FloatField()
    HGB = models.FloatField()
    HCT = models.FloatField()
    MCV = models.FloatField()
    MCH = models.FloatField()
    MCHC = models.FloatField()
    PLT = models.FloatField()
    PDW = models.FloatField()
    PCT = models.FloatField()
    Diagnosis = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Diagnosis} - {self.timestamp}"
