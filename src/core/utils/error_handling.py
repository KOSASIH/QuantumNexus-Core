import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom Exception Classes
class QuantumError(Exception):
    """Base class for exceptions related to quantum operations."""
    pass

class QuantumStateError(QuantumError):
    """Exception raised for errors in quantum state operations."""
    def __init__(self, message):
        self.message = message
        logging.error(f"QuantumStateError: {self.message}")

class QuantumCircuitError(QuantumError):
    """Exception raised for errors in quantum circuit operations."""
    def __init__(self, message):
        self.message = message
        logging.error(f"QuantumCircuitError: {self.message}")

class ContractError(Exception):
    """Base class for exceptions related to smart contracts."""
    pass

class ContractValidationError(ContractError):
    """Exception raised for errors in contract validation."""
    def __init__(self, message):
        self.message = message
        logging.error(f"ContractValidationError: {self.message}")

class ContractExecutionError(ContractError):
    """Exception raised for errors during contract execution."""
    def __init__(self, message):
        self.message = message
        logging.error(f"ContractExecutionError: {self.message}")

# Utility Functions
def handle_error(error):
    """Handles errors by logging and raising appropriate exceptions."""
    if isinstance(error, QuantumError):
        logging.error(f"Handling Quantum Error: {error.message}")
        raise error
    elif isinstance(error, ContractError):
        logging.error(f"Handling Contract Error: {error.message}")
        raise error
    else:
        logging.error("An unknown error occurred.")
        raise Exception("An unknown error occurred.")

def log_error(message):
    """Logs an error message."""
    logging.error(message)

# Example usage
if __name__ == "__main__":
    try:
        # Simulate a quantum state error
        raise QuantumStateError("Invalid quantum state encountered.")
    except QuantumError as e:
        handle_error(e)

    try:
        # Simulate a contract validation error
        raise ContractValidationError("Contract does not meet required standards.")
    except ContractError as e:
        handle_error(e)
