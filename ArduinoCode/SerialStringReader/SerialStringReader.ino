void parseString(String s){
  String functionCode = s.substring(0, 1);
  int deviceMod = s.substring(2, 3).toInt();
  int pin = s.substring(4, 5).toInt();
  int action = s.substring(6, 7).toInt();

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

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String s = Serial.readString();
    parseString(s);
  }
}
