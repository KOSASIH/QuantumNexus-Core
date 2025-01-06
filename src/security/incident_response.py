import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Incident:
    def __init__(self, incident_id, description, severity, status='Open'):
        self.incident_id = incident_id
        self.description = description
        self.severity = severity
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update_status(self, new_status):
        """Update the status of the incident."""
        self.status = new_status
        self.updated_at = datetime.now()
        logging.info(f"Incident {self.incident_id} status updated to {self.status}.")

class IncidentResponse:
    def __init__(self):
        self.incidents = []

    def log_incident(self, description, severity):
        """Log a new incident."""
        incident_id = len(self.incidents) + 1  # Simple ID generation
        incident = Incident(incident_id, description, severity)
        self.incidents.append(incident)
        logging.info(f"Incident logged: {incident_id} - {description} (Severity: {severity})")
        return incident_id

    def categorize_incident(self, incident_id):
        """Categorize the incident based on severity."""
        incident = self.get_incident(incident_id)
        if incident:
            if incident.severity == 'Critical':
                logging.warning(f"Incident {incident_id} is critical! Immediate action required.")
                return "Immediate action required."
            elif incident.severity == 'High':
                logging.info(f"Incident {incident_id} is high severity. Prioritize response.")
                return "Prioritize response."
            elif incident.severity == 'Medium':
                logging.info(f"Incident {incident_id} is medium severity. Address in due time.")
                return "Address in due time."
            elif incident.severity == 'Low':
                logging.info(f"Incident {incident_id} is low severity. Monitor the situation.")
                return "Monitor the situation."
        else:
            logging.error("Incident not found.")
            return None

    def get_incident(self, incident_id):
        """Retrieve an incident by its ID."""
        for incident in self.incidents:
            if incident.incident_id == incident_id:
                return incident
        logging.error("Incident not found.")
        return None

    def resolve_incident(self, incident_id):
        """Resolve an incident."""
        incident = self.get_incident(incident_id)
        if incident:
            incident.update_status('Resolved')
            logging.info(f"Incident {incident_id} resolved.")
        else:
            logging.error("Incident not found.")

# Example usage
if __name__ == "__main__":
    ir = IncidentResponse()
    
    # Log a new incident
    incident_id = ir.log_incident("Unauthorized access attempt detected.", "High")
    
    # Categorize the incident
    category = ir.categorize_incident(incident_id)
    logging.info(f"Incident {incident_id} categorized as: {category}")
    
    # Resolve the incident
    ir.resolve_incident(incident_id)
