# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:17:12 2020

@author: anushka singh
"""
import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    for rendering results on HTML GUI

    Returns
    -------
    None.

    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    predictions = model.predict(final_features)
    
    output = round(predictions[0],2)
    
    return render_template('index.html', prediction_text = 'Medical Charges be {}'.format(output) )


if __name__ == "__main__":
    app.run(debug = True)
