# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 05:32:27 2021

@author: Bunnyyyyyyy
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
 
app=Flask(__name__) ## this is the satrt point of code
pickle_in=open('bank_note_authentication_classifier.pkl','rb') 
classifier=pickle.load(pickle_in)


@app.route('/')  ## this is decorator of flask app which it creates a home page
def Home():
    return "Sai Bank note authentication"
@app.route('/predict')    #http://127.0.0.1:5000/predict?variance=-1.6677&skewness=-7.1535&curtosis=7.5&entropy=0.9
def predict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction==1):
        return "The prediction value is  : "+ str(' '.join(map(str, prediction))) +" it means the Bank note the Authentic"
    else:
        return "The prediction value is  : "+ str(' '.join(map(str, prediction))) +" it means the Bank note the NOT Authentic"
        


## this is used to predict a input file using post method 
@app.route('/predict_file',methods=["POST"])
def predict_note_file_authentication():
    #variance=request.args.get('variance')
    #skewness=request.args.get('skewness')
    #curtosis=request.args.get('curtosis')
    ##entropy=request.args.get('entropy')
    df_test=pd.read_csv(request.files.get("C//Users//SAI//machine_learining-use case Bank_Note_Authentication Dockerised Model//test_file.csv"))
    prediction=classifier.predict(df_test)
    return "The prediction value is : "+ str(list(prediction))
    
     
    

 
 
 
 
 
 
 
 
 
if __name__=='__main__':
    app.run()