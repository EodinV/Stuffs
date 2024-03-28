/**
 * @file main.cpp
 * @author Mattias Veschetti Holmgren (mattiasvholmgren@gmail.com)
 * @brief 
 * @version 0.1
 * @date 2023-11-22
 * 
 * @copyright Copyright (c) 2023
 * 
 */
#include <Arduino.h>
#include <Wire.h>
#include <Windy.h>
#include <DHT.h>

int temp()
{
  //collect temperature from DHT 11 / DHT 22
  uint8_t temp = dht.readTemperature();
  return temp;
}

int hygro()
{
  //collect Hygometric data from DHT 11 / DHT 22
  uint8_t hum = dht.readHumidity();
  return hum;
}

int barometer()
{
  //collect barometric pressure via I2C from barometer
  Wire.requestFrom(0, 8);
  uint8_t baro = Wire.read();
  return baro;
}

int correction()
{
  //use hygrometer and barometer to adjust windchill factor. shoud return an int.
  barometer();
  hygro();
  return 0;
}

int direction()
{
  //compare temperatures of termistor-ring to determine/calculate wind direction
  int dir = 0;
  int n = analogRead(N);
  int ne = analogRead(NE);
  int e = analogRead(E);
  int se = analogRead(SE);
  int s = analogRead(S);
  int sw = analogRead(SW);
  int w = analogRead(W);
  int nw = analogRead(NW);

  if (((nw + n + ne) / 3) > ((se + s + sw + w + e) / 5))
  {
    dir = 1;
  }

  if (((n + ne + e) / 3) > ((se + s + sw + w + nw) / 5))
  {
    dir = 2;
  }

  if (((ne + e + se) / 3) > ((n + s + sw + w + nw) / 5))
  {
    dir = 3;
  }

  if (((e + se + s) / 3) > ((ne + n + sw + w + nw) / 5))
  {
    dir = 4;
  }

  if (((se + s + sw) / 3) > ((ne + n + e + w + nw) / 5))
  {
    dir = 5;
  }

  if (((s + sw + w) / 3) > ((ne + n + e + se + nw) / 5))
  {
    dir = 6;
  }

  if (((sw + w + nw) / 3) > ((se + s + ne + e + n) / 5))
  {
    dir = 7;
  }

  if (((w + nw + n) / 3) > ((se + s + sw + e + ne) / 5))
  {
    dir = 8;
  }
  
  else
  {
    dir = 0;
  }
  
  switch (dir)
  {
  case 1:
    digitalWrite(LEDNW, HIGH);
    digitalWrite(LEDN, HIGH);
    digitalWrite(LEDNE, HIGH);
    digitalWrite(LEDE, LOW);
    digitalWrite(LEDSE, LOW);
    digitalWrite(LEDS, LOW);
    digitalWrite(LEDSW, LOW);
    digitalWrite(LEDW, LOW);
  case 2:
    digitalWrite(LEDN, HIGH);
    digitalWrite(LEDNE, HIGH);
    digitalWrite(LEDE, HIGH);
    digitalWrite(LEDSE, LOW);
    digitalWrite(LEDS, LOW);
    digitalWrite(LEDSW, LOW);
    digitalWrite(LEDW, LOW);
    digitalWrite(LEDNW, LOW);
  case 3:
    digitalWrite(LEDNE, HIGH);
    digitalWrite(LEDE, HIGH);
    digitalWrite(LEDSE, HIGH);
    digitalWrite(LEDS, LOW);
    digitalWrite(LEDSW, LOW);
    digitalWrite(LEDW, LOW);
    digitalWrite(LEDNW, LOW);
    digitalWrite(LEDN, LOW);
  case 4:
    digitalWrite(LEDE, HIGH);
    digitalWrite(LEDSE, HIGH);
    digitalWrite(LEDS, HIGH);
    digitalWrite(LEDSW, LOW);
    digitalWrite(LEDW, LOW);
    digitalWrite(LEDNW, LOW);
    digitalWrite(LEDN, LOW);
    digitalWrite(LEDNE, LOW);
  case 5:
    digitalWrite(LEDSE, HIGH);
    digitalWrite(LEDS, HIGH);
    digitalWrite(LEDSW, HIGH);
    digitalWrite(LEDW, LOW);
    digitalWrite(LEDNW, LOW);
    digitalWrite(LEDN, LOW);
    digitalWrite(LEDNE, LOW);
    digitalWrite(LEDE, LOW);
  case 6:
    digitalWrite(LEDS, HIGH);
    digitalWrite(LEDSW, HIGH);
    digitalWrite(LEDW, HIGH);
    digitalWrite(LEDNW, LOW);
    digitalWrite(LEDN, LOW);
    digitalWrite(LEDNE, LOW);
    digitalWrite(LEDE, LOW);
    digitalWrite(LEDSE, LOW);
  case 7:
    digitalWrite(LEDSW, HIGH);
    digitalWrite(LEDW, HIGH);
    digitalWrite(LEDNW, HIGH);
    digitalWrite(LEDN, LOW);
    digitalWrite(LEDNE, LOW);
    digitalWrite(LEDE, LOW);
    digitalWrite(LEDSE, LOW);
    digitalWrite(LEDS, LOW);
  case 8:
    digitalWrite(LEDW, HIGH);
    digitalWrite(LEDNW, HIGH);
    digitalWrite(LEDN, HIGH);
    digitalWrite(LEDNE, LOW);
    digitalWrite(LEDE, LOW);
    digitalWrite(LEDSE, LOW);
    digitalWrite(LEDS, LOW);
    digitalWrite(LEDSW, LOW);
    break;
  
  default:
    digitalWrite(LEDN, LOW);
    digitalWrite(LEDNE, LOW);
    digitalWrite(LEDE, LOW);
    digitalWrite(LEDSE, LOW);
    digitalWrite(LEDS, LOW);
    digitalWrite(LEDSW, LOW);
    digitalWrite(LEDW, LOW);
    digitalWrite(LEDNW, LOW);
    break;
  }
  

  return dir;
}

//int windchill(int bar,int hyg ,int tmp)
//{
  //calculate windchill to determine approximate windspeed .. Wind Chill
  //tmp is ambient temp, wind will be calculated as difference in temp is known.
  //C = Q /(m × ΔT)
  // Q = energy (Joules) ΔT = difference in temperature (⁰C) m = Mass (kg)
  //int wind = 0;
//
//  
//
//  return wind;
//}



void setup() {
  dht.begin();
  Wire.begin();
  Serial.begin(9600);
  pinMode(N, INPUT);
  pinMode(NE, INPUT);
  pinMode(E, INPUT);
  pinMode(SE, INPUT);
  pinMode(S, INPUT);
  pinMode(SW, INPUT);
  pinMode(W, INPUT);
  pinMode(NW, INPUT);
  pinMode(BAROA, INPUT);
  pinMode(BAROL, INPUT);
  pinMode(DHTPIN, INPUT);
  pinMode(LEDN, OUTPUT);
  pinMode(LEDNE, OUTPUT);
  pinMode(LEDE, OUTPUT);
  pinMode(LEDSE, OUTPUT);
  pinMode(LEDS, OUTPUT);
  pinMode(LEDSW, OUTPUT);
  pinMode(LEDW, OUTPUT);
  pinMode(LEDNW, OUTPUT);
}


void loop() 
{  
  direction();
}



