import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
RELAY_PIN = 18
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Activate the relay
GPIO.output(RELAY_PIN, GPIO.HIGH)
print("Relay is ON")
time.sleep(5)  # Keep relay ON for 5 seconds

# Deactivate the relay
GPIO.output(RELAY_PIN, GPIO.LOW)
print("Relay is OFF")
GPIO.cleanup()