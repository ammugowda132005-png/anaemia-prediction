from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
import joblib
import numpy as np
from .forms import PredictForm
import pandas as pd

def home(request):
    return render(request, 'anemia/home.html')

def about(request):
    return render(request, 'anemia/about.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'anemia/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'anemia/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def predict(request):
    anemia_descriptions = {
        'Iron deficiency anemia': 'Iron deficiency anemia is a common type of anemia that occurs when the body does not have enough iron to produce adequate hemoglobin. Symptoms include fatigue, weakness, pale skin, and shortness of breath.',
        'Vitamin deficiency anemia': 'Vitamin deficiency anemia can result from a lack of vitamin B12 or folate. Symptoms include fatigue, weakness, and pale or yellowish skin.',
        'Aplastic anemia': 'Aplastic anemia is a rare condition in which the body stops producing enough new blood cells. Symptoms include fatigue, frequent infections, and uncontrolled bleeding.',
        'Sickle cell anemia': 'Sickle cell anemia is a hereditary form of anemia where the red blood cells become rigid and shaped like sickles. Symptoms include pain, fatigue, and frequent infections.',
        'Normocytic normochromic anemia': 'Normocytic normochromic anemia occurs when the red blood cells are normal in size and color but are low in number. It can be caused by chronic diseases, acute blood loss, or bone marrow failure.',
        'Normocytic hypochromic anemia': 'Normocytic hypochromic anemia occurs when red blood cells are normal in size but have less hemoglobin than normal. This can result in fatigue, weakness, and pale skin.',
        'Other microcytic anemia': 'Other microcytic anemia refers to anemia types where the red blood cells are smaller than normal. Causes can include thalassemia and chronic disease. Symptoms include fatigue and weakness.',
        'Leukemia': 'Leukemia is a type of cancer of the blood-forming tissues, hindering the body’s ability to fight infection. Symptoms include fever, fatigue, frequent infections, and bleeding.',
        'Healthy': 'No signs of anemia or blood disorders detected. Maintain a balanced diet and regular check-ups to stay healthy.',
        'Thrombocytopenia': 'Thrombocytopenia is a condition characterized by low levels of platelets in the blood. Symptoms can include easy or excessive bruising, prolonged bleeding, and fatigue.',
        'Leukemia with thrombocytopenia': 'Leukemia with thrombocytopenia is a condition where both leukemia and low platelet count are present. Symptoms can include frequent infections, fatigue, bruising, and bleeding.',
        'Macrocytic anemia': 'Macrocytic anemia is a condition where the red blood cells are larger than normal. It is often caused by vitamin B12 or folate deficiency. Symptoms include fatigue, pale skin, and shortness of breath.'
    }

    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            # Load the model
            model = joblib.load('anemia_model.pkl')

            # Get the form data
            hgb = form.cleaned_data['hgb']
            rbc = form.cleaned_data['rbc']
            mcv = form.cleaned_data['mcv']
            mch = form.cleaned_data['mch']
            mchc = form.cleaned_data['mchc']
            plt = form.cleaned_data['plt']
            wbc = form.cleaned_data['wbc']

            # Make prediction
            prediction = model.predict([[hgb, rbc, mcv, mch, mchc, plt, wbc]])[0]

            # Get description
            description = anemia_descriptions.get(prediction, 'Description not available.')

            # Load the dataset
            df = pd.read_csv('diagnosed_cbc_data_v4 2.csv')

            # Calculate descriptive statistics
            descriptive_stats = df.describe().to_dict()

            # Model accuracy (as an example)
            model_accuracy = 0.9883268482490273

            # Confusion matrix
            confusion_matrix = [
                [80, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 34, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 5, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 3, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 56, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 45, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 13, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 17]
            ]

            return render(request, 'anemia/result.html', {
                'prediction': prediction,
                'description': description,
                'descriptive_stats': descriptive_stats,
                'model_accuracy': model_accuracy,
                'confusion_matrix': confusion_matrix
            })
    else:
        form = PredictForm()

    return render(request, 'anemia/predict.html', {'form': form})

def result(request, prediction):
    return render(request, 'anemia/result.html', {'prediction': prediction})

@login_required
def data_analytics(request):
    # Load the data
    df = pd.read_csv('diagnosed_cbc_data_v4 2.csv')

    # Prepare the data for display and charts
    pie_labels = df['Diagnosis'].unique().tolist()
    pie_values = df['Diagnosis'].value_counts().tolist()

    # For the bar chart, let's use 'Diagnosis' and count occurrences of each diagnosis
    bar_labels = df['Diagnosis'].unique().tolist()
    bar_values = df['Diagnosis'].value_counts().tolist()

    # For the line chart, we can use a relevant numerical column over the index (assuming index represents some time sequence)
    line_labels = df.index.tolist()
    line_datasets = [
        {
            'label': 'WBC',
            'data': df['WBC'].tolist(),
            'borderColor': 'rgba(75, 192, 192, 1)',
            'backgroundColor': 'rgba(75, 192, 192, 0.2)'
        }
    ]

    context = {
        
        'pie_labels': pie_labels,
        'pie_values': pie_values,
        'bar_labels': bar_labels,
        'bar_values': bar_values,
        'line_labels': line_labels,
        'line_datasets': line_datasets
    }
    
    return render(request, 'data_analytics.html', context)