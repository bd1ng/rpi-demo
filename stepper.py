import RPi.GPIO as GPIO
import time

# GPIO Pins for stepper motor control
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

# Stepper motor sequence for full-step mode
step_sequence = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1]
]

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Helper function to set motor step
def set_step(step):
    GPIO.output(IN1, step[0])
    GPIO.output(IN2, step[1])
    GPIO.output(IN3, step[2])
    GPIO.output(IN4, step[3])

# Rotate motor
def rotate_motor(steps, delay=0.01):
    for _ in range(steps):
        for step in step_sequence:
            set_step(step)
            time.sleep(delay)

try:
    print("Rotating motor ...")
    rotate_motor(512)  # Rotate one full revolution (assuming 512 steps/rev)
    time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()