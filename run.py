import encrypt as e
import decrypt as d
import genKey as g

# Prompt the user to enter the plaintext
plaintext = input("\nEnter the text to encrypt: \n")

# Generate a key of the same length as the plaintext
key = g.genKey(len(plaintext))

# Encrypt and decrypt the plaintext
encrypted_text = e.encrypt(plaintext, key)
decrypted_text = d.decrypt(encrypted_text, key)

print(f"\nEncrypting : {plaintext} \nKeywoard   : {key} \nEncrypted  : {encrypted_text}")
print(f"\nDecrypting using the same key: \n{decrypted_text}")
