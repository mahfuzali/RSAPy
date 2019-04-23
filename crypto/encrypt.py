
import os, struct
from Crypto.Cipher import PKCS1_OAEP

class Encrypt:
    def encrypt(self, key, message):
        cipher = PKCS1_OAEP.new(key)
        ciphertext = cipher.encrypt(message)
        return ciphertext

    def decrypt(self, key, ciphertext):
        cipher = PKCS1_OAEP.new(key)
        message = cipher.decrypt(ciphertext)
        return message 
    
    def encrypt_file(self, key, in_filename, out_filename=None, chunksize=64*1024):
        if not out_filename:
            out_filename = in_filename + '.enc'

        filesize = os.path.getsize(in_filename)

        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))

                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += ' ' * (16 - len(chunk) % 16)

                    outfile.write(self.encrypt(key, chunk))

    def decrypt_file(self, key, in_filename, out_filename=None, chunksize=24*1024):
        if not out_filename:
            out_filename = os.path.splitext(in_filename)[0]

        with open(in_filename, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]

            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(self.decrypt(key, chunk))

                outfile.truncate(origsize)