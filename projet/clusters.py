import numpy as np
import pandas as pd
import random
import common_functions as cf
import sys
from matplotlib import image
from matplotlib import pyplot
from PIL.Image import *
import glob
from skimage import io, transform
import skimage
from tensorflow import keras
from sklearn.model_selection import train_test_split
import neural_network_function as nn


att_cluster1 = {"Male":-1,"Straight_Hair":-1,"Young":-1}
# att_cluster2= {"Male":-1,"Straight_Hair":-1,"Young":1}
# att_cluster3 = {"Male":-1,"Straight_Hair":1,"Young":1}
# att_cluster4 = {"Male":1,"Straight_Hair":1,"Young":-1}
# att_cluster5 = {"Male":1,"Straight_Hair":-1,"Young":1}
# att_cluster6 = {"Male":1,"Straight_Hair":-1,"Young":-1}
# att_cluster7 = {"Male":-1,"Straight_Hair":1,"Young":-1}
# att_cluster8 = {"Male":1,"Straight_Hair":1,"Young":1}


df_attributes = cf.convert_attributes_into_pandas("attributes_data.csv")

index_cluster1 =cf.matrix_reduction(df_attributes,att_cluster1)
# index_cluster2 =cf.matrix_reduction(df_attributes,att_cluster2)
# index_cluster3 =cf.matrix_reduction(df_attributes,att_cluster3)
# index_cluster4 =cf.matrix_reduction(df_attributes,att_cluster4)
# index_cluster5 =cf.matrix_reduction(df_attributes,att_cluster5)
# index_cluster6 =cf.matrix_reduction(df_attributes,att_cluster6)
# index_cluster7 =cf.matrix_reduction(df_attributes,att_cluster7)
# index_cluster8 =cf.matrix_reduction(df_attributes,att_cluster8)


#Upload pictures avec ckuster1
images=[]
for k in range(len(index_cluster1)):
    images.append(glob.glob("/media/cloisel/SAMSUNG/projet4BIM/img_align_celeba/"+index_cluster1[k]+".jpg")[0])
i=0
n=len(images)
img=[None]*n
image_size=(128,128)
for image_ in images:
    picture = pyplot.imread(image_)
    img[i] = transform.resize(picture, image_size)
    i+=1
dataset=[None]*n
for j in range(n):
    dataset[j]=np.reshape(np.asarray(img[j]),(128*128*3))
data=np.array(dataset)

del images
del index_cluster1
del att_cluster1
del dataset


#Upload data
y = cf.convert_attributes_into_pandas("attributes_data.csv")
y = y.drop('ID', axis=1)
y = y.to_numpy()
Y=y[0:700]
del y
#y=y[0:2000]
X=data[0:700]

del data

# Split the dataset
(X_train_, X_test_, y_train_, y_test_) = nn.split_dataset(X, Y)

#input_shape = (128,128,3)
image_size    = (128,128)
lx,ly      = image_size
encoded_dim = 1000

input_img    = keras.Input(shape=(lx, ly, 3))
#x = keras.layers.Conv2D(64, 3,strides=2,activation='relu', padding='same')(input_img)
#x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
x = keras.layers.Conv2D(32, 3, activation='relu', padding='same')(input_img)
x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
#x = keras.layers.Dropout(0.2)(x)
x = keras.layers.Conv2D(16, 3, activation='relu', padding='same')(x)
x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
#x = keras.layers.Dropout(0.2)(x)
x = keras.layers.Conv2D(8, 3, activation='relu', padding='same')(x)
x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
#x = keras.layers.Flatten()(x)
#encoded = keras.layers.Dense(encoded_dim,activation='relu')(x)
encoded = keras.layers.Flatten()(x)

# at this point the representation is (4, 8, 8) i.e. 256-dimensional
#x = keras.layers.Dense(128,"relu")(encoded)
#x = keras.layers.Dense(2048,"relu")(encoded)  #meriem
#x = keras.layers.Dense(4*4*8,"relu")(x)
#x = keras.layers.Reshape((4,4,8))(x)
x = keras.layers.Reshape((16,16,8))(encoded) #meriem
#x = keras.layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x)
#x = keras.layers.UpSampling2D((2, 2))(x)
#x = keras.layers.Dropout(0.2)(x)
x = keras.layers.Conv2D(8, (3, 3), activation='relu', padding='same')(x) #meriem
x = keras.layers.UpSampling2D((2, 2))(x)  #meriem
#x = keras.layers.Dropout(0.2)(x)
x = keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same')(x)
x = keras.layers.UpSampling2D((2, 2))(x)
#x = keras.layers.Dropout(0.2)(x)
x = keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = keras.layers.UpSampling2D((2, 2))(x)
#x = keras.layers.Dropout(0.2)(x)
#x = keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
#x = keras.layers.UpSampling2D((2, 2))(x)
#x = keras.layers.Dropout(0.2)(x)
#x = keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same')(x)
#x = keras.layers.UpSampling2D((2, 2))(x)
decoded = keras.layers.Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = keras.Model(input_img, decoded)
encoder = keras.Model(input_img, encoded)
decoder = keras.Model(encoded, decoded)

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

autoencoder.summary()

X_train = X_train_.reshape(-3,128,128,3)
X_test = X_test_.reshape(-3,128,128,3)

autoencoder.fit(X_train, X_train,
                epochs=100,  #100
                batch_size=1,  #32
                shuffle=True,
                validation_data=(X_test, X_test))

history = autoencoder.history.history

pyplot.plot(history['val_loss'],label="test")
pyplot.plot(history['loss'],label="training")
pyplot.xlabel("epochs")
pyplot.ylabel("Loss")
pyplot.legend()

encoded_imgs = encoder.predict(X_test)

#save encoded imgs
np.save('encoded_imgs', encoded_imgs)
#np.save('decoded_imgs', decoded_imgs)

#decoded_imgs = autoencoder.predict(X_test)
decoded_imgs = decoder.predict(encoded_imgs)

# Use Matplotlib (don't ask)
import matplotlib.pyplot as plt

n = 10  # How many faces we will display
plt.figure(figsize=(20, 4))
for i in range(n):
    # Display original
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(X_test[i].reshape(128, 128,3))
    #plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Display reconstruction
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(128, 128,3))
    #plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
