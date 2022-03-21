import numpy as np                   # advanced math library
import matplotlib.pyplot as plt      # plotting routines
import keras
from keras.models import Model       # Model type to be used
from keras.layers.core import Dense, Dropout, Activation # Types of layers to be used in our model
from keras.utils import np_utils                         # NumPy related tools
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
from PIL.Image import *


## Split dataset definition

def split_dataset(dataset, attribut):
  '''
  Split the dataset into train and test

  Args :
    pixel (array) : X
    attributs (array) : y
  Returns :
    (array) : X_train
    (array) : X_test
    (array) : y_train
    (array) : y_test

  >>>

  '''
  X_train, X_test, y_train, y_test = train_test_split(dataset, attribut, test_size=0.2, random_state=0)
  return X_train, X_test, y_train, y_test

## Model definition

def model (original_dim, hidden_encoding_dim, encoding_dim,
           dropout_level, hidden_decoding_dim):
  '''
  Model of neural network

  Args :
    original_dim (int)
    hidden_encoding_dim (int)
    encoding_dim (int)
    dropout_level (float)
    hidden_decoding_dim (int)
  Returns :
    (keras.engine.functional.Functional) : encoder
    (keras.engine.functional.Functional) : decoder
    (keras.engine.functional.Functional) : autoencoder

  >>> type(encoder); type(decoder); type(autoencoder);
  <keras.engine.functional.Functional>
  >>> look the the learning curve
      the training and the loss curve tends to a low same constant

  '''
  # "encoded" is the encoded representation of the input
  input_img = keras.Input(shape=(original_dim,))
  hidden_encoded = Dense(hidden_encoding_dim, activation='relu')(input_img)
  dropout_hidden_encoded = Dropout(dropout_level)(hidden_encoded)
  encoded = Dense(encoding_dim, activation='relu')(dropout_hidden_encoded)
  dropout_encoded = Dropout(dropout_level)(encoded)

  # "decoded" is the reconstruction of the input
  hidden_decoded = Dense(hidden_decoding_dim, activation='relu')(dropout_encoded)
  dropout_hidden_decoded = Dropout(dropout_level)(hidden_decoded)
  decoded = Dense(original_dim, activation='sigmoid')(dropout_hidden_decoded)

  # This model maps an input to its reconstruction
  autoencoder = keras.Model(input_img, decoded)
  # This model maps an input to is encoded representation
  encoder = keras.Model(input_img, encoded)
  # This model maps an imput with the same dim as the encoded to the reconstruction
  input_encoded_img = keras.Input(shape=(encoding_dim,))
  hidden_decoder_layer = autoencoder.layers[-3]
  hidden_dropout_decoded_layer = autoencoder.layers[-2]
  decoder_layer = autoencoder.layers[-1]
  decoder = keras.Model(input_encoded_img, decoder_layer(hidden_dropout_decoded_layer(hidden_decoder_layer(input_encoded_img))))

  return encoder, decoder, autoencoder

  # Reconstruction plot definition

def save_reconstruction(n,decoded):
  '''
  Save the input images and their reconstruction after being decoded

  Args :
    decoded (array)
    n (int) : number of faces we will display
  Returns :
    None

  >>>

  '''
  for i in range(n):
    plt.imshow(decoded[i].reshape(64,64))
    plt.axis('off')
    plt.gray()
    plt.savefig("pictures_showed/img"+str(i)+".png")
  return None


# Plot the learning curve to test the model
def loss_test(autoencoder):
    '''
    Save the input images and their reconstruction after being decoded

    Args :
        autoencoder(keras.engine.functional.Functional)
    Returns :
        None

    >>>

    '''
    history = autoencoder.history.history
    plt.plot(history['val_loss'],label="test")
    plt.plot(history['loss'],label="training")
    plt.xlabel("epochs")
    plt.ylabel("Loss")
    plt.legend()
    return None
