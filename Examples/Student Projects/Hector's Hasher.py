# Hector's Hasher
# Hector B.
# UM Cyber Bootcamp Student May 2021

import hashlib
import random
password = input("Enter password: ")
md5hash = hashlib.md5(password.encode())
print(f"MD5 Hash is: {md5hash.hexdigest()}")
sha512hash = hashlib.sha512(password.encode())
print(f"Sha512 Hash is: {sha512hash.hexdigest()}")
blake2bhash = hashlib.blake2b(password.encode())
print(f"Blake2b hash is: {blake2bhash.hexdigest()}")
sha1 = hashlib.sha1(password.encode())
print(f"Sha1 is: {sha1.hexdigest()}")
sha256 = hashlib.sha256(password.encode())
print(f"Sha256 hash is: {sha256.hexdigest()}")
sha384 = hashlib.sha384(password.encode())
print(f"Sha384 hash is: {sha384.hexdigest()}")
sha3_256 = hashlib.sha3_256(password.encode())
print(f"Sha3_256 hash is: {sha3_256.hexdigest()}")
sha3_224 = hashlib.sha3_224(password.encode())
print(f"sha3_224 hash is: {sha3_224.hexdigest()}")
sha3_512 = hashlib.sha3_512(password.encode())
print(f"Sha3_512 hash is: {sha3_512.hexdigest()}")
randomhash = [md5hash.hexdigest(), sha3_512.hexdigest(),blake2bhash.hexdigest(),sha1.hexdigest(), sha256.hexdigest(), sha384.hexdigest(), sha3_256.hexdigest(), sha3_224.hexdigest(), sha3_512.hexdigest()]
print(f"The random Hash chosen is: {random.choice(randomhash)}")