from flask import Flask, render_template, request, redirect, url_for, session
from tracker.data_input import DataInput
from tracker.prediction import MenstrualCyclePredictor
from tracker.advice import AdviceGenerator
from tracker.resources import ResourceProvider
import os

app = Flask(__name__)
import os

app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')  # Add a secret key for session management

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        data_input = DataInput()
        data_input.cycle_data = {
            'start_date': request.form['start_date'],
            'cycle_length': int(request.form['cycle_length']),
            'period_length': int(request.form['period_length']),
            'symptoms': request.form['symptoms'].split(','),
            'flow_intensity': request.form['flow_intensity'],
            'ovulation_symptoms': request.form['ovulation_symptoms'].split(','),
            'mood_changes': request.form['mood_changes'].split(','),
            'basal_body_temperature': float(request.form['basal_body_temperature']),
            'weight': float(request.form['weight']),
            'lifestyle_factors': request.form['lifestyle_factors'].split(','),
            'medication': request.form['medication'].split(','),
            'sexual_activity': request.form['sexual_activity'],
            'notes': request.form['notes']
        }
        session['cycle_data'] = data_input.get_data()  # Store data in session
        return redirect(url_for('display_data'))
    return render_template('input.html')

@app.route('/display')
def display_data():
    cycle_data = session.get('cycle_data')  # Retrieve data from session
    return render_template('display.html', cycle_data=cycle_data)

@app.route('/predict')
def predict():
    cycle_data = session.get('cycle_data')  # Retrieve data from session
    predictor = MenstrualCyclePredictor(cycle_data)
    predictions = {
        'next_period': predictor.predict_next_period(),
        'ovulation': predictor.predict_ovulation(),
        'fertile_window': predictor.forecast_fertile_window()
    }
    return render_template('predict.html', predictions=predictions)

@app.route('/advice')
def advice():
    cycle_data = session.get('cycle_data')  # Retrieve data from session
    advice_generator = AdviceGenerator(cycle_data)
    advice = advice_generator.personalized_advice()
    return render_template('advice.html', advice=advice)

@app.route('/resources')
def resources():
    resource_provider = ResourceProvider()
    resources = resource_provider.get_resources()
    return render_template('resources.html', resources=resources)

if __name__ == "__main__":
    app.run(debug=True)
