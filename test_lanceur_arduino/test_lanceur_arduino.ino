#include <Servo.h>

//Constantes de la vitesse et de l'angle pour le lancer à effectuer selon la position
const double SPEED = 4.82;  // m/s
const double OFFSETSPEED = 0.0; // Ajustement de la vitesse provenant des algorithme -> en microSeconds
const double VERTANGLE = 59.265;  // angle in degrees 61 is max height, 0 is lowest

int pinServoVert = 3;
int pinServoShoot = 6;

Servo servoVert; //Servo pour modifier l'angle de tir
Servo esc1;  // Moteur droite vue du tireur (vers la cible)
Servo esc2;  // Moteur gauche vue du tireur (vers la cible)
Servo shooter; //Servo pour pousser la balle vers les moteurs (pour tirer)

void setup()
{
  // put your setup code here, to run once:
  servoVert.attach(pinServoVert,900,2100); //Nombres = MIN et MAX du PWM (micro secondes) pour le serbo
  shooter.attach(pinServoShoot,1500,2000);
  esc1.attach(9); // Moteur droite attaché en PWM à la pin #9
  esc2.attach(10); // Moteur droite attaché en PWM à la pin #9
  esc1.writeMicroseconds(750); // Valeur minimal en micro secondes (PWM) à appliquer au moteur pour le bon fonctionnement
  esc2.writeMicroseconds(750); // Valeur minimal en micro secondes (PWM) à appliquer au moteur pour le bon fonctionnement
  shooter.writeMicroseconds(1500); // Position de base (bandé vers le ciel)
  delay(3000); // Permet aux moteurs de s'initialiser (valeur à optimiser)
  shooter.detach(); // Désalimente le shaft bandé du servo pour pousser la balle / évite de rentrer en conflit avec le servo de l'angle

}

//Fonction permettant d'adapter la vitesse en m/s pour une consigne aux moteurs en micro secondes
double linSpeedToMicroSeconds(double vSpeed)
{
 // y = 5*x + 885
 const double pente = 5.0;
 double microSeconds = (vSpeed * pente) + (885 + OFFSETSPEED);
 return microSeconds;
}

//Fonction permettant d'adapter l'angle voulue et celle réelle pour le servo
double convertAngle(double pAngle)
{
   // y = -1.4367*x + 171.61
  double pente = -1.4367;
  double correctedAngle = pAngle * (pente) + 171.61;
  double microSeconds = map (correctedAngle, 0,180,900,2100);
  return microSeconds;
}

//Envoi la commande au servo de se position à l'angle voulue
void raiseLauncher(double pAngle)
{
  servoVert.writeMicroseconds(convertAngle(pAngle));
}

////Envoi la commande aux servos des moteurs de se mettre à la vitesse voulue
void activateLaunchWheels(double linearSpeed)
{
  double rotSpeed = linSpeedToMicroSeconds(linearSpeed); //Appel la fonction d'adaptation
  esc1.writeMicroseconds(rotSpeed);
  esc2.writeMicroseconds(rotSpeed);
}

//Permet de pousser la balle
void shootLauch()
{
  shooter.attach(pinServoShoot,1500,2000); //Alimente le servo
  delay(1000);
  shooter.writeMicroseconds(1805); // 1805 -> position débandée du pousseux
  delay(1000);
}

//Remet en position pour être prêt à recevoir une balle
void shootReturn()
{
  shooter.writeMicroseconds(1500); //Position bandée du pousseux
  delay(1000);
  shooter.detach(); //Désalimente le servo
}

void loop()
{
  // put your main code here, to run repeatedly:
    raiseLauncher(VERTANGLE);
    delay(1000);
    activateLaunchWheels(SPEED);
    delay(2000);
    shootLauch();
    esc1.writeMicroseconds(750); //Pour arrêter les moteurs
    esc2.writeMicroseconds(750);
    raiseLauncher(0); //Descends le lanceur
    delay(1000);
    shootReturn();
    delay(2000);
}
