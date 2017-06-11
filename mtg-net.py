
# coding: utf-8

# In[8]:

import numpy as np
import time

from keras.models import Sequential
from keras.layers import *

# Data paths
data_path = 'data/AllSets.json'

# Training Parameters
patience = 5  # Early Stopping (using validation macro recall)
minImprovement = 0.005
max_epochs = 100
batch_size = 256


# In[14]:

def build_model():
    '''Method for simply recreating the model when necessary (e.g. between validation folds)
    '''
    max_len = 150
    max_features = 1000
    
    model = Sequential()
    model.add(Embedding(max_features + 1, 128, input_length=max_len))
    model.add(LSTM(512, activation='tanh', recurrent_activation='hard_sigmoid', use_bias=True, 
                   kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', 
                   bias_initializer='zeros', unit_forget_bias=True, kernel_regularizer=None, 
                   recurrent_regularizer=None, bias_regularizer=None, activity_regularizer=None, 
                   kernel_constraint=None, recurrent_constraint=None, bias_constraint=None, 
                   dropout=0.2, recurrent_dropout=0.2, return_sequences=True))
    
    model.add(LSTM(512, activation='tanh', recurrent_activation='hard_sigmoid', use_bias=True, 
                   kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', 
                   bias_initializer='zeros', unit_forget_bias=True, kernel_regularizer=None, 
                   recurrent_regularizer=None, bias_regularizer=None, activity_regularizer=None, 
                   kernel_constraint=None, recurrent_constraint=None, bias_constraint=None, 
                   dropout=0.2, recurrent_dropout=0.2, return_sequences=True))
    
    model.add(LSTM(512, activation='tanh', recurrent_activation='hard_sigmoid', use_bias=True, 
                   kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', 
                   bias_initializer='zeros', unit_forget_bias=True, kernel_regularizer=None, 
                   recurrent_regularizer=None, bias_regularizer=None, activity_regularizer=None, 
                   kernel_constraint=None, recurrent_constraint=None, bias_constraint=None, 
                   dropout=0.2, recurrent_dropout=0.2, return_sequences=False))
    model.add(Dense(max_len, activation='softmax'))

    
    model.compile(optimizer='rmsprop',
                  loss='binary_crossentropy',
                  sample_weight_mode='None',
                  metrics=['accuracy'])
    
    return model

model = build_model()    
model.summary()

