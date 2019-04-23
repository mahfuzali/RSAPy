from crypto import hashing
from users import user
from crypto import keys
from crypto import signature
from crypto import encrypt

def main():
    h = hashing.Hash()
    k = keys.Key()
    s = signature.Signature()
    e = encrypt.Encrypt()

    a = k.generate_keys()
    b = k.generate_keys()

    alice = user.User(a['publicKey'], a['privateKey'])
    bob = user.User(b['publicKey'], b['privateKey'])

    file = "doc.txt"
    signed = s.sign(h.get_file_hash(file), k.read_key(alice.private_key))

    e.encrypt(k.read_key(bob.public_key), file)
    

    e.decrypt(k.read_key(bob.private_key), file + ".enc")

    verify = s.verify(h.get_file_hash(file), signed, k.read_key(alice.public_key))



if __name__ == '__main__':
    main()