#include <Arduino.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pca = Adafruit_PWMServoDriver();

void setup()
{
    Serial.begin(115200);
    pca.begin();
    pca.setPWMFreq(50);
}

void loop()
{
    if (Serial.available())
    {
        String input = Serial.readStringUntil('\n');
        int off = input.toInt();
        if (off > 0)
        {
            pca.setPWM(4, 0, off);
            Serial.println(off);
        }
    }
}