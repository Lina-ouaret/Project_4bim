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


att_cluster1 = {"Male":-1,"Straight_Hair":-1,"Young":-1}
att_cluster2= {"Male":-1,"Straight_Hair":-1,"Young":1}
att_cluster3 = {"Male":-1,"Straight_Hair":1,"Young":1}
att_cluster4 = {"Male":1,"Straight_Hair":1,"Young":-1}
att_cluster5 = {"Male":1,"Straight_Hair":-1,"Young":1}
att_cluster6 = {"Male":1,"Straight_Hair":-1,"Young":-1}
att_cluster7 = {"Male":-1,"Straight_Hair":1,"Young":-1}
att_cluster8 = {"Male":1,"Straight_Hair":1,"Young":1}


df_attributes = cf.convert_attributes_into_pandas("attributes_data.csv")

index_cluster1 =cf.matrix_reduction(df_attributes,att_cluster1)
index_cluster2 =cf.matrix_reduction(df_attributes,att_cluster2)
index_cluster3 =cf.matrix_reduction(df_attributes,att_cluster3)
index_cluster4 =cf.matrix_reduction(df_attributes,att_cluster4)
index_cluster5 =cf.matrix_reduction(df_attributes,att_cluster5)
index_cluster6 =cf.matrix_reduction(df_attributes,att_cluster6)
index_cluster7 =cf.matrix_reduction(df_attributes,att_cluster7)
index_cluster8 =cf.matrix_reduction(df_attributes,att_cluster8)


#Upload pictures avec ckuster1
for k in range(len(index_cluster1)):
    images.append(glob.glob("img_align_celeba/"+index_cluster1[k]+".jpg")[0])
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
