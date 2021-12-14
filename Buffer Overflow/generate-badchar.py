#!/usr/bin/env python3
from __future__ import print_function

#tart with 00 and add any others you find
bad = "00 04 38 72 d9".split()

#turns them into a nice string to copy into python
print("badchars = ")
for x in range(1, 256):
	if "{:02x}".format(x) not in bad: 
		print("\\x" + "{:02x}".format(x), end='')

#creates a nice string to use in Mona
asd=''
for byte in bad:
	asd+=("\\x{}".format(byte))
print("\n\n!mona bytearray -b "+asd)
print("!mona compare -f bytearray.bin -a ESP")
print("!mona jmp -r esp -cpb \""+asd+'"')
