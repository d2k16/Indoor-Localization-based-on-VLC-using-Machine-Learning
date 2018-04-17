from rssical import *
import pandas as pd
import pickle
names = ['A', 'B','C','D','x','y']

dataset = pd.read_csv("rssi2.csv")

train_features,test_features, train_labels1,test_labels1=DataRd(dataset,names)
rf=RandPrd(train_features,train_labels1)
with open('E:/python/trainmod', 'wb') as f:
    pickle.dump(rf, f)
