Question 1
1.1 Using examples differentiate between classification and regression.(5)

 1.2. Describe when you would prefer median imputation instead of mean imputation.(5)

1.3 List FIVE (5) Python Machine Learning libraries.(5)

1.4 Describe using an example the bias-variance trade-off in Machine Learning.(5)

Q2

2.1. How can a dataset without the target variable be utilized into supervised learning algorithms? (5)

2.2 Write Python code snippet to show  how to standardize a numeric feature called Age which is part of a dataframe, df using StandardScaler from sklearn.preprocessing (5)

2.3  Using examples, differentiate between model overfitting and underfitting.  Describe in detail FOUR (four) ways to mitigate each of these problems.  (10)

2.4 write the formular for accuracy, precision, recall, F1-score, and specificity. Calculate the following performance metrics: accuracy, precision, recall, F1-score, and specificity.(10)

Predicted Positive

Predicted Negative

Actual Positive

40

10

Actual Negative

20

30


Question 3

3.1 Use Table 3.1  to answer the following questions:

Table 3.1
| square_footage | num_bedrooms | age | location  | price   |
|----------------|-------------|-----|-----------|---------|
| 800            | 2           | 10  | Urban     | 350000  |
| 1200           | 3           | 5   | Suburban  | 245000  |
| 1500           | 4           | 10  | Urban     | 400000  |
| 1800           | 3           | 20  | Urban     | 300000  |
| 2500           | 4           | 7   | Rural     | 200000  |
| 900            | 2           | 25  | Urban     | 250000  |
| 1100           | 5           | 15  | Suburban  | 320000  |
| 2200           | 4           | 17  | Rural     | 280000  |

square_footage is the area of the house in square feet.

num_bedrooms is the number of bedrooms.

age is the age of the house in years.

location is the location of the which is Urban, Suburban or Rural.

price is the cost of the house in ZAR (rand).

Using the following imported libraries:

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score

from sklearn.preprocessing import LabelEncoder

Each question has a weighting of 5 marks.

(a )Write Python code snippet to load the houses data in a dataframe

(b) Write a Python code snippet to separate independent features/attributes and a target feature (price).                                                                                                                   

 

(c) Write a Python code snippet to apply label-encoding (one-hot encoding) to the location column. 

                                                                                                                           

(d) Write a Python code snippet to split the dataset into 80% train and 20% test.

(e) Write a Python code snippet to train a linear regression model (using the test dataset) and predict the house price of a house with 2000 square_footage, num_bedrooms: 5, age: 5 and location:  Urban.                                        

# question 4
4.1 Write a pseudo code/ algorithm for the K-means clustering algorithm.(10)

4.2   Explain why accuracy is not always the ideal metric for model evaluation (5)

 4.3 Use Table 4.3 to answer the following questions:  

  Table 4.3

| age | blood_pressure | cholesterol | has_disease |
|-----|----------------|-------------|-------------|
| 40  | 120            | 200         | 0           |
| 55  | 140            | 210         | 1           |
| 60  | 130            | 250         | 0           |
| 45  | 135            | 240         | 1           |
| 50  | 142            | 190         | 0           |
| 35  | 110            | 180         | 0           |
| 70  | 160            | 260         | 1           |
| 65  | 150            | 210         | 1           |
| 54  | 138            | 225         | 0           |
| 75  | 170            | 280         | 1           |



·         age: Patient age (years).

·         blood_pressure: Systolic blood pressure (mmHg)

·         cholesterol: Serum cholesterol level (mg/dL)

·         has_disease: Binary target indicating if the patient has the disease (1 = yes, 0 = no)

Complete the following code to show a Python code snippet to train the decision tree and logistic regression models for making predictions.

import pandas as pd

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import classification_report, confusion_matrix

 

# Load the data in the dataframe

data = {

    "age": [40, 55, 60, 45, 50, 35, 70, 65, 54, 75],

    "blood_pressure": [120, 140, 130, 135, 142, 110, 160, 150, 138, 170],

    "cholesterol": [200, 210, 250, 240, 190, 180, 260, 210, 225, 280],

    "has_disease": [0, 1, 0, 1, 0, 0, 1, 1, 0, 1]

}

df = pd.DataFrame(data)

 

# Split into features (X) and target (y)

X = df[["age", "blood_pressure", "cholesterol"]]

y = df["has_disease"]

 

 

# Dataset split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

 # Code for training the Decision tree and make predictions (5)

……………………………………………………

# Code for training the Logistic regression  and make predictions                                                 (5)
