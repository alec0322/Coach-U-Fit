# **Coach-U-Fit**

Linear regression, Python based machine learning model that predicts the number of calories 
consumed by a user depending on both exercise and macronutrient input data. 🥪 🍎

## Datasets

Two datasets are used for the implementation of Coach-U-Fit.

### Calories Burned During Exercise and Activities (CBDEA) 🏋🏼‍♂️

Created by Kaggle user Aadhav Vignesh, the CBDEA dataset is used to provide Coach-U-Fit
users with a variety of workouts to choose from. It contains calorie expenditure information
of exactly 992 activities, exercises, and sports. It is titled 'exercise_dataset.csv' in the zip file.
Available: https://www.kaggle.com/datasets/aadhavvignesh/calories-burned-during-exercise-and-activities

### Nutritional Facts for Most Common Foods (NFMCF) 🍔

Created by Kaggle user Niharika Pandit, the NFMCF dataset is used to train and test Coach-U-Fit. 
It contains the number of calories in 329 popular food items alongside their protein, carbohydrate,
fat, saturated fat, and fiber content. It is titled 'nutrients.csv' in the zip file.
Available: https://www.kaggle.com/datasets/niharika41298/nutrition-details-for-most-common-foods

*Note that in this case the dataset was manually altered after download, **using the 'nutrients.csv'
in the zip file is highly recommended.**

## Libraries and Frameworks

### Streamlit 💻

Open-source Python library that facilitates the creation of custom web applications. Although not
necessary for the implementation of a machine learning model, it greatly enhances user experience
and simplifies the inputting of data.

### Pandas 🐼

Open-source Python library for data manipulation and analysis. It contains a variety of data structures
and operations for working with structured data, such as SQL tables, spreadsheets, or, in Coach-U-Fit's
case, .csv files.

All forms of data manipulation, cleaning, and transformation of both datasets was performed using pandas.

### Scikit-Learn 📈

Open-source machine learning Python library designed to facilitate the implementation of machine learning
models, evaluation metrics, and much more. It is easy to use alongside other data manipulation libraries 
such as Pandas as it built on top of NumPy, SciPy, and Matplotlib.

## Instructions

The complete implementation of both the web application and the regression model can be found in the
'coachufit.py' Python file. The following steps detail how to properly run the file:

* Make sure that all files in coachufit.zip are extracted to the same directory
* The '.vscode' directory contains a variety of .json run paths used to properly set up the Streamlit web app
    * Note that the code was written using VS Code, using it for your own implementation is highly recommended
* Open the directory through VS Code, open 'coachufit.py', and go to VS Code's "Run and Debug" tab
* In the top left, press the green start icon titled: "Python: Module"
    * Doing this will point to the previously mentioned run paths in the '.vscode' directory
* Finally, the streamlit app will run on localhost on your preferred web browser

