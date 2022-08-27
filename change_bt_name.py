#define rxPin 7 // Teensy pin 7 <--> HC-05 Tx
#define txPin 8 // Teensy pin 8 <--> HC-05 Rx

#define keyPin 9
void setup() 
{
  pinMode(keyPin, OUTPUT);    // this pin will pull the HC-05 
                         // pin 34 (KEY pin) HIGH to switch
                         //  module to AT mode

  digitalWrite(keyPin, HIGH); 
  Serial.begin(9600);
  Serial.println("Enter AT commands:");
  Serial1.begin(38400);  // HC-05 default speed in AT 
                          // command mode
}

void loop()
{
  // Keep reading from HC-05 and send to Arduino 
  // Serial Monitor
  if (Serial1.available())
    Serial.write(Serial1.read());

  // Keep reading from Arduino Serial Monitor 
  //  and send to HC-05
  if (Serial.available())
    Serial1.write(Serial.read());
}
