#include <SpeedyStepper.h>

#include <ros.h>        //rosrun rosserial_arduino serial_node.py _port:=/dev/ttyUSB0
#include <std_msgs/String.h> //http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup

ros::NodeHandle  nh;

#define X_STEP_PIN         54
#define X_DIR_PIN          55
#define X_ENABLE_PIN       38
#define X_MIN_PIN           3
#define X_MAX_PIN           2

#define Y_STEP_PIN         60
#define Y_DIR_PIN          61
#define Y_ENABLE_PIN       56
#define Y_MIN_PIN          14
#define Y_MAX_PIN          15

#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       62
#define Z_MIN_PIN          18
#define Z_MAX_PIN          19

#define E_STEP_PIN         26
#define E_DIR_PIN          28
#define E_ENABLE_PIN       24

#define Q_STEP_PIN         36
#define Q_DIR_PIN          34
#define Q_ENABLE_PIN       30

SpeedyStepper stepperX;
SpeedyStepper stepperZ;

String numb2 ;
String numb1;
String x;

void stepmove(){
  int stepx = numb1.toInt();
  int stepy = numb2.toInt();
  stepperX.setSpeedInStepsPerSecond(100);
  stepperX.setAccelerationInStepsPerSecondPerSecond(80);
  stepperX.moveRelativeInSteps(stepx);

  stepperZ.setSpeedInStepsPerSecond(100);
  stepperZ.setAccelerationInStepsPerSecondPerSecond(80);
  stepperZ.moveRelativeInSteps(stepy);

}

void messageCb(std_msgs::String& toggle){
    x = toggle.data;
    int Fvirg = x.indexOf(',');
    int svirg = x.indexOf('}');
    numb2 = x.substring(Fvirg+2, svirg);
    numb1 = x.substring(1,Fvirg);
    //Serial.print(numb2);
    stepmove();
 
}

ros::Subscriber<std_msgs:: String> sub("arduino", &messageCb );

void setup() {
  Serial.begin(57600);
  pinMode(X_STEP_PIN  , OUTPUT);
  pinMode(X_DIR_PIN    , OUTPUT);
  pinMode(X_ENABLE_PIN    , OUTPUT);

  pinMode(Y_STEP_PIN  , OUTPUT);
  pinMode(Y_DIR_PIN    , OUTPUT);
  pinMode(Y_ENABLE_PIN    , OUTPUT);

  pinMode(Z_STEP_PIN  , OUTPUT);
  pinMode(Z_DIR_PIN    , OUTPUT);
  pinMode(Z_ENABLE_PIN    , OUTPUT);

  digitalWrite(X_ENABLE_PIN    , LOW);
  digitalWrite(Y_ENABLE_PIN    , LOW);
  digitalWrite(Z_ENABLE_PIN    , LOW);
 
  stepperX.connectToPins(X_STEP_PIN, X_DIR_PIN);
  stepperZ.connectToPins(Z_STEP_PIN, Z_DIR_PIN);

  nh.initNode();
  nh.subscribe(sub);
}
void loop() {
  nh.spinOnce();
  delay(1);
}
