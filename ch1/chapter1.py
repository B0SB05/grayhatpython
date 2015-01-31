from ctypes import * 

libc = CDLL('libc.so.6')
mymessage = "Hello World ! \n "

libc.printf('%s',mymessage)
