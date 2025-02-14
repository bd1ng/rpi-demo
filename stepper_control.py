"""
AIPI 590
WEEK 3 - LAB 1
___________________
STEPPER MOTOR CONTROL WITH L298N DRIVER

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
Add the GPIO Pins for your L298N Stepper controller here
"""
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

"""
FORWARD STEP SEQUENCE:
Define a clockwise stepper motor sequence
"""
forward = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1],
]

"""
REVERSE STEP SEQUENCE:
Define a counter-clockwise stepper motor sequence
"""
reverse = [
    [1,0,0,1],
    [0,0,1,1],
    [0,1,1,0],
    [1,1,0,0],
]

"""
S0LUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def configure_motor_pins():
    """
    Configure GPIO pins for stepper motor control.
    - Setup IN1, IN2, IN3, and IN4 as output pins
    """
    ### BEGIN SOLUTION ###

    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

    ### END SOLUTION ###

"""
S0LUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def step_forward(delay):
    """
    Perform one step of the motor sequence.
    -This function is passed the 'delay' (float) variable.
    -'delay' represents the time delay between steps.
    -You will need to create a 'for' loop that iterates through
     each step in the 'forward' sequence.
    -Within the 'for' loop you should send the step information
     to the motor pins, and then delay the loop using the 'delay' variable.
    """
    ### BEGIN SOLUTION ###
    
    def set_pins(step):
        GPIO.output(IN1, step[0])
        GPIO.output(IN2, step[1])
        GPIO.output(IN3, step[2])
        GPIO.output(IN4, step[3])
    
    for step in forward:
        set_pins(step)
        time.sleep(delay)


    ### END SOLUTION ###

"""
S0LUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def step_backward(delay):
    """
    Perform one step of the motor sequence.
    -This function is passed the 'delay' (float) variable.
    -'delay' represents the time delay between steps.
    -You will need to create a 'for' loop that iterates through
     each step in the 'reverse' sequence.
    -Within the 'for' loop you should send the step information
     to the motor pins, and then delay the loop using the 'delay' variable.
    """
    ### BEGIN SOLUTION ###
    def set_pins(step):
        GPIO.output(IN1, step[0])
        GPIO.output(IN2, step[1])
        GPIO.output(IN3, step[2])
        GPIO.output(IN4, step[3])
    
    for step in reverse:
        set_pins(step)
        time.sleep(delay)
    ### END SOLUTION ###


"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
ANY CODE BELOW THIS LINE
___________________
"""

def test_motor():
    """
    Tests the motor by performing a forward and backward rotation.
    """
    try:
        print("Testing stepper motor...")
        for _ in range(512):  # Forward rotation (512 steps for one full rotation)
            step_forward(0.003)
        print("Forward rotation complete.")

        time.sleep(1)  # Pause before reversing

        print("Testing reverse rotation...")
        for _ in range(512):  # Reverse rotation
            step_backward(0.003)
        print("Reverse rotation complete.")

        print("All tests passed!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()

try:
    # Configure motor pins
    configure_motor_pins()

    # Test the motor
    test_motor()

except KeyboardInterrupt:
    print("Test interrupted by user.")
    GPIO.cleanup()

