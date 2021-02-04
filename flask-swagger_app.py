#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Mon Jan 25 05:32:27 2021

@author: Bunnyyyyyyy
"""

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger
import jsonify

app = Flask(__name__)  # # this is the satrt point of code
Swagger(app)
pickle_in = open('bank_note_authentication_classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


                 # # this is decorator of flask app which it creates a home page

@app.route('/')
def Home():
    return 'Sai Bank note authentication'


                                          # http://127.0.0.1:5000/predict?variance=-1.6677&skewness=-7.1535&curtosis=7.5&entropy=0.9

@app.route('/predict', methods=["Get"])
def predict_note_authentication():
    """Lets Authenticate the banks Note
    This is using docstrings for specifications.
    ---
    parameters:
        -name: variance
        in:query
        type: number
        requried: true
    responses:
        200:
            description: the outpput values
            
    """
    variance=request.args.get("variance")
    return variance

@app.route('/predict_file', methods=["POST"])
def predict_note_file_authentication():
    """Lets Authenticate the banks Note
    this is using docstrings for specifications.
    
    ---
    parameters:
        - name:file
          in:formData
          type:file
          requried:true
       
    responses:
        200:
            description : the output values
        
 
    """

    # variance=request.args.get('variance')
    # skewness=request.args.get('skewness')
    # curtosis=request.args.get('curtosis')
    # #entropy=request.args.get('entropy')

    df_test = \
        pd.read_csv(request.files.get('C://Users//SAI//machine_learining-use case Bank_Note_Authentication Dockerised Model//test_file.csv'
                    ))
    prediction = classifier.predict(df_test)
    return 'The prediction value is : ' + str(list(prediction))

if __name__ == '__main__':
    app.run()
