void setup() {
  Serial.begin(9600);
  String data = "c,2,3,4";
  int lastCommaIndex = -1; 
  int commaIndex = 0;

  while ((commaIndex = data.indexOf(',', lastCommaIndex + 1)) != -1) {
    String part = data.substring(lastCommaIndex + 1, commaIndex);
    Serial.println(part);
    lastCommaIndex = commaIndex;
  }

  String lastPart = data.substring(lastCommaIndex + 1);
  Serial.println(lastPart);
}

void loop() {
  
}
