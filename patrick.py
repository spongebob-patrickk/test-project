from cryptography.fernet import Fernet
key=Fernet.generate_key()
cipher_suit=Fernet(key)
text=input("please enter your word\n")
cipher_text =cipher_suit.encrypt(text.encode())
print("encrypt text", cipher_text)
decrypted_text = cipher_suit.decrypt(cipher_text).decode()
print("encrypt text:", decrypted_text)