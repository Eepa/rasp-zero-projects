#!/usr/bin/env python

import sys
import time
import scrollphat
from smallNumbersFont import smallNumbersFont

def write_string_as_is(text, offset = 0):
    for char in text:
        if ord(char) not in smallNumbersFont:
            scrollphat.set_col(offset, 0)
            offset += 1
        else:
            charInFont = smallNumbersFont[ord(char)]
            for i in range(0, len(charInFont)):
                scrollphat.set_col(offset, charInFont[i])
                offset += 1
    scrollphat.update()            
            
scrollphat.set_brightness(10)

message = "- 2 4 'C"

scrollphat.set_rotate(True)
write_string_as_is(message)

while True:
    try:
        time.sleep(0.3)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
