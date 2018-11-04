#!/usr/bin/env python

from light import init,writeByte,cleanup
import sys,time,random

if __name__=="__main__":
    init()
    try:
        while (True):
            byte=random.randint(1,255)
            writeByte(byte)
            time.sleep(0.1)
    except KeyboardInterrupt:
        writeByte(0xff)
        cleanup()
