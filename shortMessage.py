#!/usr/bin/env python

import sys
import time

import scrollphat

scrollphat.set_brightness(50)

message = '^.^'

scrollphat.set_rotate(True)
scrollphat.write_string(message, 1)

while True:
    try:
        time.sleep(0.3)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
