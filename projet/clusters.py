import numpy as np
import pandas as pd
import random
import common_functions as cf


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