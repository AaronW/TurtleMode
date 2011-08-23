#!/usr/bin/env python
# encoding: utf-8
"""
throttle.py

Created by Aaron on 2011-08-23

>>> tc.set_session(timeout=None, alt_speed_time_enabled=1)
>>> tc.set_session(timeout=None, alt_speed_enabled=False)
"""
from sys import argv
import transmissionrpc

script, first, second, third = argv

def main():
    pass

def throttleOn():
"""
Turtle-mode ON
"""
    tc.set_session(timeout=None, alt_speed_time_enabled=1)

def throttleOff():
    tc.set_session(timeout=None, alt_speed_enabled=False)

def scanHosts():
"""
Scan the priority addresses to see if they're online.
"""
    pass

def addClient(address, port):
"""
Add a transmission client address to remotely manage.
"""
    pass

def removeClient():
    pass

if __name__ == '__main__':
    main()
