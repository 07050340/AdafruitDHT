#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
import time
import httplib as http
import urllib
import json
import Adafruit_DHT
import requests
import socket
import threading
import logging
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
deviceId = "D3eBcmo7"
deviceKey ="ZA0VJimQcZqVZrl0"

def get():
    # Query command server's IP & port
    url = 'https://api.mediatek.com/mcs/v2/devices/D3eBcmo7/datachannels/LEDControl/datapoints'
    headers = {"content-type":"application/json","deviceKey": deviceKey }
    r = requests.get(url,headers = headers)
    value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
    return value
while True:
    # Note the LED is "reversed" to the pin's GPIO status.
    # So we reverse it here.
    if get():
        LEDon = GPIO.output(17, 1)
    else:
	LEDoff = GPIO.output(17,0)
