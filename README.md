# MQTT Simulators

This repository will allow you to spin up different MQTT simulators producing fake IoT data for different scenarios. 

## Scenarios

### Emergency Generators (Payload: JSON)
Each generator will write to its own MQTT topic the following values: 

1. Load
2. Voltage
3. Fuel Level
4. Temperature

The payload will look like this:

```json
{"generatorID": "generator1", "lat": 40.68066, "lon": -73.47429, "temperature": 186, "power": 186, "load": 2, "fuel": 277}
```

### Construction Yard (Payload: Single Value) (WIP)
Each vehicle will write to its own MQTT topic and subtopics the following values: 

1. Speed
2. Temperature
3. Vibration

The payload will look like this:

```
RoadRoller/Temperature 24.1
RoadRoller/Speed 12
RoadRoller/Vibration 1.00394
```

To run this construction site example make sure to uncomment the correct sections of the MQTT Input plugin in the the [telegraf.conf](telegraf/telegraf.conf) and [docker-compose.yml](docker-compose.yml). Also make sure to replace the commands below with the right pathways, i.e:

```bash
docker build -t construction-site:latest ./construction_site 
```


## Setup

There are two ways to setup this Sim: Docker + Locally


### Option 1: Docker (Recommended)


1. Clone this repo to your system

```bash
git clone https://github.com/InfluxCommunity/MQTT_Simulators.git
```

2. Build the simulator docker image:

```bash
docker build emergency_generator/. -t emergency-generator:latest
```

3. Deploy the docker-compose file:

```bash
docker-compose up -d
```

### Option 2: Locally

1. Install the Mosquitto MQTT Broker onto your device:

```bash
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudp apt-get install mosquitto
```

2. Start the Mosquitto broker:

```bash
sudo systemctl enable Mosquitto
sudo systemctl start Mosquitto
```

3. Clone this repo to your local system:

```bash
git clone https://github.com/Jayclifford345/mqtt-emergency-generator.git
```

4. Naviage to this folder

```bash
cd mqtt-emergency-generator/tree/master/generator_simulator
```

5. Install the pip requirements

```bash
RUN python3 -m pip install --no-cache-dir -r requirements.txt
```

6. Setup your enviroment variables

```bash
export GENERATORS=3
export BROKER=localhost
```

7. Run the the simulator

```bash
python3 src/emergency_generator.py
```


### Edge to Cloud Replication
This section will teach you how to configure InfluxDB OSS to send data to InfluxDB Cloud.

To use this option, first uncomment the InfluxDB Output section of [telegraf.conf](telegraf/telegraf.conf) and uncomment out the current InfluxDB Output section which is configured to write directly to InfluxDB Cloud. 

1. Create a remote connection

```bash
influx remote create --name cloud --remote-url https://us-east-1-1.aws.cloud2.influxdata.com --remote-org-id <ORG_ID> --remote-api-token <CLOUD_TOKEN>
```

2. Create a replication between a local bucket and a cloud bucket
```bash
influx replication create --local-bucket-id 1f158076adc417f5 --remote-bucket-id 621a1bf27327b2fc --remote-id 0947082f21c3e000  --name edge_to_cloud
```



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
