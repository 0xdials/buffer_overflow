# buffer_overflow

Collection of python2/3 scripts to use as a framework for OSCP. 
(Note that working with raw bytes in python3 is not my favorite so a number of scripts use python)


### bad_characters.py
Framework for checking nearly all raw byte characters, null byte not included.


### byte_write.py
Quick and dirty way of writing a buffer string with a raw byte section to a file. Used to create malicious text files to be injested by the vulnerable application.


### exploit_framework.py
basic BoF exploit framework we all know and love.


### fuzzing_framework.py
basic fuzzing framework we all know and love.


### headers_BoF.py
A framework that includes http headers and sends the buffer via the data portion of the HTTP request. Python2 because combining strings with raw bytes in python3 is an actual nightmare. 
