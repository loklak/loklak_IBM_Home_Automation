
import time
import sys
import pprint
import uuid
from uuid import getnode as get_mac

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(11,GPIO.IN)
ls='OFF'

try:
	import ibmiotf.application
	import ibmiotf.device
except ImportError:
	# This part is only required to run the sample from within the samples
	# directory when the module itself is not installed.
	#
	# If you have the module installed, just use "import ibmiotf.application" & "import ibmiotf.device"
	import os
	import inspect
	cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../../src")))
	if cmd_subfolder not in sys.path:
		sys.path.insert(0, cmd_subfolder)
	import ibmiotf.application
	import ibmiotf.device


def myAppEventCallback(event):
	print("Received live data from %s (%s) sent at %s: hello=%s x=%s" % (event.deviceId, event.deviceType, event.timestamp.strftime("%H:%M:%S"), data['hello'], data['x']))

def myCommandCallback(cmd):
  print("Command received: %s" % cmd.payload)
  if cmd.command == "on":
    print("Turning Light ON")
    GPIO.output(3,1)

  elif cmd.command == "off":  
    print("Turning Light OFF")
    GPIO.output(3,0) 

print       
#####################################
#FILL IN THESE DETAILS
#####################################     
organization = ""
deviceType = ""
deviceId = ""
appId = str(uuid.uuid4())
authMethod = "token"
authToken = ""

# Initialize the device client.
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
	print(str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
deviceCli.commandCallback = myCommandCallback
#x=0
while(1):
	lightStatus=GPIO.input(7)
	if lightStatus==0:
		ls='ON'
	else:
		ls='OFF'
	intruder=GPIO.input(11)
	data = { 'LightStatus': ls, 'Intruder': intruder}
        deviceCli.publishEvent("status", data)
	#x=x+1
	time.sleep(1)
		

# Disconnect the device and application from the cloud
deviceCli.disconnect()
#appCli.disconnect()

