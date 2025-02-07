import RPi.GPIO as GPIO
import time

# GPIO Pin Definitions
IN1 = 17  # Control pin 1
IN2 = 27  # Control pin 2
ENA = 18  # PWM pin for speed control

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

# PWM Setup
pwm = GPIO.PWM(ENA, 100)  # 100Hz PWM frequency
pwm.start(0)  # Start PWM with 0% duty cycle

def motor_forward(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)

def motor_reverse(speed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm.ChangeDutyCycle(speed)

try:
    print("Motor running forward at 50% speed")
    motor_forward(50)  # Forward with 50% speed
    time.sleep(2)

    print("Motor running reverse at 75% speed")
    motor_reverse(75)  # Reverse with 75% speed
    time.sleep(2)

    print("Stopping motor")
    pwm.ChangeDutyCycle(0)  # Stop motor
    time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    pwm.stop()
    GPIO.cleanup()