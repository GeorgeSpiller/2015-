from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

rawMessage = input("Paste message to be encrypted:")

message = rawMessage.encode()
print(message)

print("Type public key in manually or use a .pem file?")
typeKey = input("Type in Manually? true/false>>")
if typeKey[0] == "t":
    typeKey = input("publicKey>>")
    public_key = serialization.load_pem_public_key(
            typeKey,
            backend=default_backend()
        )
else:
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

with open('encryptedFile.encrypted', 'wb') as f:
    f.write(encrypted)
