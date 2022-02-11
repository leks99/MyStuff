from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
import pygame as pg
import matplotlib.pyplot as plt
#import tensorflow.compact.v2.feature_column as fc
import tensorflow as tf
from IPython.display import clear_output
from six.moves import urllib

dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
                       'embark_town', 'alone']
NUMERIC_COLUMNS = ['age', 'fare']

featureColumns = []
for fname in CATEGORICAL_COLUMNS:
    voc = dftrain[fname].unique()
    featureColumns.append(tf.feature_column.categorical_column_with_vocabulary_list(fname, voc))

for fname in NUMERIC_COLUMNS:
    featureColumns.append(tf.feature_column.numeric_column(fname, dtype=tf.float32))

def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():  # inner function, this will be returned
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))  # create tf.data.Dataset object with data and its label
    if shuffle:
      ds = ds.shuffle(1000)  # randomize order of data
    ds = ds.batch(batch_size).repeat(num_epochs)  # split dataset into batches of 32 and repeat process for number of epochs
    return ds  # return a batch of the dataset
  return input_function  # return a function object for use

train_input_fn = make_input_fn(dftrain, y_train)  # here we will call the input_function that was returned to us to get a dataset object we can feed to the model
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)

linear_est = tf.estimator.LinearClassifier(feature_columns=featureColumns)

linear_est.train(train_input_fn)  # train
result = linear_est.evaluate(eval_input_fn)  # get model metrics/stats by testing on tetsing data

clear_output()  # clears consoke output
print(result['accuracy'])  # the result variable is simply a dict of stats about our model

result = list(linear_est.predict(eval_input_fn))
print(dfeval.loc[100])
print(result[100]['probabilities'][1])

