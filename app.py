import random
import string

def genera_password(lunghezza=12):
    caratteri = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caratteri) for i in range(lunghezza))
    return password

print(f"La tua nuova password sicura è: {genera_password()}")
