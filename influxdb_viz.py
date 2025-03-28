from influxdb_client import InfluxDBClient
import pandas as pd
import matplotlib.pyplot as plt
import time
import os

# InfluxDB connection details
token = os.environ.get("INFLUXDB_TOKEN")
org = "aipi_class"
url = "http://vcm-46240.vm.duke.edu:8086"
bucket = "stuff"


# Initialize the InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)

# Create a query variable to pull the desired data
query =f'''from(bucket: "stuff")
  |> range(start: -1h)  // Adjust the time range as needed
  |> filter(fn: (r) => r._measurement == "indoor1")  // Replace "stuff" with the actual measurement name if different
  |> filter(fn: (r) => r._field == "temp")
  |> aggregateWindow(every: 1m, fn: mean, createEmpty: false)  // Adjust window size as needed
  |> yield(name: "mean")
'''

while True:
    # Query the data
    tables = client.query_api().query(query)

    # Convert results to a Pandas DataFrame
    data = []
    for table in tables:
        for record in table.records:
            data.append({
                "time": record.get_time(),
                "field": record.get_field(),
                "value": record.get_value()
            })

    df = pd.DataFrame(data)

    df.to_csv("dht11_data.csv", index=False)

    # Calculate statistics
    print(df.groupby("field")["value"].describe())