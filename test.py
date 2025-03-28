import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

print("Blinking GPIO 17")
for i in range(5):
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()