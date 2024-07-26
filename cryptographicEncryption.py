import random
import string
import math


class Message:
    """Base class for messages."""
    
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return self.message
    
    def apply_cipher(self, cipher):
        """Applies the given cipher to the message."""
        self.message = cipher.encrypt(self.message)
        

class plaintextMsg(Message):
    """Subclass of Message for plaintext messages."""
    
    def encrypt(self, cipher):
        """Encrypts the message using the given cipher."""
        self.apply_cipher(cipher)
        return ciphertextMsg(self.message)
    
    
class ciphertextMsg(Message):
    """Subclass of Message for ciphertext messages."""
    
    def decrypt(self, cipher):
        """Decrypts the message using the given cipher."""
        self.apply_cipher(cipher)
        return plaintextMsg(self.message)
    

class SubstitutionCipher:
    """Class implementing the Substitution cipher."""
    
    def __init__(self):
        self.mapping = {}
        chars = list(string.ascii_lowercase)
        random.shuffle(chars)
        for i, c in enumerate(string.ascii_lowercase):
            self.mapping[c] = chars[i]
            
    def encrypt(self, message):
        return ''.join([self.mapping.get(c.lower(), c) for c in message])
    
    
class PlayfairCipher:
    """Class implementing the Playfair cipher."""
    
    def __init__(self):
        self.alphabet = string.ascii_lowercase.replace('j', 'i')
        self.matrix = []
        for i in range(5):
            row = []
            for j in range(5):
                row.append(self.alphabet[i*5+j])
            self.matrix.append(row)
            
    def find_char(self, char):
        """Returns the row and column of the given character in the matrix."""
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == char:
                    return i, j
        return None
    
    def encrypt(self, message):
        # Pad message with 'x' if necessary
        if len(message) % 2 != 0:
            message += 'x'
        # Split message into pairs of characters
        pairs = [message[i:i+2] for i in range(0, len(message), 2)]
        # Apply cipher to each pair
        result = ''
        for pair in pairs:
            c1, c2 = pair
            i1, j1 = self.find_char(c1)
            i2, j2 = self.find_char(c2)
            if i1 == i2:
                j1 = (j1 + 1) % 5
                j2 = (j2 + 1) % 5
            elif j1 == j2:
                i1 = (i1 + 1) % 5
                i2 = (i2 + 1) % 5
            else:
                j1, j2 = j2, j1
            result += self.matrix[i1][j1] + self.matrix[i2][j2]
        return result
    
    
class CaesarCipher:
    """Class implementing the Caesar cipher."""
    
    def __init__(self):
        self.shift = random.randint(1, 25)
        
    def encrypt(self, message):
        result = ''
        for c in message:
            if c.isalpha():
                if c.isupper():
                    result += chr((ord(c) - ord('A') + self.shift) % 26 + ord('A'))
                else:
                    result += chr((ord(c) - ord('a') + self.shift) % 26 + ord('a'))
                
                                                                              
class ProductCipher(Message):
    def init(self):
        super().init()

    def encrypt(self, message):
        sub_message_1 = message[::2]
        sub_message_2 = message[1::2]
        encrypted_message = sub_message_2 + sub_message_1
        return encrypted_message

    def decrypt(self, message):
        mid = len(message) // 2
        sub_message_1 = message[mid:]
        sub_message_2 = message[:mid]
        decrypted_message = ""
        for i in range(mid):
            decrypted_message += sub_message_1[i] + sub_message_2[i]
        if len(sub_message_1) > len(sub_message_2):
            decrypted_message += sub_message_1[-1]
        return decrypted_message

class RSA(Message):
    def init(self):
        super().init()


    def encrypt(self, message):
        n, e = 2537, 13
        encrypted_message = [(ord(char) ** e) % n for char in message]
        return encrypted_message

    def decrypt(self, message):
        n, d = 2537, 937
        decrypted_message = ""
        for num in message:
            decrypted_message += chr((num ** d) % n)
        return decrypted_message



def main():
    ciphers = [SubstitutionCipher(), PlayfairCipher(), CaesarCipher(), TranspositionCipher(), ProductCipher(), RSA()]
    plaintext_messages = []
    encrypted_messages = []
    methods = []
    while True:
        message = input("Enter a message to encrypt (or 'Stop' to end the program): ")
        if message.lower() == "stop":
            break
        cipher = random.choice(ciphers)
        methods.append(type(cipher).name)
        plaintext_messages.append(message)
        encrypted_messages.append(cipher.encrypt(message))
    print("Results:")
    for i in range(len(plaintext_messages)):
        print("Method: ", methods[i])
        print("Original message: ", plaintext_messages[i])
        print("Encrypted message: ", encrypted_messages[i])
        print("Decrypted message: ", ciphers[i].decrypt(encrypted_messages[i]))
        print()

if __name__ == "main":
    main()
