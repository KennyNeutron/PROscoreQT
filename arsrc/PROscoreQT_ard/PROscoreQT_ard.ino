#include <Arduino.h>

#define testPin 1

void setup(){
    Serial.begin(9600);
    Serial.setTimeout(1);
}

void loop(){
    uint8_t anyNum= random(0,255);
    Serial.println("The Random Num: "+ String(anyNum));
    delay(500);
}