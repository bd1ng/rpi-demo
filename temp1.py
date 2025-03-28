import adafruit_dht
import board
import time

sensor = adafruit_dht.DHT11(board.D26)

while True:
    temp_c = sensor.temperature
    humidity = sensor.humidity
    if humidity is not None and temp_c is not None:
        print(f'\nTemp in C: {temp_c}\nHumidity: {humidity}\n____________________')
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(2)