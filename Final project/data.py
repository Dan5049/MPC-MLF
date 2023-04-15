import numpy as np
import pandas as pd
import glob

file_test = glob.glob("C:/Users/Dan/Documents/MLF/Dataset/Test/CSV/*.csv")
file_train = glob.glob("C:/Users/Dan/Documents/MLF/Dataset/Train/CSV/*.csv")
num_test = len(file_test)
num_train = len(file_train)

path_test = []
path_train = []
csv_test = []
csv_train = []

for i in range(num_test):
  path_test.append("C:/Users/Dan/Documents/MLF/Dataset/Test/CSV/img_%d.csv" %(i))

for j in range(num_train):
  path_train.append("C:/Users/Dan/Documents/MLF/Dataset/Train/CSV/img_%d.csv" %(j))

print("loading")

for file_test in path_test:
  csv_test.append(pd.read_csv(file_test))

for file_train in path_train:
  csv_train.append(pd.read_csv(file_train))

print("saving")

np.save("C:/Users/Dan/Documents/MLF/csv_test", csv_test)
np.save("C:/Users/Dan/Documents/MLF/csv_train", csv_train)

print("done")