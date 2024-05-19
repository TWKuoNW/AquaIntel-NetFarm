String* parseString(String originalString, char op) {
  String* resultString = new String[10];
  int startIndex = 0;
  int endIndex = 0;
  int count = 0;
  while (endIndex != -1 && count < 10) {
    endIndex = originalString.indexOf(op, startIndex);
    String elementString = (endIndex == -1) ? originalString.substring(startIndex) : originalString.substring(startIndex, endIndex);
    startIndex = endIndex + 1;
    resultString[count] = elementString;
    count++;
  }
  return resultString;
}
#include "BluetoothSerial.h"
BluetoothSerial SerialBT;

int pumpInside = 4;
int pumpOutside = 0;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ProbioticSprayer");  //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");

  // 預設兩顆幫浦關閉
  pinMode(pumpInside, OUTPUT);
  digitalWrite(pumpInside, HIGH);
  pinMode(pumpOutside, OUTPUT);
  digitalWrite(pumpOutside, HIGH);
}

void loop() {
  if (Serial.available() > 0 || SerialBT.available() > 0) {
    String inputString = "";
    if(Serial.available() > 0){
      inputString = Serial.readString();
    }else if(SerialBT.available() > 0){
      inputString = SerialBT.readString();
    }
    String* modifiedString = parseString(inputString, ',');
    //char status = (char)SerialBT.read();
    String functionCode = modifiedString[0];
    int deviceMod = modifiedString[1].toInt();
    int GPIOPin = modifiedString[2].toInt();
    int status = modifiedString[3].toInt();
    // deviceMod: 0 -> OUTPUT, 1 -> INPUT
    if (deviceMod == 0) {
      pinMode(GPIOPin, OUTPUT);
    } else if(deviceMod == 1) {
      pinMode(GPIOPin, INPUT);
    }

    // status: 0 -> close, 1 -> open
    if (status == 0) {
      digitalWrite(GPIOPin, HIGH);
      Serial.println("close");
      SerialBT.println("close");
    } else {
      digitalWrite(GPIOPin, LOW);
      Serial.println("open");
      SerialBT.println("open");
    }
  }
}