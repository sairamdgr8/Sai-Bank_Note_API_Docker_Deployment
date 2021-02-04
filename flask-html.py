# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:23:08 2021

@author: Bunnyyyyyyy
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
app = Flask(__name__)
pickle_in=open('bank_note_authentication_classifier.pkl','rb') 
classifier=pickle.load(pickle_in)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        variance = float(request.form['variance'])
        skewness=float(request.form['skewness'])
        curtosis=float(request.form['curtosis'])
        entropy=float(request.form['entropy'])
        prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
        output=str(' '.join(map(str,
                prediction)))
        if(output=='0'):
            return render_template('index.html', prediction_text="This Bank Note is Authentic :" +" " +output  )
        else:
            return render_template('index.html', prediction_text="This Bank Note is Not Authentic : " + " "+output )
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)

