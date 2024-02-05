# ligoPhaseOne
<<<<<<< HEAD

This repo is a demo project for a monitor app that sends data to an [InfluxDB](https://www.influxdata.com) instance on a docker container.
This project assumes Docker is installed in the target machine.

## InfluxDB set-up

Run [an instance of InfluxDB](https://hub.docker.com/_/influxdb) on Docker:

```bash
docker run \
      -p 8086:8086 \
      -v myInfluxVolume:/var/lib/influxdb2 \
      influxdb:latest
```

With the InfluxDB container **running**, set-up your credentials, username, password and organization using the InfluxDB UI page.
When run locally, the setup page will be at http://localhost:8086. Copy the organization name to the `writeOneObject.py` script.

Create a bucket named `bucketPhaseOne` and a read-write token to access the bucket.
You should copy the token into the `writeOneObject.py` script.

## Install the Dependencies

Before running the application, install the dependencies:

```bash
python3 -m pip install influxdb-client
```

You may want to install the dependencies in a virtual environment.

## Run the application

When InfluxDB is setup, run the python application `writeOneObject.py`:

```bash
python3 writeOneObject.py
```

When the script ends you should see one new data point on InfluxDB GUI.

***

(c) Anika - 2023
=======
steps to use github:
git clone (for new device)
git status (to check status of branch)
git pull (brings remote to local)
git push (sends local to remote)
git commit 
git add
>>>>>>> 8e9946d (Send CPU and RAM data into bucketPhaseOne every second)
