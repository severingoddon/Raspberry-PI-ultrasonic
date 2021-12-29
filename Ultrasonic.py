# this code reads ultrasonic sensor data and puts out the distance
# wiring under: https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

# Trigger is GPIO 23, Echo is GPIO 24


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("Distance measurement loading")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)
count = 0
while count < 20:
    count += 1
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print("Distance is: ", distance, "cm")


    time.sleep(2)

GPIO.cleanup()