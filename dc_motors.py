"""
AIPI 590
WEEK 3 - LAB 2
___________________
DC MOTOR CONTROL WITH H-BRIDGE

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
Make sure your ENA is plugged into a PWM compatible GPIO
"""
ENA =   18
IN1 =   17
IN2 =   27

"""
S0LUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def configure_motor():
    """
    Configure GPIO pins for the H-Bridge motor driver as outputs.
    """
    ### BEGIN SOLUTION ###
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    ### END SOLUTION ###

"""
S0LUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def motor_control(direction, speed):
    """
    Control the motor's direction and speed.
    - This function takes 'direction' and 'speed' arguments.
        - direction (str): 'forward' or 'reverse'.
        - speed (int): PWM duty cycle speed percentage (0 to 100).
    - Create a variable for 'pwm' and initialize the GPIO pin at 100 Hz.
    - Once initialized, start the pwm.
    - Create an 'if' statement to check if the direction arg is set to 'forward' or 'reverse'.
        - If it's 'forward', set IN1 to HIGH and IN2 to LOW
        - If it's 'reverse', set IN1 to LOW and IN2 to HIGH
        - Else, print out an error.
    - Change the PWM Duty cycle to the 'speed' arg.
    - Pause the code for 2 seconds to let the motor run.
    - Stop the PWM
    """
    ### BEGIN SOLUTION ###
    pwm = GPIO.PWM(ENA, 100)  # 100Hz PWM frequency
    pwm.start(0)

    if direction == 'forward':
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        pwm.ChangeDutyCycle(speed)
    
    elif direction == 'reverse':
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        pwm.ChangeDutyCycle(speed) 
    
    else: 
        print("darn that didn't work")       

    time.sleep(2)
    pwm.stop()

    ### END SOLUTION ###

"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
ANY CODE BELOW THIS LINE
___________________
"""

def test_motor():
    """
    Tests the motor by performing forward and reverse rotations at different speeds.
    """
    try:
        print("Testing DC motor control with H-Bridge...")

        print("Running motor forward at 50% speed...")
        motor_control('forward', 50)
        time.sleep(1)  # Pause between tests

        print("Running motor reverse at 75% speed...")
        motor_control('reverse', 75)
        time.sleep(1)

        print("Running motor forward at 100% speed...")
        motor_control('forward', 100)

        print("All tests passed!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()

try:
    # Configure motor pins
    configure_motor()

    # Test the motor
    test_motor()

except KeyboardInterrupt:
    print("Test interrupted by user.")
    GPIO.cleanup()

