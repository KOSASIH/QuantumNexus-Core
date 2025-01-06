import hashlib
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumDataSecurity:
    def __init__(self):
        self.key = None

    def generate_key(self, length=256):
        """Generates a random quantum key for encryption."""
        self.key = np.random.randint(0, 2, length)  # Generate a binary key
        logging.info(f"Generated quantum key: {self.key}")
        return self.key

    def encrypt_data(self, data):
        """Encrypts data using a simple XOR operation with the quantum key."""
        if self.key is None:
            logging.error("No key generated. Please generate a key first.")
            raise ValueError("Key not generated.")
        
        # Convert data to binary
        data_bits = np.array(list(map(int, ''.join(format(ord(char), '08b') for char in data))), dtype=int)
        
        # Ensure the key is the same length as the data
        if len(data_bits) > len(self.key):
            logging.error("Data is too long for the generated key.")
            raise ValueError("Data length exceeds key length.")
        
        # Encrypt data using XOR
        encrypted_data = np.bitwise_xor(data_bits, self.key[:len(data_bits)])
        logging.info(f"Encrypted data: {encrypted_data}")
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """Decrypts data using the quantum key."""
        if self.key is None:
            logging.error("No key generated. Please generate a key first.")
            raise ValueError("Key not generated.")
        
        # Decrypt data using XOR
        decrypted_data = np.bitwise_xor(encrypted_data, self.key[:len(encrypted_data)])
        decrypted_string = ''.join(chr(int(''.join(map(str, decrypted_data[i:i + 8])), 2)) for i in range(0, len(decrypted_data), 8))
        logging.info(f"Decrypted data: {decrypted_string}")
        return decrypted_string

    def verify_integrity(self, data, hash_value):
        """Verifies the integrity of the data using a hash function."""
        computed_hash = hashlib.sha256(data.encode()).hexdigest()
        if computed_hash == hash_value:
            logging.info("Data integrity verified.")
            return True
        else:
            logging.error("Data integrity verification failed.")
            return False

# Example usage
if __name__ == "__main__":
    qds = QuantumDataSecurity()
    
    # Generate a quantum key
    key = qds.generate_key(length=256)
    
    # Encrypt data
    original_data = "Hello, Quantum World!"
    encrypted_data = qds.encrypt_data(original_data)
    
    # Decrypt data
    decrypted_data = qds.decrypt_data(encrypted_data)
    
    # Verify integrity
    hash_value = hashlib.sha256(original_data.encode()).hexdigest()
    integrity_check = qds.verify_integrity(original_data, hash_value)
    
    logging.info(f"Original Data: {original_data}")
    logging.info(f"Decrypted Data: {decrypted_data}")
    logging.info(f"Integrity Check: {integrity_check}")
