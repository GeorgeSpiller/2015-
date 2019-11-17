from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import glob, os

print("Will look for files with the .encrypted extention")
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
print(dir_path)
for file in glob.glob("*.encrypted"): 
    with open(file, "rb") as to_Decrypt:
        encrypted = to_Decrypt.read()



print("Type private key in manually or use a .pem file?")
typeKey = input("Type in Manually? true/false>>")
if typeKey[0] == "t":
    typeKey = input("privateKey>>")
    private_key = serialization.load_pem_private_key(
            typeKey,
            backend=default_backend()
        )
else:
    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
            )
original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

print(original_message)
