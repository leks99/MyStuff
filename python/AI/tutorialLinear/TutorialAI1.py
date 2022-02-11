import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

# https://www.youtube.com/watch?v=1BYu65vLKdA&list=PLzMcBGfZo4-mP7qA9cagf68V06sko5otr&index=3

data = pd.read_csv("student-mat.csv", sep=";") # import data base
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]] # trim data base

predict = "G3"

X = np.array(data.drop([predict], axis=1)) # creates array of values without this what we want to predict
Y = np.array(data[predict]) # creates array of in this case G3 values

# takes arrays above and splits it in to test and train parts
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print(acc)

# save the model
with open("student-mat.pickle", "wb") as f: # open the file
    pickle.dump(linear, f) # dump model "linear" to the file

# load the model
pickle_in = open("student-mat.pickle", "rb") # opens the file with model
linear = pickle.load(pickle_in) # loads the model

p= "absences"
style.use("ggplot")
pyplot.scatter(data[p], data[predict])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()