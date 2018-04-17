
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
np.random.seed(0)
names = ['A', 'B','C','D','x','y']

dataset = pd.read_csv("rssi2.csv")
##print('The shape of our features is:', dataset.shape)
#print(dataset.describe())
def DataRd(dataset,names):
    df=pd.DataFrame(dataset,columns=names)
    features = pd.get_dummies(df)
    labels1 = np.array(features['x'])
    labels2 = np.array(features['y'])
    features= features.drop('x', axis = 1)
    features= features.drop('y', axis = 1)
    feature_list = list(features.columns)
    features = np.array(features)
    train_features, test_features, train_labels1,test_labels1 = train_test_split(features, labels1,test_size = 0.25, random_state = 42)
    train_features, test_features, train_labelss2,test_labels2 = train_test_split(features, labels2,test_size = 0.25, random_state = 42)
    return train_features,test_features, train_labels1,test_labels1
    
##print('Training Labels Shape:', train_labels1.shape)
##print('Testing Features Shape:', test_features.shape)
##print('Testing Labels Shape:', test_labels1.shape)
##baseline_preds = test_features[:, feature_list.index('Voltage OF PD')]]

def RandPrd(train_features,train_labels1):
    from sklearn.ensemble import RandomForestRegressor
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 40)
    rf.fit(train_features, train_labels1)
    return rf
    #rf2 = RandomForestRegressor(n_estimators = 1000, random_state = 40)

#rf.fit(train_features, train_labels1)
     
    #.fit(train_features, train_labels2);
    #predictions = rf.predict(np.array([[30,37,6,17]]))
    #predictions2 = rf2.predict(np.array([[30,37,6,17]]))
  


