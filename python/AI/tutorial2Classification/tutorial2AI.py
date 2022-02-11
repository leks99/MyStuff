import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas
import numpy
from sklearn import linear_model, preprocessing

data = pandas.read_csv("car.data")

# pre processing (non numeric values to numeric)
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"])) # takes "buying" column and transforms values to numeric
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

predict = "class"

X = list(zip(buying, maint, door, persons, lug_boot, safety)) # makes one list from all the lists
Y = list(cls)

# takes lists from above and splits it in to test and train parts
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=9)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

predicted = model.predict(x_test)

for x in range(len(x_test)):
    print("predicted: ", predicted[x], "Data: ", x_test[x], "Actual: ", y_test[x])