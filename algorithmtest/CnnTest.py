import numpy as np
np.random.seed(1337)

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Lambda
from keras.layers import Embedding
from keras.layers import Convolution1D, MaxPool1D, Flatten
from keras.datasets import imdb
from keras import backend as K

from sklearn.cross_validation import train_test_split
import pandas as pd
from keras.utils.np_utils import to_categorical

from sklearn.preprocessing import Normalizer
from keras.models import Sequential
from keras.layers import Convolution1D, Dense, Dropout, Flatten, MaxPooling1D
from keras.utils import np_utils
import numpy as np
import h5py
from keras import callbacks
from keras.layers import LSTM, GRU, SimpleRNN
from keras.callbacks import CSVLogger
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, CSVLogger

from preprocess import dataRead
from preprocess import digital


traindata = dataRead.corrected()
testdata = dataRead.full_data()

X = digital.contious_features(traindata)
Y = digital.ground_truth(traindata)
C = digital.contious_features(testdata)
T = digital.ground_truth(testdata)

Y_train = to_categorical(np.array(Y))
Y_test = to_categorical(np.array(T))

X = np.array(X)
C = np.array(C)
X_train = np.reshape(X, (X.shape[0],X.shape[1],1))
X_test = np.reshape(C, (C.shape[0],C.shape[1],1))

cnn = Sequential()
cnn.add(Convolution1D(64, 3, border_mode="same",activation="relu",input_shape=(38, 1)))
cnn.add(MaxPooling1D(pool_length=(2)))
cnn.add(Flatten())
cnn.add(Dense(128, activation="relu"))
cnn.add(Dropout(0.5))
cnn.add(Dense(38, activation="softmax"))

cnn.compile(loss="categorical_crossentropy", optimizer="adam",metrics=['accuracy'])

# cnn.fit(X_train, Y_train, epochs=1,validation_data=(X_test, Y_test))
#
# loss, accuracy = cnn.evaluate(X_test, Y_test)
#
# print("\nLoss: %.2f, Accuracy: %.2f%%" % (loss, accuracy*100))





























