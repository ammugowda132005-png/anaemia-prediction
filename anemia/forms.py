from django import forms

class PredictForm(forms.Form):
    hgb = forms.FloatField(
        label='Hemoglobin (HGB)', 
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Hemoglobin level (e.g., 14.5)'})
    )
    rbc = forms.FloatField(
        label='Red Blood Cell Count (RBC)', 
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Red Blood Cells count (e.g., 5.2)'})
    )
    mcv = forms.FloatField(
        label='Mean Corpuscular Volume (MCV)', 
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Mean Corpuscular Volume (e.g., 90)'})
    )
    mch = forms.FloatField(
        label='Mean Corpuscular Hemoglobin (MCH)', 
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Mean Corpuscular Hemoglobin (e.g., 29)'})
    )
    mchc = forms.FloatField(
        label='Mean Corpuscular Hemoglobin Concentration (MCHC)', 
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Mean Corpuscular Hemoglobin Concentration (e.g., 34)'})
    )
    plt = forms.FloatField(
        label='Platelet Count (PLT)', 
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Platelets count (e.g., 300)'})
    )
    wbc = forms.FloatField(
        label='White Blood Cell Count (WBC)', 
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter White Blood Cells count (e.g., 6.5)'})
    )
