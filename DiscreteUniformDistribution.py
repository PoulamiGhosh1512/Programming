#Importing packages
'''
Numpy:Contains functions for working in domain of linear algebra, fourier transform, and matrices.
Scipy:statistics module,Contains several functions for statistics and probability distributions.
Matplotlib:For visualization and plotting
'''
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

'''Discrete Uniform Distribution:Probability distribution in which all outcomes are equally likely
n=number of outcomes in the sample space'''
def uniform(n,m):
    return np.random.randint(1,n+1,size=m)

'''Example 1:Tossing a coin 100 times:1 indicates heads and 2 indicates tails'''
print('Coin Toss:',uniform(2,100))

'''Example 2:Rolling a die 100 times'''
print('Rolling an unbiased die:5',uniform(6,100))
