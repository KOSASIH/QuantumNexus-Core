
import numpy as np
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Basis states
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
        if not isinstance(qubit, np.ndarray) or len(qubit) != 2:
            raise ValueError("Input must be a 2-element numpy array representing a qubit.")
        if code not in self.codes:
            raise ValueError("Unsupported error correction code.")
        logging.info(f"Encoding qubit using {code} code.")
        return self.codes[code](qubit)

    def shor_code(self, qubit):
        """Encodes a single qubit into nine qubits using the Shor code."""
        # |ψ> -> |ψψψ>, then apply bit-flip and phase-flip redundancy
        triple = np.kron(np.kron(qubit, qubit), qubit)  # Tensor product |ψψψ>
        return np.kron(triple, triple)  # Redundancy for phase-flip correction

    def steane_code(self, qubit):
        """Encodes a single qubit into seven qubits using the Steane code."""
        # Simplified implementation for demonstration
        return np.kron(qubit, np.ones(7)) / np.sqrt(7)  # Distribute qubit into 7 states

    def introduce_errors(self, encoded_qubit, error_positions):
        """Introduces bit-flip errors at the specified positions."""
        if not isinstance(encoded_qubit, np.ndarray):
            raise ValueError("Encoded qubit must be a numpy array.")
        error_qubit = encoded_qubit.copy()
        for pos in error_positions:
            if pos >= len(encoded_qubit):
                raise ValueError(f"Error position {pos} exceeds qubit length.")
            error_qubit[pos] = 1 - error_qubit[pos]  # Flip the bit
        logging.info(f"Introduced errors at positions: {error_positions}")
        return error_qubit

    def measure_syndrome(self, encoded_qubit, code='shor'):
        """Measures the syndrome to detect errors in the encoded qubit."""
        if code == 'shor':
            # Check parity of 3-bit groups
            groups = [encoded_qubit[i:i + 3] for i in range(0, len(encoded_qubit), 3)]
            syndrome = [np.sum(group) % 2 for group in groups]
            logging.info(f"Syndrome for Shor code: {syndrome}")
            return syndrome
        elif code == 'steane':
            # Syndrome measurement logic for Steane (simplified)
            syndrome = [np.sum(encoded_qubit) % 2]
            logging.info(f"Syndrome for Steane code: {syndrome}")
            return syndrome
        else:
            raise ValueError("Unsupported error correction code.")

    def correct_error(self, encoded_qubit, syndrome, code='shor'):
        """Corrects the error based on the measured syndrome."""
        corrected_qubit = encoded_qubit.copy()
        if code == 'shor':
            # Correct errors in 3-bit groups based on syndrome
            for i, group_syndrome in enumerate(syndrome):
                if group_syndrome == 1:  # Detected error
                    group_start = i * 3
                    corrected_qubit[group_start] = 1 - corrected_qubit[group_start]  # Flip the first bit in group
        elif code == 'steane':
            if syndrome[0] == 1:  # Simplified single-bit correction
                corrected_qubit[0] = 1 - corrected_qubit[0]
        logging.info(f"Corrected qubit: {corrected_qubit}")
        return corrected_qubit

    def visualize_results(self, original, erroneous, corrected, syndrome):
        """Visualizes the original, erroneous, and corrected qubits."""
        labels = ['Original', 'Erroneous', 'Corrected']
        data = [original, erroneous, corrected]
        fig, ax = plt.subplots(figsize=(8, 6))

        ax.bar(labels, [np.sum(np.abs(d)) for d in data], color=['green', 'red', 'blue'])
        ax.set_ylabel('Total Amplitude')
        ax.set_title('Quantum Error Correction Visualization')
        ax.text(1, np.sum(erroneous), f'Syndrome: {syndrome}', ha='center', va='bottom')
        plt.show()

# Example usage
if __name__ == "__main__":
    qec = QuantumErrorCorrection()

    # Step 1: Encode a qubit
    original_qubit = (zero + one) / np.sqrt(2)  # Superposition state |+>
    encoded_qubit = qec.encode_qubit(original_qubit, code='shor')
    logging.info(f"Encoded Qubit: {encoded_qubit}")

    # Step 2: Introduce errors
    error_positions = [1, 7]  # Introduce errors
    erroneous_qubit = qec.introduce_errors(encoded_qubit, error_positions)
    logging.info(f"Erroneous Qubit: {erroneous_qubit}")

    # Step 3: Measure syndrome
    syndrome = qec.measure_syndrome(erroneous_qubit, code='shor')

    # Step 4: Correct the error
    corrected_qubit = qec.correct_error(erroneous_qubit, syndrome, code='shor')

    # Step 5: Visualize results
    qec.visualize_results(encoded_qubit, erroneous_qubit, corrected_qubit, syndrome)
