import serial                                          #Serial imported for Serial communication
import time
import numpy as np
import cmath
#import least square con.py
from xlwt import Workbook
start=time.time()
i=1
Mn=0
Ln=0
cu=0
wb=Workbook()
sh1=wb.add_sheet('sheet2',cell_overwrite_ok=True)
ArduinoUnoSerial = serial.Serial('com9',115200)       #Create Serial port object called ArduinoUnoSerialData time.sleep(1)                                                             #wait for 2 secounds for the communication to get established
#print ArduinoNanoSerial.readline()                             #read the serial data and print it as line 
while(True):
    #mydata=(ArduinoUnoSerial.readline().strip())
    #print(mydata.decode('utf-8'))
    H2=[7000]
    H=[]

    while( (time.time() - start) <= 1.0):
                                mydata=(ArduinoUnoSerial.readline().strip())
                                H2=mydata.decode('utf-8')
                                H.append(H2)
                                
    start=time.time()
    #print(len(H))
    y=np.fft.fft(H)
    k=abs(y/len(H))
    Fs=len(H)/2
    fs=Fs*(np.arange(0,len(H)))/len(H)
    a=(np.where(np.logical_and(fs>47, fs<52)))
    d=(np.where(np.logical_and(fs>68, fs<72)))
    c=(np.where(np.logical_and(fs>121, fs<126)))
    bl=(np.where(np.logical_and(fs>145, fs<152)))
    #print(k[b1])
    #print(max(k[a]))
    #print(max(k[bl]))
    #print(max(k[c]))
    #print(max(k[d]))
    
    H2=[0]
    if i-Ln>3:
        sh1.write(i,0,max(k[a]))
        sh1.write(i,1,max(k[bl]))
        sh1.write(i,2,max(k[c]))
        sh1.write(i,3,max(k[d]))
        
        
    #print(i-k)
    if i-Mn==15:
        #sh1.write(i,0,'change')
        print('change the location')
       
        Mn=i
        Ln=i
    i=i+1 
    wb.save('xlwt Arduinodata.csv')    
    
