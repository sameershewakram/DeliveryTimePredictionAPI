#Import Libraries
## this library is for lodaing our already trained machine learning model
from sklearn.externals import joblib
from flask import Response, request
from webapp import app
import pandas as pd
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
        json_array = request.get_json()
        ## Convert json into pandas dataframe
        df = pd.DataFrame.from_dict(json_array)
        ## Now it's time to set the feature as we set during the model
        df['CreatedTime'] = pd.to_datetime(df['CreatedTime'])
        print(df['CreatedTime'])
        timestamp_into_int = df['CreatedTime'].values.astype(int)
        location_code = df[['LocationCode', 'PendingOrdersLocationWise', 'Qty']].values
        ## Create numpy array of inputs
        X = np.insert(location_code, 1,timestamp_into_int , axis=1)
        ## Load the saved model
        model = joblib.load(path+'/model1_dt.sav')
        ## Getting created time to add the predicted time in to it.
        time = df.iloc[0]['CreatedTime']
        ## Predicting the output
        predict_output = model.predict(X)
        ## Convert output into real minutes
        minutes = np.floor(np.multiply(np.subtract(np.multiply(predict_output,24), 
            np.floor(np.multiply(predict_output,24))),60))
        Organization_ID = df['OrganizationID']
        print(Organization_ID)
        hours = str(predict_output[0]).split('.')[0]
        minutes = str(minutes[0]).split('.')[0] 

        total_time = time + datetime.timedelta(hours=int(hours) , minutes=int(minutes))
        hour_min_days = total_time - time
        ## Setting up the json format for sending output in json 
        t1={ 
            'time_in_hours_and_minutes':str(hour_min_days),
            'time_with_date_and_time':str(total_time)
        }
        response = Response(json.dumps(t1))
        return response