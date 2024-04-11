#include <BluetoothSerial.h> 
BluetoothSerial SerialBT; 

char command;
int led = 4;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ProbioticSprayer");
  pinMode(led, OUTPUT);
}

void loop() {
  if (SerialBT.available()) {
    command = SerialBT.read();
    if(command == '1'){
      Serial.println("open");
      SerialBT.println("ProbioticSprayer Open");
      digitalWrite(led, HIGH);
    }else if(command == '0'){
      Serial.println("close");
      SerialBT.println("ProbioticSprayer Close");
      digitalWrite(led, LOW);
    }else{
      Serial.println("keyin error");
      SerialBT.println("keyin error");
    }
  }
  delay(50);
}