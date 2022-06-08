
from construction_assets import construction_vehicle
from mqtt_producer import mqtt_publisher

from threading import Thread, Event
from os import getenv
from time import sleep
from random import randint


def simulateVehicle(mqtthost, name):
    cv = construction_vehicle(name)

    mqttProducer = mqtt_publisher(address=mqtthost, port=1883, clientID=cv.construction_vehicle_ID)
    mqttProducer.connect_client()
    
    sleeptime = randint(5, 15)
    cvID = cv.returnConstructionVehicleID()
    while (True):
        

        mqttProducer.publish_to_topic(topic= str(cvID+"/speed"), data=cv.returnSpeed())
        mqttProducer.publish_to_topic(topic=str(cvID+"/temperature"), data=cv.returnTemperature())
        mqttProducer.publish_to_topic(topic=str(cvID+"/vibration"), data=cv.returnVibration())
        
        sleep(sleeptime)




    


if __name__ == "__main__":
    VEHICLE = getenv('VEHICLE', 1)
    BROKER = getenv('BROKER', "localhost")


    i =0
    while (i < int(VEHICLE)):
        vehicle = Thread(target=simulateVehicle, args=[BROKER, "RoadRoller"], daemon=True)
        vehicle.start()
        i = i +1
            
    Event().wait()
