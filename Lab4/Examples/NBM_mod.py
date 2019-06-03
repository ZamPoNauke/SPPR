#Import Library of Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
import numpy as np

#assigning predictor and target variables
x = np.array([[0, 0, 0], [0, 0, -1], [0, -1, 0], [-1, 0, 0], [1, 0, 0], [1, 0, 1]])
Y = np.array([1, 2, 2, 1, 3, 3])

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(x, Y)

#Predict Output
predicted = model.predict([0, 0, 0])
print(predicted)

#Output: ([3,4])