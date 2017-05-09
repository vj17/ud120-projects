#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Print the no. of people in the data set
print "No. of people in the data set:",len(enron_data)

# Print the no. of features for each person
print "No. of features per person in the data set:",len(enron_data["SKILLING JEFFREY K"])

# No. of POI in the dataset
poi_count = 0
for person in enron_data:
	if enron_data[person]['poi'] == True:
		poi_count+=1
print "No. of POI in the dataset:",poi_count

# No. of POI in the ../final_project/poi_names.txt
file = open("../final_project/poi_names.txt","r")
poi_count1 = 0
for line in file:
	if "(n)" in line or "(y)" in line:
		poi_count1 += 1
			
print "No. of POI in the ../final_project/poi_names.txt:",poi_count1

# Total value of stocks belonging to James Prentice
print "Total value of stocks belonging to James Prentice:",enron_data["PRENTICE JAMES"]["total_stock_value"]

# No. of emails from Wesley Colwell to persons of interest
print "No. of emails from Wesley Colwell to persons of interest:",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# Total value of exercised stock options belonging to Jeffrey K Skilling
print "Total value of exercised stock options belonging to Jeffrey K Skilling:",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Highest money taken among Lay, Skilling and Fastow
emp_dict = {}
emp_dict["LAY KENNETH L"] = enron_data["LAY KENNETH L"]["total_payments"]
emp_dict["SILLING JEFFREY K"] = enron_data["SKILLING JEFFREY K"]["total_payments"]
emp_dict["FASTOW ANDREW S"] = enron_data["FASTOW ANDREW S"]["total_payments"]

max_value =  max(emp_dict.values())

#k = emp_dict.keys()[emp_dict.keys().index(max(emp_dict.values()))] 
#k,v = emp_dict.items()[emp_dict.items().index(max(emp_dict.values()))] 

for emp in emp_dict:
	if emp_dict[emp] == max_value:
		print "The highest money was taken by",emp,"which was",max_value
		break

# No. of people who have quantified salary and known email address
count_sal = 0
count_mail = 0
for person in enron_data:

	if enron_data[person]["salary"] != 'NaN':
		count_sal += 1

	if enron_data[person]["email_address"] != 'NaN':
		count_mail += 1

print "No. of people with a quanitified salary is:",count_sal
print "No. of people with an email address is:",count_mail

		
# Percentage of people who have NaN in their total_payments
count_nan = 0
for person in enron_data:
	if enron_data[person]["total_payments"] == 'NaN':
		count_nan += 1

print "Percentage of people who have NaN in their total_payments:",((count_nan)*100)/len(enron_data),"%"

# Percentage of POI who have NaN in their total_payments
count_nan_poi = 0
for person in enron_data:
	if enron_data[person]["poi"] == True and enron_data[person]["total_payments"] == 'NaN':
		count_nan_poi += 1

print "Percentage of POI who have NaN in their total_payments:",count_nan_poi/poi_count,"%"

# No. of persons who have NaN in their total_payments when 10 data points are added
count_plus10 = len(enron_data)+10
count_nan_plus10 = count_nan+10
print "No. of points in the dataset:",count_plus10, "and no. of points with NaN:",count_nan_plus10

# No. of POI in the dataset and no. of POI with total_payments as NaN when 10 data points are added
poi_count_plus10 = poi_count+10
count_nan_poi_plus10 = count_nan_poi+10
print "No. of POI in the dataset is:",poi_count_plus10,"and no. of POI with total_payments as NaN:",count_nan_poi_plus10
