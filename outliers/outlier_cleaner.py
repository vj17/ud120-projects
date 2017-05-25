#!/usr/bin/python
import numpy

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    ### your code goes here
    cleaned_data = [(ages[i], net_worths[i], predictions[i] - net_worths[i]) for i in range(len(ages))]
    return sorted(cleaned_data,key=lambda n:n[2])[:81]

