#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def init(DS=6,SHCP=19,STCP=13):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(DS,GPIO.OUT)
    GPIO.setup(SHCP,GPIO.OUT)
    GPIO.setup(STCP,GPIO.OUT)

    GPIO.output(DS,GPIO.LOW)
    GPIO.output(SHCP,GPIO.LOW)
    GPIO.output(STCP,GPIO.LOW)


def writeByte(data,DS=6,SHCP=19,STCP=13):
    for i in range(0,8):
        GPIO.output(DS,(data>>i)&0x01)
        GPIO.output(SHCP,GPIO.LOW)
        GPIO.output(SHCP,GPIO.HIGH)
    GPIO.output(STCP,GPIO.LOW)
    GPIO.output(STCP,GPIO.HIGH)

def cleanup():
    GPIO.cleanup()

if __name__=="__main__":
    try:
        init()
        while True:
            for i in [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]:
                writeByte(i)
                time.sleep(0.1)
            writeByte(0xff)
            time.sleep(0.1)

    except KeyboardInterrupt:
        print "except"
        writeByte(0x00)
        cleanup()

