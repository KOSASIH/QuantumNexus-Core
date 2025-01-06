import unittest
import numpy as np
from quantum_error_correction import QuantumErrorCorrection  # Assuming the main code is in this module

class TestQuantumErrorCorrection(unittest.TestCase):
    def setUp(self):
        """Set up the QuantumErrorCorrection instance for testing."""
        self.qec = QuantumErrorCorrection()

    def test_encode_qubit(self):
        """Test encoding of qubits."""
        encoded_zero = self.qec.encode_qubit(np.array([1, 0]))  # |0>
        encoded_one = self.qec.encode_qubit(np.array([0, 1]))   # |1>
        
        expected_zero = np.array([1, 0, 0, 0, 0, 0, 0, 0])  # Shor code for |0>
        expected_one = np.array([0, 0, 0, 0, 1, 0, 0, 0])   # Shor code for |1>
        
        np.testing.assert_array_equal(encoded_zero, expected_zero)
        np.testing.assert_array_equal(encoded_one, expected_one)

    def test_introduce_error(self):
        """Test introduction of errors."""
        encoded_qubit = self.qec.encode_qubit(np.array([0, 1]))  # |1>
        erroneous_qubit = self.qec.introduce_errors(encoded_qubit, [0])  # Introduce error at position 0
        
        expected_erroneous = np.array([1, 0, 0, 0, 1, 0, 0, 0])  # Error introduced
        np.testing.assert_array_equal(erroneous_qubit, expected_erroneous)

    def test_measure_syndrome(self):
        """Test syndrome measurement."""
        encoded_qubit = self.qec.encode_qubit(np.array([0, 1]))  # |1>
        erroneous_qubit = self.qec.introduce_errors(encoded_qubit, [0])  # Introduce error at position 0
        
        syndrome = self.qec.measure_syndrome(erroneous_qubit)
        expected_syndrome = np.array([1, 0, 0])  # Expected syndrome for the error introduced
        
        np.testing.assert_array_equal(syndrome, expected_syndrome)

    def test_correct_error(self):
        """Test error correction."""
        encoded_qubit = self.qec.encode_qubit(np.array([0, 1]))  # |1>
        erroneous_qubit = self.qec.introduce_errors(encoded_qubit, [0])  # Introduce error at position 0
        
        syndrome = self.qec.measure_syndrome(erroneous_qubit)
        corrected_qubit = self.qec.correct_error(erroneous_qubit, syndrome)
        
        np.testing.assert_array_equal(corrected_qubit, encoded_qubit)  # Check if corrected qubit matches original

if __name__ == "__main__":
    unittest.main()
