from Crypto.Cipher import DES
import os

# Ppad the data to make it a multiple of 8 bytes 
def pad_data(data):
    while len(data) % 8 != 0:
        data += b' '  # Add space characters to pad
    return data

# Encrypt the plaintext file using DES
def encrypt_file(key, filename):
    with open(filename, 'rb') as f:
        plaintext = f.read()
    
    # Padding the plaintext
    plaintext = pad_data(plaintext)
    
    # Creating DES cipher
    des = DES.new(key, DES.MODE_ECB)
    
    # Encrypting the data
    ciphertext = des.encrypt(plaintext)
    
    # Converting the encrypted data to hexadecimal
    hex_ciphertext = ciphertext.hex()
    
    # Writing the hex-encoded encrypted data to cipher.txt
    with open('cipher.txt', 'w') as f:
        f.write(hex_ciphertext)
    
    print("Encryption complete. Encrypted hex text saved to cipher.txt")

# Function to decrypt the ciphertext file using DES
def decrypt_file(key, filename):
    # Reading hex-encoded ciphertext from the file
    with open(filename, 'r') as f:
        hex_ciphertext = f.read()
    
    # Converting the hex-encoded ciphertext back to bytes
    ciphertext = bytes.fromhex(hex_ciphertext)
    
    # Creating DES cipher
    des = DES.new(key, DES.MODE_ECB)
    
    # Decrypting the data
    decrypted_data = des.decrypt(ciphertext)
    
    # Writing the decrypted data to decrypted.txt
    with open('decrypted.txt', 'wb') as f:
        f.write(decrypted_data.strip())  # Remove padding
    
    print("Decryption complete. Decrypted text saved to decrypted.txt")

# Convert key from binary or hexadecimal to bytes
def get_key_in_bytes(key_input, key_format):
    if key_format.lower() == 'binary':
        return int(key_input, 2).to_bytes(8, 'big')  
    elif key_format.lower() == 'hex':
        return bytes.fromhex(key_input)  
    else:
        print("Invalid format. Please enter 'binary' or 'hexadecimal'.")
        return None

if __name__ == "__main__":
    key_format = input("Enter key format (binary or hex): ").strip()
    key_input = input(f"Enter your {key_format} key (must be 64 bits): ").strip()
    key = get_key_in_bytes(key_input, key_format)
    if key is None or len(key) != 8:
        print("Error: Key must be exactly 64 bits (8 bytes) long!")
    else:
        filename = input("Enter the file name (plain.txt for encryption, cipher.txt for decryption): ")
        if filename == 'plain.txt':
            encrypt_file(key, filename)  
        elif filename == 'cipher.txt':
            decrypt_file(key, filename) 
        else:
            print("Invalid file. Please provide either 'plain.txt' or 'cipher.txt'.")
