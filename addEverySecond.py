#import required libraries
import time
import psutil
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    return cpu_usage, ram_usage

def main():
    #initializing based on influx components
    bucket = "bucketPhaseOne"
    org = "myOrg"
    token = "ceLwt-nVFEV5ZQiZMcgrxtcA-1VbJT9AXsEXhrlz2n5glbNWdccJ9fLDV1cKcWb7B3kAghEfXOR7b69Jg7Q5Bg=="
    url = "http://localhost:8086"

    #initialize client
    client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
    )

    #initialize write_api
    write_api = client.write_api(write_options=SYNCHRONOUS)

    while True:
        #get values from function
        cpu_usage, ram_usage = get_system_metrics()
        #create new object
        p = influxdb_client.Point("my_measurement").tag("location", "Pasadena").field("cpu_usage", cpu_usage).field("ram_usage", ram_usage)
        #store to database
        write_api.write(bucket=bucket, org=org, record=p)
        #wait one second
        time.sleep(1)

main()