import numpy as np
import pandas as pd
import glob

path_test = glob.glob("C:/Users/Dan/Documents/MLF/Dataset/Test/CSV/*.csv")
path_train = glob.glob("C:/Users/Dan/Documents/MLF/Dataset/Train/CSV/*.csv")

csv_test = []
csv_train = []

print("loading")

for file_test in path_test:
  csv_test.append(pd.read_csv(file_test))

for file_train in path_train:
  csv_train.append(pd.read_csv(file_train))

print("saving")

np.save("C:/Users/Dan/Documents/MLF/csv_test", csv_test)
np.save("C:/Users/Dan/Documents/MLF/csv_train", csv_train)

print("done")