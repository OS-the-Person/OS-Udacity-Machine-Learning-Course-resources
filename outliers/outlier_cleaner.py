#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    import numpy as np
    from math import floor
    import operator
    cleaned_data = []

    ### your code goes here
    
    #creating differences list
    reduc_pred = np.subtract(predictions, net_worths)
    
    arr = []
    #putting the diferences in a list
    for x in range(len(reduc_pred)):
        arr.append(reduc_pred[x][0])
    
    
    #list of tuples
    for i in range(len(arr)):
        test_tuple = (ages[i],net_worths[i], arr[i])
        cleaned_data.append(test_tuple)
    # how to sort list of tuples according to a a particular feature
    
    cleaned_data.sort(key = operator.itemgetter(2))
   
    #no of items to remove (the ten percent)
    ten_per = int(floor(0.1 * len(arr)))
    
    cleaned_data = cleaned_data[:-ten_per]
    return cleaned_data

