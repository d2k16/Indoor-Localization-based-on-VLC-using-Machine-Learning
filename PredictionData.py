from TrainRssi import *
with open('E:/python/trainmod', 'rb') as f:
    rf = pickle.load(f)
##train_features= pd.read_csv("train_features.csv")
##train_labels1 = pd.read_csv("train_labels1.csv")
##rf.fit(train_features, train_labels1)
predictions = rf.predict(np.array([[30,37,6,17]]))
print(predictions)
