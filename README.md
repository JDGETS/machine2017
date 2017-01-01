# Machine 2017

## Procédure de contrôle dev
1. Diffuser le Wi-Fi "yul22" avec l'ordinateur de contrôle
2. Alimenter la machine
3. Démarrer le launch file `rpi.launch` sur le RPi
4. Démarrer le launch file `control_station.launch` sur l'ordinateur de contrôle
5. Placer le robot sur le terrain
6. Appuyer la touche "Logitech" de la manette lorsque stable sur le terrain pour mapper le terrain
7. Au signal de départ, appuyer sur "Logitech" pour passer en mode "autonome"
8. Au signal de transition, appuyer sur "Logitech" pour passer en mode "manuel"


### Nodes
#### `launcher place_launcher.py`
Cette node s'occupe de calculer l'angle de tir idéal et placer le lanceur de balle pour atteindre une cible donné. Cette cicle est selectionné par une valeur de 0 à 2 par un message sur le topic `/place_launcher` (de type `std_msgs/Byte`).

![Launcher](http://i.imgur.com/UH0FM1g.png)

#### `imu mpu6050.py`
Implémentation de l'IMU MPU-6050 pour ROS. Les valeurs brutes sont retransmises sur le topic `/imu`. Seul la vitesse angulaire et l'accélération linéaire sont disponibles avec ce modèle. L'angle est caculé à l'aide d'un filtre de Kalman fournit par le package `robot_localization`. L'angle est aussi publié `/imu_pose` à l'aide d'un filtre complémentaire mais est moins précis.

#### `lift lift_node.py`
Cette node s'occupe de géré la position du scissor lift. Deux capteurs permettent de déterminé si les positions du lift sont atteintes. Le lift est contrôllé par le topic `/lift` de type `std_msgs/String` qui indique la position à désiré (`up` ou `down`).

#### `pwm_driver pwm_driver_node.py`
Cette node est une implémentation pour le [Adafruit 16-Channel 12-bit PWM/Servo Driver - I2C interface - PCA9685](https://www.adafruit.com/product/815). La node permet de contrôle les 16 cannaux de la chip soit par un duty cycle (0%-100%) ou bien en microsecondes. Les topics utilisés sont respectivement `/duty_cycle` avec un message de type pwm_driver/DutyCycle et `/pulse_width` avec un message de type `pwm_driver/PulseWidth`

#### `joy_broadcaster teleop.py`
Cette node est adapté de du package [capra_teleop](https://github.com/clubcapra/Ibex/tree/master/src/capra_teleop) du [Club Capra](http://www.clubcapra.com/). Elle permet d'interpréter les messages de type `sensor_msgs/Joy` diffuser par la node `joy joy` qui contient les entrés de la manette.
