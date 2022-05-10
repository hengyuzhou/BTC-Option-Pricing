
import numpy as np
import math 
import time
from matplotlib import pyplot as plt
from math import log, sqrt, pi, exp
from scipy.stats import norm
from datetime import datetime, date
import numpy as np
import pandas as pd
from pandas import DataFrame

class OptionPricing:
    def __init__(self,S,K,T,r,sigma,iterations):
        self.S=S;
        self.K=K;
        self.T=T;
        self.r=r;
        self.sigma=sigma;
        self.iterations=iterations;
        
    def call_option_simulation(self):
        option_data=np.zeros([self.iterations,2]);
        rand=np.random.normal(0,1,[1,self.iterations]);
        stock_price=self.S*np.exp(self.T*(self.r-0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand);
        option_data[:,1]=stock_price-self.K;
        plt.plot(option_data);
        average=np.sum(np.amax(option_data,axis=1))/float(self.iterations);
        return np.exp(-1.0*self.r*self.T)*average;
    def put_option_simulation(self):
        option_data=np.zeros([self.iterations,2]);
        rand=np.random.normal(0,1,[1,self.iterations]);
        stock_price=self.S*np.exp(self.T*(self.r-0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand);
        option_data[:,1]=self.K-stock_price;
        #plt.plot(option_data);
        average=np.sum(np.amax(option_data,axis=1))/float(self.iterations);
        return np.exp(-1.0*self.r*self.T)*average;

if __name__=='__main__':
    S=43469.26; ###spot price
    K=44000;    ###Strike Price
    T=1/365;
    r=2.85;
    sigma=67.42;
    iterations=1000;
    
    model=OptionPricing(S,K,T,r,sigma,iterations);
    print(model.call_option_simulation());
    print(model.put_option_simulation());

