from scipy.stats import ttest_ind

import numpy as np
import itertools
import operator

from scipy.stats import mannwhitneyu

AUTHOR_EMAIL = 'edvard88@inbox.ru'

def mean_conversion(index, conversion):
    
    l = list(zip(index,conversion))             
    it = itertools.groupby(l, lambda x: x[0])    
    data = []
    for key, subiter in it:
        data.append(np.mean([item[1] for item in subiter]))
    return data

def evaluate(
    train_conversions, 
    train_indices,
    test_conversions,
    test_indices
):


    #train_conversions = mean_conversion(train_indices, train_conversions)
    #test_conversions = mean_conversion(test_indices, test_conversions)
    
    train_conversions = np.bincount(train_indices, weights=train_conversions)/np.bincount(train_indices)
    test_conversions = np.bincount(test_indices, weights=test_conversions)/np.bincount(test_indices)


    #return mannwhitneyu(train_conversions, test_conversions, alternative='less').pvalue
    return ttest_ind(train_conversions, test_conversions, equal_var=False).pvalue
    #return ttest_ind(train_conversions - test_conversions, 0, equal_var=False).pvalue
    
    #return np.random.uniform()
