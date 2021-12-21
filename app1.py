# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:14:28 2021

@author: PIJUSH_DAS
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    if request.method=='post':
        GENDER=request.form['GENDER']
        if(GENDER=='F'):
           GENDER=0
        elif(GENDER=='M'):
            GENDER=1
        INCOME_TYPE=request.form['INCOME_TYPE']
        if(INCOME_TYPE=='Commercial associate'):
            INCOME_TYPE=0
        elif(INCOME_TYPE=='Pensioner'):
            INCOME_TYPE=1
        elif(INCOME_TYPE=='State servant'):
            INCOME_TYPE=2
        elif(INCOME_TYPE=='Student'):
            INCOME_TYPE=3
        elif(INCOME_TYPE=='Working'):
            INCOME_TYPE=4
            
        CAR=request.form['CAR']
        if(CAR=='no'):
          CAR=0
        elif(CAR=='yes'):
          CAR=1
    
        EDUCATION_TYPE=request.form['EDUCATION_TYPE']
        if(EDUCATION_TYPE=='Academic degree'):
            EDUCATION_TYPE=0
        elif(EDUCATION_TYPE=='Higher education'):
            EDUCATION_TYPE=1
        elif(EDUCATION_TYPE=='Incomplete higher'):
            EDUCATION_TYPE=2
        elif(EDUCATION_TYPE=='Lower secondary'):
            EDUCATION_TYPE=3
        elif(EDUCATION_TYPE=='Secondary / secondary special'):
            EDUCATION_TYPE=4
    
        FAMILY_TYPE=request.form['FAMILY_TYPE']
        if(FAMILY_TYPE=='Civil marriage'):
            FAMILY_TYPE=0
        elif(FAMILY_TYPE=='Married'):
            FAMILY_TYPE=1
        elif(FAMILY_TYPE=='Separated'):
            FAMILY_TYPE=2
        elif(FAMILY_TYPE=='Single / not married'):
            FAMILY_TYPE=3
        elif(FAMILY_TYPE=='Widow'):
            FAMILY_TYPE=4
    
        HOUSE_TYPE=request.form['HOUSE_TYPE']
        if(HOUSE_TYPE=='Co-op apartment'):
            HOUSE_TYPE=0
        elif(HOUSE_TYPE=='House / apartment'):
            HOUSE_TYPE=1
        elif(HOUSE_TYPE=='Municipal apartment'):
            HOUSE_TYPE=2
        elif(HOUSE_TYPE=='Office apartment'):
            HOUSE_TYPE=3
        elif(HOUSE_TYPE=='Rented apartment'):
            HOUSE_TYPE=4
        elif(HOUSE_TYPE=='With parents'):
            HOUSE_TYPE=5
        
        REALITY=request.form['REALITY']
        if(REALITY=='Y'):
            REALITY=1
        else:
            REALITY=0
        
        E_MAIL=request.form['E_MAIL']
        if(E_MAIL=='Yes'):
            E_MAIL=0
        elif(E_MAIL=='no'):
            E_MAIL=1
        
        PHONE=request.form['PHONE']
        if(PHONE=='Yes'):
            PHONE=0
        elif(PHONE=='no'):
            PHONE=1
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='should be {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)