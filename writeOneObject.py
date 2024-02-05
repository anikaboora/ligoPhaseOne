#import required libraries
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

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


#create new object
p = influxdb_client.Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
#store to database
write_api.write(bucket=bucket, org=org, record=p)
