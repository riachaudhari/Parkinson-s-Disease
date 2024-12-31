# -*- coding: utf-8 -*-
"""Parkinson's Disease.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WYrwsbTwRbVgLIhcwPVwaBb7NobOy3h4

**Importing dependencies**
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

"""**Data Collection and Analysis**"""

parkisons_data=pd.read_csv("/content/parkinsons.csv")

parkisons_data.head()

parkisons_data.shape

parkisons_data.info()

parkisons_data.isnull().sum()

parkisons_data.describe()

#distribution of target variable
parkisons_data['status'].value_counts()

"""0-> parkinsons negative

1-> parkinsons positive
"""

#grouping the data based on the target column(status)
# Exclude non-numeric columns and then group by 'status'
numeric_columns = parkisons_data.select_dtypes(include=['number'])
grouped_mean = numeric_columns.groupby(parkisons_data['status']).mean()

# Display the result
grouped_mean

"""**Data Preprocessing**"""

#Separating the features and target
X=parkisons_data.drop(columns=['name','status'],axis=1)
Y=parkisons_data['status']

print(X)

print(Y)

"""**Splitting datatset into train and test data**"""

X_train,X_test,Y_train,Y_test=train_test=train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""**Data Standardization**"""

scaler=StandardScaler()

scaler.fit(X_train)

X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

print(X_train)

"""**Model Training**

Support Vector Machine Model
"""

# SVC->Support Vector Classifier
  model=svm.SVC(kernel='linear')

#training the SVM model with training data
model.fit(X_train,Y_train)

"""**Model Evaluation**

Accuracy Score
"""

#Accuracy score on training data
X_train_prediction=model.predict(X_train)
training_data_accuracy=accuracy_score(Y_train,X_train_prediction)

print('Accuracy score of training data: ',training_data_accuracy)

X_test_prediction=model.predict(X_test)
test_data_accuracy=accuracy_score(Y_test,X_test_prediction)

print('Accuracy score of test data: ',test_data_accuracy)

"""**Building a predictive system**"""

input_data=(162.56800,198.34600,77.63000,0.00502,0.00003,0.00280,0.00253,0.00841,0.01791,0.16800,0.00793,0.01057,0.01799,0.02380,0.01170,25.67800,0.427785,0.723797,-6.635729,0.209866,1.957961,0.135242)

#changing input data to a numpy array
input_data_as_numpy_array=np.asarray(input_data)

#reshape the numpy array
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

#standardizing the data
np.std_data=scaler.transform(input_data_reshaped)

prediction=model.predict(np.std_data)
print(prediction)

if prediction[0]==0:
  print("The person does not have parkinson's disease")
else:
  print("The person has parkinson's disease")

input_data=(197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)
#changing input data to a numpy array
input_data_as_numpy_array=np.asarray(input_data)

#reshape the numpy array
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

#standardizing the data
np.std_data=scaler.transform(input_data_reshaped)

prediction=model.predict(np.std_data)
print(prediction)

if prediction[0]==0:
  print("The person does not have parkinson's disease")
else:
  print("The person has parkinson's disease")

