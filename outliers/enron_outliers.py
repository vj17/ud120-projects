#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

#Remove TOTAL outlier
data_dict.pop("TOTAL",0)

data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

"""max_salary = max(data[:,0])
for k,v in data_dict.items():
    if(v["salary"] == max_salary):
	print "Max salary",k
"""

#Print the max 2 outliers
max_salaries =  sorted(data[:,0],reverse=True)[:2]
print max_salaries
for k,v in data_dict.items():
    if v["salary"] in max_salaries:
	print k
