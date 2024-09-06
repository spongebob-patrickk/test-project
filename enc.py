import hashlib
x=input("please enter your word\n")
x_bytes = x.encode()
print("md5=",hashlib.md5(x_bytes).hexdigest())
print("sha1=",hashlib.sha1(x_bytes).hexdigest())
from cryptography.fernet import Fernet
key=Fernet.generate_key()
cipher_suit=Fernet(key)
#text=input("please enter your word\n")
cipher_text =cipher_suit.encrypt(x.encode())
print("encrypt text", cipher_text)
decrypted_text = cipher_suit.decrypt(cipher_text).decode()
print("encrypt text:", decrypted_text)