from cryptography.fernet import Fernet

# Comment out below to encrypt the file

key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('SampleSheet.csv', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open('SampleSheet.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# Comment out below to decrypt the file

# with open('filekey.key', 'rb') as filekey:
#     key = filekey.read()

# fernet = Fernet(key)

# with open('SampleSheet.csv', 'rb') as enc_file:
#     encrypted = enc_file.read()

# decrypted = fernet.decrypt(encrypted)

# with open('SampleSheet.csv', 'wb') as dec_file:
#     dec_file.write(decrypted)