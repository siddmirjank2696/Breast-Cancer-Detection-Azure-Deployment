# Importing the required libraries
import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, app, render_template


# Creating a Flask application
app = Flask(__name__)

# Loading the linear regression model
logistic_model = pickle.load(open("logistic_model.pkl", "rb"))

# Loading the scaler standardizer
scaler = pickle.load(open("scaler.pkl", "rb"))

# Loading the principal component vector space
pca = pickle.load(open("pca.pkl", "rb"))


# Creating a decorator to direct to the home page
@app.route("/")
def home():

    # Returning the home page
    return render_template("home.html")


# Creating a decorator to direct to the prediction page
@app.route("/predict", methods=["POST"])
def predict():

    # Retrieving the data from an HTML form
    numbers_string = request.form['numbers']

    # Splitting the numbers
    numbers_list = numbers_string.split(',')

    # Converting each number to a float using list comprehension
    float_numbers_list = [float(num) for num in numbers_list]
    
    # Standardizing the data
    final_input =  scaler.transform(np.array(float_numbers_list).reshape(1, 30))

    # Projecting unseen data onto same principal components
    final_input = pca.transform(final_input)

    # Displaying the final input
    print(final_input)

    # Predicting the output using the linar model
    output = logistic_model.predict(np.array(final_input).reshape(1, 2))[0]

    # Initializing an empty string
    pred_text = ""

    # Checking whether output is Malignant or Benign
    if(output == 1):
        pred_text = "Benign"

    elif(output == 0):
        pred_text = "Malignant"


    # Returning the output
    return render_template("home.html", prediction_text="The Tumor Is : {}".format(pred_text))


# Creating a main function
if __name__ == "__main__":

    # Allowing debugging of the app and hosting it on my local host at port 4001
    app.run(debug=True, host='0.0.0.0', port=4001)