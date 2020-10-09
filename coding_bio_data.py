import pandas as pd 
import numpy as np
import math
X = pd.read_csv("AKSHANSH NAIN - shrub-volume-data.csv - AKSHANSH NAIN - shrub-volume-data.csv.csv")
print("Length col is :\n" ,X["length"])
X["Volume"]= X["length"]*X["width"]*X["height"]
print("Adding the volume column\n" , X)
X["Shrubs"] = 1.8 + 2 * np.log(X["Volume"])
print("Calculating shrubs\n" , X)
print("\nHeights greater than 5\n")
for i in X["height"]:
    if(i > 5):
        print(i)

data_means = X.group_by('site').mean()
data_means["height"]
X.groupby("site").max(["height"])
