#!/usr/bin/env python

from light import init,writeByte,cleanup 
import sys,time

if __name__ == '__main__':
    init(6,19,13)
    for item in sys.argv[1:]:
        writeByte(int(item))
        time.sleep(1) 
    cleanup()
    
