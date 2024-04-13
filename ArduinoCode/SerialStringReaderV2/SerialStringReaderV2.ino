String* parseString(String originalString, char op, int& count){
  String* resultString = new String[10];
  int startIndex = 0;
  int endIndex = 0;
  count = 0;
  while (endIndex != -1 && count < 10) {
    endIndex = originalString.indexOf(op, startIndex);
    String elementString = (endIndex == -1) ? originalString.substring(startIndex) : originalString.substring(startIndex, endIndex);
    startIndex = endIndex + 1;
    resultString[count] = elementString;
    count++;
  } 
  return resultString;
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String inputString = Serial.readString();
    int count = 0;
    String* modifiedString = parseString(inputString, ',', count);
    
    String functionCode = modifiedString[0];
    int deviceMod = modifiedString[1].toInt();
    int pin = modifiedString[2].toInt();
    int action = modifiedString[3].toInt();

    if(functionCode.equals("c")){
      if(deviceMod == 0){
        pinMode(pin, OUTPUT);
      }else{
        pinMode(pin, INPUT);
      }
      if(action == 1){
        digitalWrite(pin, HIGH);
      }else{
        digitalWrite(pin, LOW);
      }

    }else if(functionCode.equals("s")){
      Serial.println("is s");
    }else if(functionCode.equals("r")){
      Serial.println("is r");
    }else{
      Serial.println("other");
    }
  }

}
