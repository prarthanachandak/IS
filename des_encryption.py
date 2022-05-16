from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8) # 8 bytes =  8*8 = 64 bits

def encrypt(msg):
    cipher = DES.new(key,DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext , tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    #print(nonce)
    #print(tag)
    return nonce,ciphertext,tag

def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key,DES.MODE_EAX,nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try :
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce, ciphertext, tag = encrypt(input("Enter a message : "))
plainttext = decrypt(nonce,ciphertext,tag)

print(f'Cipher text : {ciphertext}')

if not plainttext:
    print("Message is corrupted!")
else:
    print(f'Plain text :{plainttext}')
