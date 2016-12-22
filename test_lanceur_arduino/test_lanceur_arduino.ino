#include <Servo.h>

const double LINEARSPEED = 3.50;  // m/s
const double VERTANGLE = 40;  // angle in degrees 48 is max height, higher values will lower the angle

double RADIUS = 0.0225; // radius of wheels in m

int pinServoVert = 3;
int pinServoShoot = 6;

const int shooterDown = 110;
const int shooterUp = 40;

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

  // put your setup code here, to run once:
  servoVert.attach(pinServoVert);
  shooter.attach(pinServoShoot);
  esc1.attach(9);
  esc2.attach(10);
  //throttle1 = map(throttle1,0,1023,750,2400);
  //throttle2 = map(throttle2,0,1023,750,2400);
  esc1.writeMicroseconds(750);
  esc2.writeMicroseconds(750); 
  shooter.write(shooterUp);
  delay(3000);

}


double linSpeedToMicroSeconds(double vSpeed) 
{
 double deltaY = 2400.0 - 750.0;
 double rmp_per_volts = 950;
 
 const double pente = 1;
 double microSeconds = ((vSpeed * 60)/(2 * PI * RADIUS)) * (pente) + 750;
 return microSeconds;
}

double convertAngle(double pAngle)
{
  if(pAngle > angleVertMax)pAngle = angleVertMax;
  if(pAngle < angleVertMin)pAngle = angleVertMin;

  double pente = -1.1065;
  double correctedAngle = pAngle * (pente) + 104.51;
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
  //int rotSpeed = linSpeedToMicroSeconds(linearSpeed);
  
  esc1.writeMicroseconds(1475);
  esc2.writeMicroseconds(1475);

}

void shoot()
{
  shooter.write(shooterDown);
  delay(1000);
  shooter.write(shooterUp);
}

void loop() 
{
  // put your main code here, to run repeatedly:
    raiseLauncher(VERTANGLE);
    delay(2000);
    //activateLaunchWheels(LINEARSPEED);
    delay(1500);
    shoot();
    raiseLauncher(0);
    delay(3000);
}
