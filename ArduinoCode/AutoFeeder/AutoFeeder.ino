#include <BluetoothSerial.h> 
BluetoothSerial SerialBT; 

char command;
int led = 4;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("AutoFeeder");
  pinMode(led, OUTPUT);
  Serial.println("open");
}

void loop() {
  if (SerialBT.available()) {
    command = SerialBT.read();
    if(command == '1'){
      Serial.println("open");
      SerialBT.println("AutoFeeder Open");
      digitalWrite(led, HIGH);
    }else if(command == '0'){
      Serial.println("close");
      SerialBT.println("AutoFeeder Close");
      digitalWrite(led, LOW);
    }else{
      Serial.println("keyin error");
      SerialBT.println("keyin error");
    }
  }
  delay(50);
}