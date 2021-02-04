# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 09:12:30 2021

@author: Bunnyyyyyyy
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Mon Jan 25 05:32:27 2021

@author: Bunnyyyyyyy
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger
import jsonify
from flask_restx import Api,Resource,reqparse


app = Flask(__name__)  # # this is the satrt point of code
api=Api(app)
parser = reqparse.RequestParser()
pickle_in = open('bank_note_authentication_classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


                 # # this is decorator of flask app which it creates a home page

@api.route('/home')
class Hello(Resource):
    def get(self):
        return {'home':'Sai Bank note authentication'}
    
@api.route('/home2')
class Hello1(Resource):
    def get(abc):
        return {'home':abc}

@api.route('/var')
class Hello(Resource):
    def gett(**user_input):
        variance = user_input['variance']
        skewness = user_input['skewness']
        curtosis = user_input['curtosis']
        entropy = user_input['entropy']
        prediction = classifier.predict([[variance, skewness, curtosis,entropy]])
        return 'The prediction value is  : ' + str(' '.join(map(str,
                    prediction)))
        


                                          # http://127.0.0.1:5000/predict?variance=-1.6677&skewness=-7.1535&curtosis=7.5&entropy=0.9

@api.route('/predict')
class Hello(Resource):
    def get(self):
        variance = request.args.get('variance')
        skewness = request.args.get('skewness')
        curtosis = request.args.get('curtosis')
        entropy = request.args.get('entropy')
        prediction = classifier.predict([[variance, skewness, curtosis,
                                        entropy]])
        if prediction == 1:
            return 'The prediction value is  : ' + str(' '.join(map(str,
                    prediction))) + ' it means the Bank note the Authentic'
        else:
            return 'The prediction value is  : ' + str(' '.join(map(str,
                    prediction))) \
                + ' it means the Bank note the NOT Authentic'


## this is used to predict a input file using post method

@app.route('/predict_file', methods=['POST'])
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
    app.run(debug=True)
