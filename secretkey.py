import os
import base64
import secrets
# Gera uma chave segura de 32 bytes
secret_key = base64.b64encode(os.urandom(32)).decode('utf-8')
print('SECRET_KEY')
print(secret_key)

