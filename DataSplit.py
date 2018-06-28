

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle

names = ['A', 'B','C','D','x','y','out']
dataset = pd.read_csv("rssi123.csv")

def DataRd(dataset,names):
    df=pd.DataFrame(dataset,columns=names)
    features = pd.get_dummies(df)
    labels = np.array(features['out'])
    
    features= features.drop('X', axis = 1)
    features= features.drop('Y', axis = 1)
    features= features.drop('out', axis = 1)
    feature_list = list(features.columns)
    features = np.array(features)
    
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.30, random_state = 42)
    
    return train_features,test_features, train_labels,test_labels

def RandPrd(train_features,train_labels):
    from sklearn.ensemble import RandomForestRegressor
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 40)
    rf.fit(train_features, train_labels)
    
    return rf



