void setup() {
  Serial.begin(115200);

}

void loop() {
  String s;
  while(Serial.available()){
    char c = Serial.read();
    Serial.println(c); 


  }
}
