import matplotlib.pyplot as plt
import numpy as np
import os

class splitter:
    def __init__(self, filename, epochs, bias, act_mode):
        self.data_files = filename
        self.data_epochs = epochs
        self.data_bias = bias
        self.act_mode = act_mode

    def find_the_best(self, grid_params):
        counter = 0
        filenames = []
        max_comb=0
        max_val =0.0
        with open(self.data_files, "r") as file:

            for line in file:
                if self.act_mode == True:
                    line1 = line.split(";")
                else:
                    line1 = line.split(" ")
                if self.data_bias == 6:
                    buf = float(line1[4])
                else:
                    if self.data_bias == 4:

                        buf = float(line1[3])
                if buf > max_val:
                    max_comb = counter
                    max_val  = buf
                if line1[0] == str(self.data_epochs - 1):
                    counter += 1
        print("overall: " , counter, ", the best one: ", max_comb, ", max valid accuracy: ", max_val)
        line_count = 0
        params=""
        with open(grid_params, "r") as file:
            for line in file:
                if line_count == max_comb:
                    params=line
                line_count += 1
        print("params: ", params)
      #  "C:\Users\Anastasya\Desktop\сетки\функция активации\18_02_2024\model_classify_tf_flowers_resnet20_GridSearch_30-1block+feat4.csv"
#"C:\Users\Anastasya\Desktop\сетки\функция активации\18_02_2024\effNet_tf_flowers\model_classify_cifar_resnet20Grid_Search_30-1block+2x4.csv"
#"C:\Users\Anastasya\Desktop\сетки\функция активации\18_02_2024\effNet_tf_flowers\model_classify_oxford_iiit_pet_mobilenet5_Grid_Search_304.csv"
data = ["C:/Users/Anastasya/Desktop/сетки/функция активации/01_03_2024/model_classify_tf_flowers_resnet20_GridSearch_30-1block+feat4.csv",
"C:/Users/Anastasya/Desktop/сетки/функция активации/01_03_2024/model_classify_cifar_resnet20Grid_Search_30-1block+2x4.csv",
"C:/Users/Anastasya/Desktop/сетки/функция активации/01_03_2024/model_classify_oxford_iiit_pet_mobilenet5_Grid_Search_304.csv"]
epochs =[100,90,100]
for i in range(len(epochs)):
    print(data[i])
    t = splitter(data[i],epochs[i],4,True)
    t.find_the_best("C:/Users/Anastasya/Desktop/сетки/функция активации/18_02_2024/grid_search_params_trunc.txt")