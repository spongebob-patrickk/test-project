import hashlib
#x=input("please enter your word\n")
print("md5=",hashlib.md5(b"amir").hexdigest())
print("sha1=",hashlib.sha1(b"amir").hexdigest())