#include <Servo.h>

volatile unsigned long timeSensor1 = 0;
volatile unsigned long timeSensor2 = 0;
volatile unsigned long elapsed = 0;

const double SPEED = 895.0;  // m/s
const double VERTANGLE = 56.0;  // angle in degrees 2 is max height, 85 is lowest

double RADIUS = 0.0225; // radius of wheels in m

int pinServoVert = 3;
int pinServoShoot = 6;

Servo servoVert;
Servo esc1;  // Moteur droit vue du tireur
Servo esc2;  // Moteur gauche vue du tireur
Servo shooter;

double angleVertMax = 40.0;
double angleVertMin = 20.0;

int throttle1 = 0;
int throttle2 = 0;

const int vitessemax = 179;

void setup() 
{

  pinMode(20, INPUT_PULLUP);
  pinMode(21, INPUT_PULLUP);
  pinMode(13, OUTPUT);

  Serial.begin(9600);

  // put your setup code here, to run once:
  servoVert.attach(pinServoVert,900,2100);
  shooter.attach(pinServoShoot,1500,2000);
  esc1.attach(9);
  esc2.attach(10);
  //throttle1 = map(throttle1,0,1023,750,2400);
  //throttle2 = map(throttle2,0,1023,750,2400);
  esc1.writeMicroseconds(750);
  esc2.writeMicroseconds(750); 
  shooter.write(5);
  delay(3000);

  attachInterrupt(2, readTimeSensor1, FALLING);
  attachInterrupt(3, readTimeSensor2, FALLING);

}

void readTimeSensor1() 
{
    //unsigned long t = millis();
    // calculate speed basing on t - lastTime
    timeSensor1 = millis();
    //println("hello1");
}

void readTimeSensor2() 
{
    //unsigned long t = millis();
    // calculate speed basing on t - lastTime
    timeSensor2 = millis();
    //println("hello");
}

unsigned long speedCalc()
{
  unsigned long elapsed = timeSensor2 - timeSensor1;
  //Serial.println(elapsed);
  return elapsed;
}

double linSpeedToMicroSeconds(double vSpeed) 
{
 const double pente = 5;
 double microSeconds = (vSpeed * pente) + 885;
 int result;
 result = (int) microSeconds;
 return result;
}

double convertAngle(double pAngle)
{
  //if(pAngle > angleVertMax)pAngle = angleVertMax;
  //if(pAngle < angleVertMin)pAngle = angleVertMin;

  double pente = -1.4367;
  double correctedAngle = pAngle * (pente) + 171.61;
  return correctedAngle;
}

void raiseLauncher(double pAngle) 
{
  // Raise vertical servo
  servoVert.write(convertAngle(pAngle));
  //servoVert.write(VERTANGLE);
}


void activateLaunchWheels(double linearSpeed)
{
  //int rotSpeed = convertSpeed(linearSpeed);
  int rotSpeed = linSpeedToMicroSeconds(linearSpeed);
  //esc1.writeMicroseconds(linearSpeed);
  //esc2.writeMicroseconds(linearSpeed);

}

void shoot()
{
  delay(1000);
  shooter.write(110);
  delay(1000);
  shooter.write(5);
}

void printSpeed(unsigned long deltaT)
{
  if (deltaT < 450)
  {
    Serial.println(deltaT);
    }
  }
  
void loop() 
{
  // put your main code here, to run repeatedly:
    raiseLauncher(VERTANGLE);
    delay(1000);
    activateLaunchWheels(SPEED);
    delay(2500);
    shoot();
    unsigned long zeTime = speedCalc();
    activateLaunchWheels(750);
    raiseLauncher(0);
    Serial.println(0);
    printSpeed(zeTime);
    delay(2000);
}
