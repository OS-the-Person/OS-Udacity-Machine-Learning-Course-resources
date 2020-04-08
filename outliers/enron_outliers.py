#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import math

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)#delete most obvious Outlier


features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



#loop through name : features for each employee
for key, value in data_dict.items():
    #if the bonus of each employee is equal max value in feature list

    if value["salary"] == data[0].max():
        print key
        
    if value["bonus"] == data[1].max():
        print key
    
    if value["salary"] >= 1000000 and not math.isnan(float(value["salary"])):
        if value["bonus"] >= 5000000 and not math.isnan(float(value["bonus"])):
            print key

