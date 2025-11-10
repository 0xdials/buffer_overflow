# buffer_overflow

Collection of python3 scripts to use as a framework

### bad_characters.py
Framework for checking nearly all raw byte characters, null byte not included.


### byte_write.py
Quick and dirty way of writing a buffer string with a raw byte section to a file. Used to create malicious text files to be injested by the vulnerable application.


### exploit_framework.py
basic BoF exploit framework we all know and love.


### fuzzing_framework.py
fuzzing framework, its right in the title


### headers_BoF.py
A framework that includes http headers and sends the buffer via the data portion of the request. Python2 because combining strings with raw bytes in python3 is hell on earth. 
