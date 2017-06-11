
# coding: utf-8

# In[ ]:

import numpy as np
import time

from keras.models import Model
from keras.layers import *
from keras.optimizers import Adam
from keras.losses import sparse_categorical_crossentropy

# Data paths
data_path = 'data'

