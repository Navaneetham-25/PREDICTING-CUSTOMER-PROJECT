# -*- coding: utf-8 -*-
"""Phase2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XtgHqef8qdABaDA8aaSXbjbe7jERLECz
"""

# Import required libraries
import numpy as np
import pandas as pd
from google.colab import files


uploaded = files.upload()


# Import the dataset
dataset = pd.read_csv('Naan mudhlvan Project.csv')

# Glance at the first five records
dataset.head()

# Print all the features of the data
dataset.columns

"""Code : To find the number of churners and non-churners in the dataset:"""

# Churners vs Non-Churners
dataset['Churn'].value_counts()

"""Code: To group data by Churn and compute the mean to find out if churners make more customer service calls than non-churners:"""

# Group data by 'Churn' and compute the mean
print(dataset.groupby('Churn')['Customer service calls'].mean())

"""Code: To find out if one State has more churners compared to another."""

# Count the number of churners and non-churners by State
print(dataset.groupby('State')['Churn'].value_counts())

"""Exploring Data Visualizations : To understand how variables are distributed"""

# Import matplotlib and seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Visualize the distribution of 'Total day minutes'
plt.hist(dataset['Total day minutes'], bins = 100)

# Display the plot
plt.show()

"""Code: To visualize the difference in Customer service calls between churners and non-churners"""

# Create the box plot
sns.boxplot(x = 'Churn',
			y = 'Customer service calls',
			data = dataset,
			# sym = "",	Remove or replace sym with flierprops for customization
			hue = "International plan",
            flierprops={'marker': ''}) # This will hide the outliers. You can change the marker style if needed.
# Display the plot
plt.show()

"""In telco churn data, Churn, Voice mail plan, and, International plan, in particular, are binary features that can easily be converted into 0’s and 1’s."""

# Features and Labels
X = dataset.iloc[:, 0:19].values
y = dataset.iloc[:, 19].values # Churn

# Encoding categorical data in X
from sklearn.preprocessing import LabelEncoder

labelencoder_X_1 = LabelEncoder()
X[:, 3] = labelencoder_X_1.fit_transform(X[:, 3])

labelencoder_X_2 = LabelEncoder()
X[:, 4] = labelencoder_X_2.fit_transform(X[:, 4])

# Encoding categorical data in y
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

"""Code: Encoding State feature using One hot encoding"""

# Removing extra column to avoid dummy variable trap
X_State = pd.get_dummies(X[:, 0], drop_first = True)

# Converting X to a dataframe
X = pd.DataFrame(X)

# Dropping the 'State' column
X = X.drop([0], axis = 1)

# Merging two dataframes
frames = [X_State, X]
result = pd.concat(frames, axis = 1, ignore_index = True)

# Final dataset with all numeric features
X = result

"""Code : To Create Training and Test sets"""

# Splitting the dataset into the Training and Test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""Code: To scale features of the training and test sets"""

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""Code: To train a Random Forest classifier model on the training set."""

# Import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

# Instantiate the classifier
clf = RandomForestClassifier()

# Fit to the training data
clf.fit(X_train, y_train)

"""Code : Making Predictions"""

# Predict the labels for the test set
y_pred = clf.predict(X_test)

"""Code: Evaluating Model Performance"""

# Compute accuracy
from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_pred)

"""Code : Confusion Matrix"""

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))