from keras.models import Sequential
from keras.layers import Dense, Activation
from keras import backend as K


model = Sequential([Dense(32, units=784), Activation('relu'), Dense(10), Activation('softmax')])


def mean_pred(y_true, y_pred):
    return K.mean(y_pred)


model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy', mean_pred])


