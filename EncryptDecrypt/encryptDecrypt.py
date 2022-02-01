from cryptography.fernet import Fernet

message = "Hello Wolrd"

key = Fernet.generate_key()

fernet = Fernet(key)

encryptedMessage = fernet.encrypt(message.encode())

print("Original: " + message)
print("Encypted: ", encryptedMessage)

decryptedMessage = fernet.decrypt(encryptedMessage).decode()

print("Decrypted: " + decryptedMessage)