import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GovernanceMetrics:
    def __init__(self):
        self.total_proposals = 0
        self.approved_proposals = 0
        self.rejected_proposals = 0
        self.total_votes = 0

    def update_metrics(self, proposal):
        """Update metrics based on the outcome of a proposal."""
        self.total_proposals += 1
        if proposal.status == 'Approved':
            self.approved_proposals += 1
        elif proposal.status == 'Rejected':
            self.rejected_proposals += 1
        self.total_votes += len(proposal.votes)

    def participation_rate(self):
        """Calculate the voter participation rate."""
        if self.total_proposals == 0:
            return 0
        return (self.total_votes / (self.total_proposals * 10)) * 100  # Assuming a maximum of 10 voters per proposal

    def success_rate(self):
        """Calculate the success rate of proposals."""
        if self.total_proposals == 0:
            return 0
        return (self.approved_proposals / self.total_proposals) * 100

    def report(self):
        """ Generate a report of governance metrics."""
        return {
            "Total Proposals": self.total_proposals,
            "Approved Proposals": self.approved_proposals,
            "Rejected Proposals": self.rejected_proposals,
            "Total Votes": self.total_votes,
            "Participation Rate (%)": self.participation_rate(),
            "Success Rate (%)": self.success_rate()
        }

# Example usage
if __name__ == "__main__":
    metrics = GovernanceMetrics()
    governance = DynamicGovernance()
    
    # Create and vote on proposals
    proposal_id = governance.create_proposal("Increase Block Size", "Proposal to increase the block size to improve transaction throughput.", "Alice")
    proposal = governance.get_proposal(proposal_id)
    if proposal:
        proposal.cast_vote("Bob", "yes")
        proposal.cast_vote("Charlie", "no")
        proposal.tally_votes()
        metrics.update_metrics(proposal)

    # Generate metrics report
    report = metrics.report()
    logging.info(f"Governance Metrics Report: {report}")
