from driver import PWM
import pigpio
import time

pi = pigpio.pi()
pwm = PWM(pi, 0x41)

pwm.set_frequency(50)

speed_motors = 750
angle = 55

def set_angle(x):
    pente = -10.422
    offset = 2159.2
    angle = pente * x + offset

    pwm.set_pulse_width(11, angle)

def set_speed(x):
    pwm.set_pulse_width(13, x)
    pwm.set_pulse_width(14, x)


# reset trigger
pwm.set_pulse_width(12, 2300)

time.sleep(1)

set_speed(750)

time.sleep(3)

set_angle(angle)

time.sleep(2)

set_speed(750 + 150)

time.sleep(5)

pwm.set_pulse_width(12, 550)

time.sleep(0.5)

set_speed(750)
