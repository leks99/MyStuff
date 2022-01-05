from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import pandas as pd
import pygame as pg
import matplotlib.pyplot as plt
#import tensorflow.compact.v2.feature_column as fc
import tensorflow_probability as tfp
import tensorflow as tf
from IPython.display import clear_output
from six.moves import urllib

tfd = tfp.distributions  # making a shortcut for later on
initial_distribution = tfd.Categorical(probs=[0.2, 0.8])
transition_distribution = tfd.Categorical(probs=[[0.5, 0.5],
                                                 [0.2, 0.8]])
observation_distribution = tfd.Normal(loc=[0., 15.], scale=[5., 10.])

# the loc argument represents the mean and the scale is the standard devitation

model = tfd.HiddenMarkovModel(
    initial_distribution=initial_distribution,
    transition_distribution=transition_distribution,
    observation_distribution=observation_distribution,
    num_steps=7)

mean = model.mean()

# due to the way TensorFlow works on a lower level we need to evaluate part of the graph
# from within a session to see the value of this tensor

# in the new version of tensorflow we need to use tf.compat.v1.Session() rather than just tf.Session()
with tf.compat.v1.Session() as sess:
  print(mean.numpy())
