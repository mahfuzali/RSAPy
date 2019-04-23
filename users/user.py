

class User:
    def __init__(self, pk, sk):
        self.pk = pk
        self.sk = sk
    
    def public_key(self):
        return self.pk
    
    def private_key(self):
        return self.sk