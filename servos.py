"""
AIPI 590
WEEK 3 - LAB 3
___________________
SERVO MOTOR CONTROL

- Clone this code to your Raspberry Pi
- Fill in the required functions
- Run your code
- If it passes, push back to Edstem with Git
"""

import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

"""
PIN CONFIGURATION:
Add the GPIO Pins for your H-Bridge here
"""
SERVO_PIN = 18  # PWM pin for duty cycle/angle control

"""
S0LUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def configure_servo():
    """
    Configure the GPIO pin for the servo motor.
    """
    ### BEGIN SOLUTION ###
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    ### END SOLUTION ###

"""
S0LUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def control_servo(angle):
    """
    Move the servo to a specific angle.
    - The function takes the 'angle' argument
        - angle (int): Desired angle to set the servo (0 to 180 degrees).
    - Initialize the PWM pin at 50Hz
    - Start the PWM
    - Convert the 'angle' to duty cycle
    - Change the PWM duty cycle to the converted value.
    - Pause the code for 1 second
    - Stop the PWM.
    """
    ### BEGIN SOLUTION ###
    
    servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz PWM frequency for servos
    servo.start(0)  # Start PWM with 0% duty cycle    
    duty = 2.5 + (angle / 180.0) * 10
    servo.ChangeDutyCycle(duty)
    time.sleep(1)  # Allow time to reach the position
    servo.stop()
 
    ### END SOLUTION ###

"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
ANY CODE BELOW THIS LINE
___________________
"""

def test_servo():
    """
    Tests the servo motor by moving it to 0, 90, and 180 degrees.
    """
    try:
        print("Testing servo motor control...")

        print("Moving servo to 0 degrees...")
        control_servo(0)
        time.sleep(1)

        print("Moving servo to 90 degrees...")
        control_servo(90)
        time.sleep(1)

        print("Moving servo to 180 degrees...")
        control_servo(180)
        time.sleep(1)

        print("Returning servo to 0 degrees...")
        control_servo(0)

        print("All tests passed!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()

try:
    # Configure the servo motor
    configure_servo()

    # Test the servo
    test_servo()

except KeyboardInterrupt:
    print("Test interrupted by user.")
    GPIO.cleanup()

