
import RPi.GPIO as gpio
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize the app with a service account, granting admin privileges
cred = credentials.Certificate('')

firebase_admin.initialize_app(cred,{
    'databaseURL': ''
})

ref = db.reference('/number')

# Read the data at the posts reference (this is a blocking operation)


def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def stop():
    init()
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,False)
    gpio.output(24,True)
    time.sleep(tf)
    gpio.cleanup()


def forward(tf):
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,True)
    gpio.output(24,False)
    time.sleep(tf)
    gpio.cleanup()


def rightturn():
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,False)
    gpio.output(24,True)
    time.sleep(1)
    gpio.cleanup()
    

def leftturn():
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,True)
    gpio.output(24,False)
    time.sleep(1)
    gpio.cleanup()
    

    
x=0
while x != 10:
    x=ref.get()
    if x == 'forward':
        forward(1)
    if x == 'reverse':
        reverse(1)
    if x == 'right':
        rightturn()
    if x == 'left':
        leftturn()
    if x == 'stop':
        stop()
