void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);

}

void loop() {

float ldrdata=analogRead(A1);
//boolean vol=digitalRead(2);
  // Serial.print(ldrdata);
   
float  Rvoltage=(float)ldrdata/1023*5;
 float LdrVoltage=5-Rvoltage;
 float LdrR=LdrVoltage/Rvoltage*1000;

 float lux=21.66*Rvoltage*Rvoltage+21.21*Rvoltage-13.72;
 Serial.println(ldrlux);
 
}
