# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:25:02 2020

@author: Jason
"""

import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
with open('Model_final_flask.pkl', 'rb') as f:
    model = pickle.load(f)
    
    
# initialize the flask app
app = flask.Flask(__name__)


# set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # rendering the initial form, to get input
        return(flask.render_template('ml.html'))
    
    if flask.request.method == 'POST':
        # extracting the input values
        premisetype = flask.request.form['premisetype']
        reportedyear = flask.request.form['reportedyear']
        reportedmonth = flask.request.form['reportedmonth']
        reportedday = flask.request.form['reportedday']
        reporteddayofweek = flask.request.form['reporteddayofweek']
        reportedhour = flask.request.form['reportedhour']
        same_day_reported = flask.request.form['same_day_reported']

        
        # converting input variables from user to values ML models can read
        
        def convert_premise(input):
            if input == 'Commercial':
                return 1
            elif input == 'Apartment':
                return 2
            elif input == 'House':
                return 3
            elif input == 'Outside':
                return 4
            else:
                return 5
            
        premisetype = convert_premise(premisetype)
        
        def convert_month(month):
            if month == 'January':
                return 1
            elif month == 'February':
                return 2
            elif month == 'March':
                return 3
            elif month == 'April':
                return 4
            elif month == 'May':
                return 5
            elif month =='June':
                return 6
            elif month == 'July':
                return 7
            elif month == 'August':
                return 8
            elif month == 'September':
                return 9
            elif month == 'October':
                return 10
            elif month == 'November':
                return 11
            else:
                return 12
        reportedmonth = convert_month(reportedmonth)
        
        def convert_dow(day):
            if day == 'Monday':
                return 1
            elif day == 'Tuesday':
                return 2
            elif day == 'Wednesday':
                return 3
            elif day == 'Thursday':
                return 4
            elif day == 'Friday':
                return 5
            elif day == 'Saturday':
                return 6
            else:
                return 7
        reporteddayofweek = convert_dow(reporteddayofweek)
        
        # making dataframe for model
        input_variables = pd.DataFrame([[premisetype, reportedyear, reportedmonth, reportedday, reporteddayofweek, reportedhour, same_day_reported]],
                                       columns=['premisetype', 'reportedyear', 'reportedmonth', 'reportedday', 'reporteddayofweek',
                                                'reportedhour','same_day_reported'],
                                       dtype=float,
                                       index=['input'])
        
        # get the model's prediction
        prediction = model.predict(input_variables)[0]
        
        # mapping output (float) to strings
        def convert(prediction):
            if prediction == 1:
                return 'Assault'
            elif prediction == 2:
                return 'Break and Enter'
            elif prediction == 3:
                return 'Robbery'
            elif prediction == 4:
                return 'Theft Over'
            else:
                return 'Auto Theft'
        output = convert(prediction)
        # render the form again, but add in the prediction and remind user of the values they input before
        return flask.render_template('ml.html',
                                     original_input={'premisetype':premisetype,
                                                     'reportedyear':reportedyear,
                                                     'reportedmonth':reportedmonth,
                                                     'reportedday':reportedday,
                                                     'reporteddayofweek':reporteddayofweek,
                                                     'reportedhour':reportedhour,
                                                     'same_day_reported':same_day_reported,
                                                     },
                                     result=(output)
                                     )
        
if __name__ == "__main__":
    app.run(debug=True)