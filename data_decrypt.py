# -*- coding: utf-8 -*-

import os
from io import BytesIO
from itertools import cycle


class Decryptor():

    def __init__(self) -> None:
        ...

    @staticmethod
    def xor(data: bytearray, key: bytearray) -> bytes:

        return bytes(a ^ b for a, b in zip(data, cycle(key)))

    @classmethod
    def decrypt(self, path: str) -> bool:

        try:

            key = b'\x21\x0c\xed\x10\xd8\x81\xd7\xa3\xfa\x9b\xc9\x7a\xd3\xae\xeb\x6d\x98\x89\x31\x34\x2d\x39\x1e\x1f\xe1\xc4\x7c\xdd\x2d\xef\x26\x37\x7a\xfa\xbf\xd2\xd9\x60\x79\xf1\xca\x99\xd0\x32\xf7\xd8\x4d\x4e\xf6\xce\x45\xda\x0c\x67\x99\x09\xe6\x89\x75\x69\x5f\xd9\x12\xa2\x3e\x77\x74\x3c\xf5\xbe\x2e\x57\x64\x05\x1a\x71\x96\x62\x23\x25\x80\x63\xfc\xe7\xc6\xd4\xe7\xca\x76\x7d\x70\x3c\xcb\xe2\x31\xc5\xed\x03\x8d\xcc\xad\x1a\x75\x53\x4a\x61\x27\xb8\x30\xca\xeb\x73\xb4\xc6\xd6\xdb\xda\x00\x88\xe2\x11\x21\xef\xd5\xf3\x8a\x02\x1f\x06'
            stream = BytesIO(open(os.path.join(path, "data.pack"), "rb").read())

            with open(os.path.join(path, "data.pck"), "wb") as file:

                while True:

                    decrypted_bytes = self.xor(stream.read(len(key)), key)
                    file.write(decrypted_bytes)

                    if decrypted_bytes == b'':
                        break
                    
                return True
            
        except:

            return False