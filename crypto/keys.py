from Crypto.PublicKey import RSA

class Key:

    def generate_keys(self):
        generator = RSA.generate(4096, e=65537)
        publicKey = generator.publickey().exportKey("PEM")
        privateKey = generator.exportKey("PEM")
        return {'publicKey': publicKey, 'privateKey': privateKey}

    def read_key(self, k):
        try:
            key = RSA.import_key(k)
            return key
        except IOError as e:
            print(e)

    def read_key_from_file(self, fileName):
        try:
            f = open(fileName,'r')
            key = RSA.import_key(f.read())
            return key
        except IOError as e:
            print(e)
  
    def save_key(self, fileName, key):
        try:
            f = open(fileName,'wb')
            f.write(key)
            f.close()
        except IOError as e:
            print(e)