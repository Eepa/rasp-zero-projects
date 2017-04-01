#!/usr/bin/env python

import sys
import time

import scrollphat


scrollphat.set_brightness(2)

message = 'NYT ON NUKKUMAAN MENON AIKA!!!!'

scrollphat.set_rotate(True)
scrollphat.write_string(message, 11)

while True:
    try:
        scrollphat.scroll()
        time.sleep(0.05)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
