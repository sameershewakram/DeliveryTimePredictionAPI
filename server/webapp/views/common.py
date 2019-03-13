#Import Libraries
## this library is for lodaing our already trained machine learning model
from sklearn.externals import joblib
from flask import Response, request
from webapp import app
import numpy as np
import datetime
import json
import os

## Creating the routes where '/model' is called endpoint the one which you see in url 
## like www.google.com/search in our case 'localhost:5000/model'
## since this is post method, you can use postman to test your inputs.
@app.route('/model',methods = ['POST', 'GET'])
def model():
    ## checking if method is 'post' or not if it's not then it will give you error.
    path = os.path.join(os.getcwd(), os.getcwd()+'/webapp/model')
    print(path)
    if request.method == "POST":
        ## Recieve input in Json format which is coming from POSTMAN request
        data = request.get_json()
        ## Convert json into pandas dataframe
        print (np.array([data['variance'],data['skewness'],data['curtosis'],data['entropy']]))
        ## Create numpy array of inputs
        X = np.array([[data['variance'],data['skewness'],data['curtosis'],data['entropy']]])
        ## Load the saved model
        model = joblib.load(path+'/banknote_trained_model.sav')
        ## Predicting the output
        predict_output = model.predict(X)
        ## Set response
        print(predict_output)
        response = Response(json.dumps({'output':str(predict_output[0])}))
        return response