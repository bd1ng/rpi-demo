"""
AIPI 590
WEEK 3 - LAB 4
___________________
RELAY CONTROL WITH SRD-05vDC-LS-C

- Clone this code to your Raspberry Pi
- Fill in the required functions
- Run your code
- If it passes, push back to Edstem with Git

The relay will control a DC motor connected to a 5V power source.
"""

import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

"""
PIN CONFIGURATION:
Add the GPIO Pins for your H-Bridge here
"""

RELAY_PIN = 16  # GPIO pin connected to the relay signal pin

"""
S0LUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""

def configure_relay():
    """
    Configure the GPIO pin for the relay control.
    """
    ### BEGIN SOLUTION ###

    GPIO.setup(RELAY_PIN, GPIO.OUT)

    ### END SOLUTION ###

def control_relay(state):
    """
    Control the relay to turn the motor on or off.
    - This function is passed the argument of 'state'
        - state (str): 'on' to activate the relay (turn on motor), 
          'off' to deactivate the relay (turn off motor).
    - Create an 'if' statement that checks to see if the 'state'
      variable is set to 'on' or 'off'
    - To turn the relay 'on', set the GPIO output to HIGH
    - To turn the relay 'off', set the variable output to LOW
    """
    ### BEGIN SOLUTION ###

    if state == 'on':
        GPIO.output(RELAY_PIN, GPIO.HIGH) 
        time.sleep(5)

    elif state == 'off':   
        GPIO.output(RELAY_PIN, GPIO.LOW) 

    else:
        print("bummer that didn't work")

    ### END SOLUTION ###

"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
ANY CODE BELOW THIS LINE
___________________
"""

def test_relay():
    """
    Tests the relay by turning the motor on and off.
    """
    try:
        print("Testing relay control...")

        print("Turning motor ON...")
        control_relay('on')
        time.sleep(2)

        print("Turning motor OFF...")
        control_relay('off')
        time.sleep(2)

        print("Turning motor ON again...")
        control_relay('on')
        time.sleep(2)

        print("Turning motor OFF again...")
        control_relay('off')

        print("All tests passed!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()

try:
    # Configure relay pin
    configure_relay()

    # Test the relay
    test_relay()

except KeyboardInterrupt:
    print("Test interrupted by user.")
    GPIO.cleanup()

