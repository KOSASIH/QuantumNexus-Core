# Advanced Quantum Error Correction Example

## Overview
This example demonstrates an advanced implementation of quantum error correction using the Shor code. The script encodes a single qubit into three qubits, introduces multiple bit-flip errors, measures the syndrome to detect the errors, corrects them, and visualizes the results.

## Key Components
- **Encoding**: The `encode_qubit` function encodes a single qubit into three qubits.
- **Error Introduction**: The `introduce_errors` function simulates multiple bit-flip errors at specified positions.
- **Syndrome Measurement**: The `measure_syndrome` function detects errors in the encoded qubit.
- **Error Correction**: The `correct_error` function corrects the detected errors based on the syndrome.
- **Visualization**: The `visualize_results` function provides a graphical representation of the original, erroneous, and corrected qubits.

## Requirements
- Python 3.x
- NumPy
- Matplotlib

## How to Run
1. Ensure you have the required libraries installed. You can install them using pip:
   ```bash
   pip install numpy matplotlib
   ```

2. Run the script:
   ```bash
   1 python error_correction_example.py
   ```

## Output
The script will print the encoded qubit, the erroneous qubit, the syndrome, and the corrected qubit. It will also display a bar chart visualizing the number of qubits in the |1> state for the original, erroneous, and corrected qubits, along with the syndrome information.
