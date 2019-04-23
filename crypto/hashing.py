from Crypto.Hash import SHA512

class Hash:

    def hash_string(self, string):
        hash = SHA512.new()
        return hash.hexdigest()
    
    def get_file_hash(self, filename, chunksize=24*1024):
        hash = SHA512.new()
        with open(filename, 'rb') as f:
            while True:
                chunk = f.read(chunksize)
                if len(chunk) == 0:
                    break
                hash.update(chunk)
        return hash.hexdigest()

