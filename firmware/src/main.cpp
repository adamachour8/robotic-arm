#include <Arduino.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pca = Adafruit_PWMServoDriver();

enum Joint
{
    BASE,
    SHOULDER,
    ELBOW,
    GRIPPER,
    NUM_JOINTS
};

enum GripperState
{
    OPEN,
    CLOSED
};

int channels[NUM_JOINTS] = {0, 1, 2, 3};
int tickZero[NUM_JOINTS] = {105, 180, 500, 90};
int startTick[NUM_JOINTS] = {580, 320, 100, 90};
int currentTick[NUM_JOINTS] = {580, 320, 100, 90};
float ratio[NUM_JOINTS] = {0.36, 0.643, 0.4, 1.0};
float angleMin[NUM_JOINTS] = {45, 0, -160, 0};
float angleMax[NUM_JOINTS] = {135, 120, -110, 1};

int angleToTick(Joint joint, float angle)
{
    float currentRatio = ratio[joint];
    int tick = tickZero[joint] + (angle / currentRatio);
    return tick;
}

float clampAngle(Joint joint, float angle)
{
    if (angle < angleMin[joint])
    {
        Serial.print("Angle trop bas, min = ");
        Serial.println(angleMin[joint]);
        return angleMin[joint];
    }
    if (angle > angleMax[joint])
    {
        Serial.print("Angle trop haut, max = ");
        Serial.println(angleMax[joint]);
        return angleMax[joint];
    }
    return angle;
}

void moveServo(Joint joint, float angle)
{
    angle = clampAngle(joint, angle);
    int target = angleToTick(joint, angle);
    int step = (target > currentTick[joint]) ? 1 : -1;

    for (int pos = currentTick[joint]; pos != target; pos += step)
    {
        pca.setPWM(channels[joint], 0, pos);
        delay(10);
    }

    currentTick[joint] = target;
}

void gripper(GripperState state)
{
    int tick = (state == OPEN) ? 160 : 95;
    pca.setPWM(channels[GRIPPER], 0, tick);
}

void setup()
{
    Serial.begin(115200);
    pca.begin();
    pca.setPWMFreq(50);

    Serial.println("Appuie Enter pour commencer");
    while (!Serial.available())
    {
    }
    while (Serial.available())
        Serial.read();

    for (int i = 0; i < NUM_JOINTS; i++)
    {
        pca.setPWM(channels[i], 0, startTick[i]);
        currentTick[i] = startTick[i];
        delay(1000);
    }
    delay(1000);

    moveServo(BASE, 90);
    moveServo(SHOULDER, 80);
    moveServo(ELBOW, -150);
    gripper(OPEN);
    delay(1000);
    gripper(CLOSED);
}

void loop()
{
    delay(100);
}
