#include <Arduino.h>
#include <WiFi.h>
#include "BluetoothSerial.h"
#include <ascii.h>




#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled
#endif



BluetoothSerial SerialBT;



void setup()
{
  Serial.begin(115200);
  SerialBT.begin();

  Serial.println("Bluetooth Ready: Pairing Mode");
}

void loop()
{
  if (Serial.available())
  {
    char inst = Serial.read();
    SerialBT.print(inst);
  }
  if (SerialBT.available())
  {
    char unst = SerialBT.read();
    Serial.print(unst);
  }

  delay(20);
}
