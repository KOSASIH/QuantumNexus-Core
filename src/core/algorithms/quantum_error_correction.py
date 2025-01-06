import numpy as np
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the basis states
zero = np.array([1, 0])  # |0>
one = np.array([0, 1])   # |1>

class QuantumErrorCorrection:
    def __init__(self):
        self.codes = {
            'shor': self.shor_code,
            'steane': self.steane_code
        }

    def encode_qubit(self, qubit, code='shor'):
        """Encodes a single qubit using the specified error correction code."""
        if code not in self.codes:
            raise ValueError("Unsupported error correction code.")
        return self.codes[code](qubit)

    def shor_code(self, qubit):
        """Encodes a single qubit into three qubits using the Shor code."""
        if np.array_equal(qubit, zero):
            return np.array([1, 0, 0, 0, 0, 0, 0, 0])  # |000>
        elif np.array_equal(qubit, one):
            return np.array([0, 0, 0, 0, 1, 0, 0, 0])  # |111>
        else:
            raise ValueError("Input must be a basis state |0> or |1>.")

    def steane_code(self, qubit):
        """Encodes a single qubit into seven qubits using the Steane code."""
        if np.array_equal(qubit, zero):
            return np.array([1, 0, 0, 1, 1, 0, 1])  # |0000000>
        elif np.array_equal(qubit, one):
            return np.array([0, 1, 1, 0, 0, 1, 0])  # |1111111>
        else:
            raise ValueError("Input must be a basis state |0> or |1>.")

    def introduce_errors(self, encoded_qubit, error_positions):
        """Introduces bit-flip errors at the specified positions."""
        error_qubit = encoded_qubit.copy()
        for pos in error_positions:
            error_qubit[pos] = 1 - error_qubit[pos]  # Flip the bit
        return error_qubit

    def measure_syndrome(self, encoded_qubit, code='shor'):
        """Measures the syndrome to detect errors in the encoded qubit."""
        if code == 'shor':
            syndrome = np.zeros(3)
            syndrome[0] = encoded_qubit[0] ^ encoded_qubit[1]  # Check qubits 1 and 2
            syndrome[1] = encoded_qubit[1] ^ encoded_qubit[2]  # Check qubits 2 and 3
            syndrome[2] = encoded_qubit[0] ^ encoded_qubit[2]  # Check qubits 1 and 3
            return syndrome
        elif code == 'steane':
            syndrome = np.zeros(3)
            syndrome[0] = encoded_qubit[0] ^ encoded_qubit[1] ^ encoded_qubit[3]  # Check qubits 1, 2, and 4
            syndrome[1] = encoded_qubit[2] ^ encoded_qubit[3] ^ encoded_qubit[5]  # Check qubits 3, 4, and 6
            syndrome[2] = encoded_qubit[1] ^ encoded_qubit[4] ^ encoded_qubit[5]  # Check qubits 2, 5, and 6
            return syndrome
        else:
            raise ValueError("Unsupported error correction code.")

    def correct_error(self, encoded_qubit, syndrome, code='shor'):
        """Corrects the error based on the measured syndrome."""
        corrected_qubit = encoded_qubit.copy()
        if code == 'shor':
            if np.array_equal(syndrome, [1, 0, 0]):
                corrected_qubit[0] = 1 - corrected_qubit[0]  # Correct qubit 1
            elif np.array_equal(syndrome, [0, 1, 0]):
                corrected_qubit[1] = 1 - corrected_qubit[1]  # Correct qubit 2
            elif np.array_equal(syndrome, [0, 0, 1]):
                corrected_qubit[2] = 1 - corrected_qubit[2]  # Correct qubit 3
        elif code == 'steane':
            if np.array_equal(syndrome, [1, 0, 0]):
                corrected_qubit[0] = 1 - corrected_qubit[0]  # Correct qubit 1
            elif np.array_equal(syndrome, [0, 1, 0]):
                corrected_qubit[1] = 1 - corrected_qubit[1]  # Correct qubit 2
            elif np.array_equal(syndrome, [0, 0, 1]):
                corrected_qubit[2] = 1 - corrected_qubit[2]  # Correct qubit 3
        return corrected_qubit

    def visualize_results(self, original, erroneous, corrected, syndrome):
        """Visualizes the original, erroneous, and corrected qubits."""
        labels = ['Original', 'Erroneous', 'Corrected']
        data = [original, erroneous, corrected]
        
        fig, ax = plt.subplots()
        ax.bar(labels, [np.sum(d) for d in data], color=['green', 'red', 'blue'])
        ax.set_ylabel('Number of Qubits in State |1>')
        ax.set_title('Quantum Error Correction Visualization')
        ax.text(1, np.sum(erroneous), f'Syndrome: {syndrome}', ha='center', va='bottom')
        plt.show()

# Example usage
if __name__ == "__main__":
    qec = QuantumErrorCorrection()
    
    # Step 1: Encode a qubit
    original_qubit = one  # Change to zero for |0>
    encoded_qubit = qec.encode_qubit(original_qubit, code='shor')
    logging.info(f"Encoded Qubit: {encoded_qubit}")

    # Step 2: Introduce errors
    error_positions = [0, 1]  # Introduce errors in the first and second qubits
    erroneous_qubit = qec.introduce_errors(encoded_qubit, error_positions)
    logging.info(f"Erroneous Qubit: {erroneous_qubit}")

    # Step 3: Measure syndrome
    syndrome = qec.measure_syndrome(erroneous_qubit, code='shor')
    logging.info(f"Syndrome: {syndrome}")

    # Step 4: Correct the error
    corrected_qubit = qec.correct_error(erroneous_qubit, syndrome, code='shor')
    logging.info(f"Corrected Qubit: {corrected_qubit}")

    # Verify if the correction was successful
    if np.array_equal(corrected_qubit, encoded_qubit):
        logging.info("Error correction successful!")
    else:
        logging.error("Error correction failed.")

    # Step 5: Visualize the results
    qec.visualize_results(encoded_qubit, erroneous_qubit, corrected_qubit, syndrome)
