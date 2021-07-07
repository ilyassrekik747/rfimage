#include <RH_ASK.h>
#include <SPI.h> // Not actually used but needed to compile
String incomingByte = ""; // for incoming serial data
RH_ASK driver;

void setup()
{
    Serial.begin(9600);    // Debugging only
    if (!driver.init())
         Serial.println("init failed");
}

void loop()
{     if (Serial.available() > 0) {
    int i;
    char msg[i] = {};
    incomingByte = Serial.readString();
    i=incomingByte.length()+1;
    incomingByte.toCharArray(msg, i);

  
    driver.send((uint8_t *)msg, strlen(msg));
    driver.waitPacketSent();
    delay(1000);
}
}
