import hashlib
import uuid

password = 'test_password'
salt = uuid.uuid4().hex
hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

print("geslo: " + password)
print("salt: " + salt)
print("hash: " + hashed_password)

password1 = 'test_passwor'
hashed_password1 = hashlib.sha512(password1.encode('utf-8') + salt.encode('utf-8')).hexdigest()

print("geslo: " + password1)
print("salt: " + salt)
print("hash: " + hashed_password1)

if hashed_password == hashed_password1:
    print("Enaka")
else:
    print("nista")

password2 = 'test_password'
hashed_password2 = hashlib.sha512(password2.encode('utf-8') + salt.encode('utf-8')).hexdigest()

if hashed_password == hashed_password2:
    print("Enaka")
else:
    print("nista")

print("geslo: " + password2)
print("salt: " + salt)
print("hash: " + hashed_password2)