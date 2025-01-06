import hashlib
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumSignatureScheme:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        """Generates a pair of quantum keys (private and public)."""
        self.private_key = np.random.randint(0, 2, 256)  # Random binary private key
        self.public_key = self.private_key.copy()  # In a real scheme, this would be derived differently
        logging.info("Keys generated successfully.")
        return self.private_key, self.public_key

    def sign_message(self, message):
        """Signs a message using the private key."""
        if self.private_key is None:
            logging.error("Private key not generated.")
            raise ValueError("Private key not generated.")
        
        # Hash the message
        message_hash = hashlib.sha256(message.encode()).hexdigest()
        logging.info(f"Message hash: {message_hash}")

        # Create a signature by XORing the hash with the private key
        signature = np.bitwise_xor(np.array(list(map(int, message_hash)), dtype=int), self.private_key[:len(message_hash)])
        logging.info(f"Signature created: {signature}")
        return signature

    def verify_signature(self, message, signature):
        """Verifies the signature of a message using the public key."""
        if self.public_key is None:
            logging.error("Public key not generated.")
            raise ValueError("Public key not generated.")
        
        # Hash the message
        message_hash = hashlib.sha256(message.encode()).hexdigest()
        logging.info(f"Message hash for verification: {message_hash}")

        # Verify the signature by XORing the signature with the public key
        computed_hash = np.bitwise_xor(signature, self.public_key[:len(message_hash)])
        computed_hash_hex = ''.join(map(str, computed_hash))
        
        # Check if the computed hash matches the original hash
        if computed_hash_hex == message_hash:
            logging.info("Signature verified successfully.")
            return True
        else:
            logging.error("Signature verification failed.")
            return False

# Example usage
if __name__ == "__main__":
    qss = QuantumSignatureScheme()
    
    # Generate keys
    private_key, public_key = qss.generate_keys()
    
    # Sign a message
    original_message = "Hello, Quantum World!"
    signature = qss.sign_message(original_message)
    
    # Verify the signature
    is_verified = qss.verify_signature(original_message, signature)
    
    logging.info(f"Original Message: {original_message}")
    logging.info(f"Signature Verified: {is_verified}")
