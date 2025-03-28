"""
AIPI 590
WEEK 4 - LAB 4
___________________
DHT11 SENSOR DATA STREAMING TO INFLUXDB

- Clone this code to your Raspberry Pi
- Complete the required function to log data to InfluxDB
- Push back to Edstem with Git

"""

import influxdb_client
import os
import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import adafruit_dht
import board
from datetime import datetime

"""
DHT11 CONFIGURATION:
The SENSOR_PIN variable will point to the GPIO pin
using the Adafruit 'board' library. The pin number will be preceeded with 'D'
Then create a variable for the sensor.
"""
SENSOR_PIN = 26
sensor = adafruit_dht.DHT11(board.D26)

"""
INFLUX DB CONFIGURATION:
Configure variables for your
- InfluxDB token (should be stored as an environment variable)
- Configured ORG name
- Your VM URL
- Configured Buckett name
"""

INFLUXDB_TOKEN = os.environ.get("INFLUXDB_TOKEN")
INFLUXDB_ORG = "aipi_class"
INFLUXDB_URL = "http://vcm-46240.vm.duke.edu:8086"
INFLUXDB_BUCKET = "stuff"

"""
API CONFIGURATION:
Initialize the InfluxDBCLient using the URL, Token and Org variables
"""
write_client = influxdb_client.InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = write_client.write_api(write_options=SYNCHRONOUS)

"""
SOLUTION FUNCTION:
# ADD YOUR SOLUTION TO THE DESIGNATED AREA
# DO NOT ALTER THE SURROUNDING CODE
"""


def log_to_influxdb():
    """
    Logs temperature and humidity data to InfluxDB.
    - Capture the humidity from the sensor as a variable
    - Capture the temperature from the sensor as a variable
    - Check to see if the variables are None.
    - If not, print out the variable contents and log to InfluxDB
        - Create a data point for InfluxDB
        - Use the 'write_api.write' method to log it.
    """
    ### BEGIN SOLUTION ###

    while True:
        temp_c = sensor.temperature
        humidity = sensor.humidity
        if humidity is not None and temp_c is not None:
            print(f'\nTemp in C: {temp_c}\nHumidity: {humidity}\n____________________')
            point = (
                Point("indoor1")
                .tag("dht11", "class")
                .field("temp", temp_c)
                .field("humidity", humidity)
            )
            write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)
        else:
            print("Sensor failure. Check wiring.")
        time.sleep(2)
    
    ### END SOLUTION ###


"""
TEST FUNCTION:
DO NOT REMOVE OR EDIT
ANY CODE BELOW THIS LINE
___________________
"""


def main():
    """
    Main function to read data from the DHT11 sensor and log it to InfluxDB.
    """
    print("Starting DHT11 Sensor Data Logging to InfluxDB...")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            try:
                log_to_influxdb()

            except RuntimeError as e:
                # Handle intermittent sensor reading errors
                print(f"Sensor reading error: {e}")

            # Wait before the next reading
            time.sleep(2)

    except KeyboardInterrupt:
        print("Exiting program. Goodbye!")
    finally:
        sensor.exit()


# Run the main function
if __name__ == "__main__":
    main()

