/*
該副程式接收一字串，並將字串做剖析處理
輸入兩個引數 parseString(處理字串, 分割符號)，該副程式會回傳一字串陣列。
EX:
parseString("c,0,1,1", ',');
副程式回傳["c", "0", "1", "1"]的字串陣列。
*/
String* parseString(String originalString, char op){ 
  String* resultString = new String[10]; // 建立一個字串陣列，用於儲存並回傳剖析後資料
  int startIndex = 0; // 起始 index
  int endIndex = 0; // 結束 index
  int count = 0; // 計數器
  while (endIndex != -1 && count < 10) { // 長度需小於10，並且後面還有資料
    endIndex = originalString.indexOf(op, startIndex); // 尋找第一個op所在位置
    String elementString = (endIndex == -1) ? originalString.substring(startIndex) : originalString.substring(startIndex, endIndex);
    startIndex = endIndex + 1; // 更新開始位置
    resultString[count] = elementString; // 將資料存入陣列
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
    String* modifiedString = parseString(inputString, ',');
    
    String functionCode = modifiedString[0];
    int deviceMod = modifiedString[1].toInt();
    int pin = modifiedString[2].toInt();
    int action = modifiedString[3].toInt();

    if(functionCode.equals("c")){
      Serial.println("Function Code is control.");
    }else if(functionCode.equals("s")){
      Serial.println("Function Code is set.");
    }else if(functionCode.equals("r")){
      Serial.println("Function Code is reset.");
    }else{
      Serial.println("other");
    }

    if(deviceMod == 0){
      pinMode(pin, OUTPUT);
      Serial.println("PinMode is OUTPUT");
    }else{
      pinMode(pin, INPUT);
      Serial.println("PinMode is INPUT");
    }

    Serial.print("Pin number is:");
    Serial.println(pin);

    if(action == 0){
      digitalWrite(pin, LOW);
      Serial.println("Action is LOW");
    }else{
      digitalWrite(pin, HIGH);
      Serial.println("Action is HIGH");
    }
  }

}
