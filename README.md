# Indoor-Localization-based-on-VLC-using-Machine-Learning
The Project describes the visible light communication used for localization using machine learning approach, different methods can be apply in order to get the location information i.e. trilateration, fingerprint etc. So each methods has some advantages and disadvantages. The results obtained from each method are also good,  but in trilateration FOV of the receiver is play an important role and results are affected if receiver escalates its FOV, wherein fingerprint, if the length of the database is large then the time taken to predict the location is also increase. Machine learning approach can be apply in order to overcome the aforesaid issues.  

### Prerequisites 
1. Arduino 
2. Python IDE
3. Arduino IDE
4. OPT101 Photodiode
5. LEDs
6. Resistor 1K ohm
7. Breadboard

### Experimental setup
Figure illustrates the experimental setup, 1x1m area is used for the experiment and the four LEDs are used as transmitters which are blinking at (50,70,125,145 HZ) frequencies 



![image](https://user-images.githubusercontent.com/32608510/38869918-e9f31806-4269-11e8-8ac7-1002a2a92419.png)


### Steps
## 1. Data Collection
First collect the data for model that will be used to train the data when applying for machine learning. Data is collected from arduino and store in csv format, data is collected in the grid of 5 cm, so total 18x18 row and column data with 15 samples for each grid is collected.

## 2. Training and testing the model
after the collection of data using regression approach a model is trained, so different regressor is applied and the most accurate is selected for the testing. After training, testing of data is performed and the errors in results are analysed for accuracy.  

