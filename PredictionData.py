import pandas as pd
names = ['A', 'B','C','D','X','Y','out']
dataset = pd.read_csv("rssi123.csv")
import numpy as np
df=pd.DataFrame(dataset,columns=names)
features = pd.get_dummies(df)
features= features.drop('out', axis = 1)
features= features.drop('X', axis = 1)
features= features.drop('Y', axis = 1)
features = np.array(features)

dataset=np.array(dataset)
out1=dataset[:,6]
x1=dataset[:,4]
y11=dataset[:,5]

out1=out1.tolist()
x1=x1.tolist()
y11=y11.tolist()
                                                              #Serial imported for Serial communication
import time

import cmath
#import least square con.py
import matplotlib.pyplot as plt
from xlwt import Workbook
from scipy import signal
import scipy as sp
start=time.time()
#a=[]
co=0
i=0
Mn=0
Ln=0
cu=0

#Required to use delay functions
import serial
ArduinoUnoSerial = serial.Serial('com9',115200)       #Create Serial port object called ArduinoUnoSerialData time.sleep(2)                                                             #wait for 2 secounds for the communication to get established
#ArduinoUnoSerial.open()
 
while(True):
    #mydata=(ArduinoUnoSerial.readline().strip())
    #print(mydata.decode('utf-8'))
    H2=[7000]
    H=[]
    L=[]
    M=[]
    N=[]
    P=[]
    i=0
        
    while(i<5):
        while( (time.time() - start) <=1):
                                    mydata=(ArduinoUnoSerial.readline().strip())
                                    H2=mydata.decode('utf-8')
                                    H.append(H2)
                                    
##        start=time.time()
        
        #print(H)
        y=np.fft.fft(H)
        k=abs(y/len(H))
        Fs=len(H)/1
        fs=Fs*(np.arange(0,len(H)))/len(H)
        a=(np.where(np.logical_and(fs>220, fs<260)))
        d=(np.where(np.logical_and(fs>65, fs<75)))
        c=(np.where(np.logical_and(fs>121, fs<130)))
        bl=(np.where(np.logical_and(fs>360, fs<400)))
        
    ##    L1=max(k[a],default=0)
    ##    M2=max(k[bl],default=0)
    ##    N3=max(k[c],default=0)
    ##    P4=max(k[d],default=0)
        co=co+1
        #start=time.time()
        if co>2:
            L.append((max(k[a])))
            M.append((max(k[bl])))
            N.append((max(k[c])))
            P.append(max(k[d]))
            i=i+1
                
                

                
        #print(np.mean(y1),np.mean(y2),np.mean(y3),np.mean(y4))
        
            
            
                
        #a=(np.where(np.logical_and(fs>440, fs<500)))
        #print(max(k[a]))
##        plt.plot(fs,k)
##        plt.pause(0.01)
##        plt.clf()
        H=[0]
        start=time.time()
        
    y1 = sp.signal.medfilt(L,7)
    y2 = sp.signal.medfilt(M,7)
    y3 = sp.signal.medfilt(N,7)
    y4 = sp.signal.medfilt(P,7)
    #print(y1)
    from TrainrsiML import *
    with open('E:/python/trainmodML', 'rb') as f:
                    rf=pickle.load(f)
    print(np.mean(y1),np.mean(y2),np.mean(y3),np.mean(y4))
    predictions = rf.predict([[np.mean(y1),np.mean(y2),np.mean(y3),np.mean(y4)]])
   #print(np.mean(y1),np.mean(y2),np.mean(y3),np.mean(y4))
    print(predictions)
    inx=out1.index(int(predictions))
    print(x1[inx],y11[inx])
    H2=[0]
    xd=80
    yd=80
    X=[0,0,xd,xd]

    
    Y=[0,yd,yd,0]
    plt.plot(X,Y,'ko')
    plt.grid()
    plt.plot(x1[inx],y11[inx],'ro')
    plt.pause(0.01)    
    plt.clf()                    
    start=time.time()
        #print(H)
