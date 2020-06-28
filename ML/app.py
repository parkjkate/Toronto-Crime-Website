# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:25:02 2020

@author: Jason
"""

import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
with open(f'Model_final_flask.pkl', 'rb') as f:
    model = pickle.load(f)
    
    
# initialize the flask app
app = flask.Flask(__name__, template_folder='templates')


# set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # rendering the initial form, to get input
        return(flask.render_template('index.html'))
    
    if flask.request.method == 'POST':
        # extracting the input values
        reportedyear = flask.request.form['reportedyear']
        reportedday = flask.request.form['reportedday']
        reporteddayofyear = flask.request.form['reporteddayofyear']
        reportedhour = flask.request.form['reportedhour']
        same_day_reported = flask.request.form['same_day_reported']
        same_month_reported = flask.request.form['same_month_reported']
        same_year_reported = flask.request.form['same_year_reported']
        same_dow_reported = flask.request.form['same_dow_reported']
        same_hour_reported = flask.request.form['same_hour_reported']
        
        
        # making dataframe for model
        input_variables = pd.DataFrame([[reportedyear, reportedday, reporteddayofyear,reportedhour,same_day_reported,same_month_reported,same_year_reported,same_dow_reported,same_hour_reported]],
                                       columns=['reportedyear', 'reportedday', 'reporteddayofyear', 'reportedhour',
       'same_day_reported', 'same_month_reported', 'same_year_reported',
       'same_dow_reported', 'same_hour_reported'],
                                       dtype=float,
                                       index=['input'])
        
        # get the model's prediction
        prediction = model.predict(input_variables)[0]
        output = float(round(prediction, 2))
        
        # render the form again, but add in the prediction and remind user of the values they input before
        return flask.render_template('index.html',
                                     original_input={'reportedyear':reportedyear,
                                                     'reportedday':reportedday,
                                                     'reporteddayofyear':reporteddayofyear,
                                                     'reportedhour':reportedhour,
                                                     'same_day_reported':same_day_reported,
                                                     'same_month_reported':same_month_reported,
                                                     'same_year_reported',same_year_reported,
                                                     'same_dow_reported':same_dow_reported,
                                                     'same_hour_reported',same_hour_reported},
                                     result=float(output)
                                     )
        
if __name__ == "__main__":
    app.run(debug=True)