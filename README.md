# IoT
Internet of Things based home automation project using IBM IoTF platform.
Please follow the tutorial at:  http://diyhacking.com/iot-home-automation-ibm-iotf/

This repository consists of two scripts:
client.py - This python script runs on the Raspberry Pi. It accepts command from the server 
and pushes data from a PIR motion sensor to the IBM IoTF platform.

server.py - This python script runs on the web server or laptop and issues commands that control
the GPIO pins on the Raspberry Pi. Before running this script on the server, you should install
the corresponding packages for IBM IoTF. The instructions can be found here: 
https://docs.internetofthings.ibmcloud.com/libraries/python.html
