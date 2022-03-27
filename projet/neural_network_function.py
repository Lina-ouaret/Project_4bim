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
import cv2


## Split dataset definition

def split_dataset(dataset, attribut):
  '''
  Split the dataset into train and test, in order to train the neural network

  Args :
    pixel (array) : X, the photo represented by a 64x64 matrix, each element containing 3 values (a RGB-coded pixel)
    attributs (array) : Y, case Olivetti db : name of the photo, ex : 00000 ; 11111 ; 22222 etc

  Returns :
    X_train (array) : portion of the db used to train the neural network - input
    X_test (array) : portion of the db used to test the neural network - output
    Y_train (array) : portion of the db used to train the neural network - input
    Y_test (array) : portion of the db used to test the neural network - output

  >>>

  '''
  X_train, X_test, Y_train, Y_test = train_test_split(dataset, attribut, test_size=0.2, random_state=0)
  return X_train, X_test, Y_train, Y_test

## Model definition

def model(original_dim, hidden_encoding_dim, encoding_dim,
           dropout_level, hidden_decoding_dim):
  '''
  Model of neural network

  Args :
    original_dim (int) :
    hidden_encoding_dim (int) :
    encoding_dim (int) :
    dropout_level (float) :
    hidden_decoding_dim (int) :
  Returns :
    encoder (keras.engine.functional.Functional) :
    decoder (keras.engine.functional.Functional) :
    autoencoder (keras.engine.functional.Functional) :

  >>> type(encoder); type(decoder); type(autoencoder);
  <keras.engine.functional.Functional>
  >>> Verify that loss and val loss never reach 0:
      history = autoencoder.history.history
      for i in range(len(history['val_loss'])):
            if history['val_loss'][i]==0:
                print("test failed")
                break
      for i in range(len(history['loss'])):
            if history['loss'][i]==0:
                print("test failed")
                break
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
    j=i+1
    plt.savefig("son/"+str(j)+".png")

    img_=cv2.imread("son/"+str(j)+".png")
    img_2=cv2.resize(img_,(100,100))
    #print(img_2)
    cv2.imwrite('son/'+str(j)+'.png', img_2)

  return None


# Plot the learning curve to test the model
def loss_test(autoencoder):
    '''
    Save the input images and their reconstruction after being decoded

    Args :
        autoencoder(keras.engine.functional.Functional)
    Returns :
        None

    >>> epochs=300 #parameters of autoencoder_.fit(...)
        history['val_loss']==epochs
        <True>
        history['loss']==epochs
        <True>
    '''
    history = autoencoder.history.history
    plt.plot(history['val_loss'],label="test")
    plt.plot(history['loss'],label="training")
    plt.xlabel("epochs")
    plt.ylabel("Loss")
    plt.legend()
    return None
