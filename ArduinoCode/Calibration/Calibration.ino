#include <Arduino.h>

#include <OneWire.h> 
#include <DallasTemperature.h> 

#define VREF    5000 //若ADC参考电压不为5V，请根据实际情况修改VREF
#define ADC_RES 1024 //若ADC分辨率不为1024，请根据实际情况修改ADC_RES
#define DQ_Pin 2    // 溫度感測器Pin

OneWire oneWire(DQ_Pin);
DallasTemperature sensors(&oneWire);

uint32_t raw;

void setup()
{
    Serial.begin(115200);
    sensors.begin();
}

void loop()
{
    
    sensors.requestTemperatures();
    uint8_t Temperaturet = (uint8_t)sensors.getTempCByIndex(0);
    raw=analogRead(A1);
    Serial.println("Temp:\t"+String(Temperaturet)+"\traw:\t"+String(raw)+"\tVoltage(mv)"+String(raw*VREF/ADC_RES));
    delay(1000);
}