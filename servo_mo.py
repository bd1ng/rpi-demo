import RPi.GPIO as GPIO
import time

# GPIO Pin Definitions
SERVO_PIN = 21  # PWM-capable GPIO pin

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# PWM Setup
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz PWM frequency for servos
servo.start(0)  # Start PWM with 0% duty cycle

def set_angle(angle):
    """
    Moves the servo to the specified angle.
    Args:
        angle (int): Desired angle (0 to 180 degrees)
    """
    duty = 2 + (angle / 18)  # Map angle to duty cycle
    GPIO.output(SERVO_PIN, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)  # Allow time to reach the position
    GPIO.output(SERVO_PIN, False)
    servo.ChangeDutyCycle(0)

try:
    print("Moving servo to 0°...")
    set_angle(0)  # Move to 0°
    time.sleep(1)

    print("Moving servo to 90°...")
    set_angle(90)  # Move to 90°
    time.sleep(1)

    print("Moving servo to 180°...")
    set_angle(180)  # Move to 180°
    time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    servo.stop()
    GPIO.cleanup()