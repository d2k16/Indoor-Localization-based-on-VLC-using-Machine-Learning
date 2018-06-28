
from randmtest2 import *
import pandas as pd
import pickle
names = ['A', 'B','C','D','X','Y','out']

dataset = pd.read_csv("rssi123.csv")
dataset.head()

train_features,test_features, train_labels,test_labels=DataRd(dataset,names)
rf=RandPrd(train_features,train_labels)
with open('E:/python/trainmodML', 'wb') as f:
    pickle.dump(rf, f)
