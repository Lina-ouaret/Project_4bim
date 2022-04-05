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

  >>> run the program code "testunitairedataplit"

  '''
  X_train, X_test, Y_train, Y_test = train_test_split(dataset, attribut, test_size=0.2, random_state=0)
  return X_train, X_test, Y_train, Y_test

## Model definition

def model():
  '''
  Model of neural network

  Args :
  Returns :
    encoder (keras.engine.functional.Functional) :
    decoder (keras.engine.functional.Functional) :
    autoencoder (keras.engine.functional.Functional) :

  >>> type(encoder); type(decoder); type(autoencoder);
  <keras.engine.functional.Functional>
  >>> #Verify that loss and val loss never reach 0:
  >>> history = autoencoder.history.history
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
     #input_shape = (128,128,3)
     image_size    = (128,128)
     lx,ly      = image_size
     encoded_dim = 1000
     input_img    = keras.Input(shape=(lx, ly, 3))
     # #input_img = keras.Input(shape=input_shape)
     # x = keras.layers.Conv2D(128, 3,strides=2,activation='relu', padding='same')(input_img)
     # x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
     # x = keras.layers.Dropout(0.2)(x)
     # x = keras.layers.Conv2D(64, 3,strides=2,activation='relu', padding='same')(x)
     # x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
     # x = keras.layers.Dropout(0.2)(x)
     # x = keras.layers.Conv2D(32, 3, activation='relu', padding='same')(x)
     # x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
     # x = keras.layers.Dropout(0.2)(x)
     # x = keras.layers.Conv2D(16, 3, activation='relu', padding='same')(x)
     # x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
     # x = keras.layers.Dropout(0.2)(x)
     # x = keras.layers.Conv2D(8, 3, activation='relu', padding='same')(x)
     # x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
     # x = keras.layers.Dropout(0.2)(x)
     # x = keras.layers.Flatten()(x)
     # x = keras.layers.Dense(128,"relu")(x)
     # encoded = keras.layers.Dense(encoded_dim,activation='relu')(x)
     #
     # # "decoded" is the reconstruction of the input
     # # at this point the representation is (4, 8, 8) i.e. 256-dimensional
     # x = keras.layers.Dense(128,"relu")(encoded)
     # x = keras.layers.Dense(4*4*8,"relu")(x)
     # x = keras.layers.Reshape((4,4,8))(x)
     # x = keras.layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x)
     # x = keras.layers.UpSampling2D((2, 2))(x)
     # x = keras.layers.Dropout(0.2)(x)
     # x = keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same')(x)
     # x = keras.layers.UpSampling2D((2, 2))(x)
     # x = keras.layers.Dropout(0.2)(x)
     # x = keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
     # x = keras.layers.UpSampling2D((2, 2))(x)
     # x = keras.layers.Dropout(0.2)(x)
     # x = keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
     # x = keras.layers.UpSampling2D((2, 2))(x)
     # x = keras.layers.Dropout(0.2)(x)
     # x = keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
     # x = keras.layers.UpSampling2D((2, 2))(x)
     # decoded = keras.layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

     #input_img = keras.Input(shape=input_shape)
     input_img    = keras.Input(shape=(lx, ly, 3))
     x = keras.layers.Conv2D(32, 3, activation='relu', padding='same')(input_img)
     x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
     x = keras.layers.Conv2D(16, 3, activation='relu', padding='same')(x)
     x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
     x = keras.layers.Conv2D(8, 3, activation='relu', padding='same')(x)
     x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
     encoded = keras.layers.Flatten()(x)

     # "decoded" is the reconstruction of the input
     # at this point the representation is (16, 16, 8) i.e. 2048-dimensional
     x = keras.layers.Reshape((16,16,8))(encoded)
     x = keras.layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x) #meriem
     x = keras.layers.UpSampling2D((2, 2))(x)
     x = keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same')(x)
     x = keras.layers.UpSampling2D((2, 2))(x)
     x = keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
     x = keras.layers.UpSampling2D((2, 2))(x)
     decoded = keras.layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

     # This model maps an input to its reconstruction
     autoencoder = keras.Model(input_img, decoded)
     # This model maps an input to is encoded representation
     encoder = keras.Model(input_img, encoded)
     # This model maps an imput with the same dim as the encoded to the reconstruction
     decoder = keras.Model(encoded, decoded)

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

  >>> run the program code "testunitairecontrolplot"

  '''
  for i in range(n):
    plt.imshow(decoded[i].reshape(128, 128,3))
    plt.axis('off')
    #plt.gray()
    j=i+1
    plt.savefig("son/"+str(j)+".png")
    img_=cv2.imread("son/"+str(j)+".png")
    img_2=cv2.resize(img_,(128,128))
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

    >>> epochs=100 #parameters of autoencoder_.fit(...)
    >>> history['val_loss']==epochs
    <True>
    >>> history['loss']==epochs
    <True>
    '''
    history = autoencoder.history.history
    plt.plot(history['val_loss'],label="test")
    plt.plot(history['loss'],label="training")
    plt.xlabel("epochs")
    plt.ylabel("Loss")
    plt.legend()
    return None


#################
#TESTS UNITAIRES#
#################

if __name__ == "__main__" :
    import doctest
    doctest.testmod(verbose = True)
