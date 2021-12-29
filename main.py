import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT) # G

GPIO.output(23, GPIO.HIGH)
i = 0
while True:
    time.sleep(10)
    i+= 1
    print(i)
    if i == 10: break


GPIO.cleanup()
