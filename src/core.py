import hashlib
import time
import random

class QistNode:
    """Represents a node within the Qist network (Executor or Overseer)"""
    def __init__(self, node_id, power, wallet_address):
        self.node_id = node_id
        self.power = power
        self.wallet = wallet_address
        # Designated as Executor if hardware power meets the threshold (>= 50)
        self.is_executor = power >= 50
        self.reputation = 1.0

class Task:
    """Represents an AI task submitted to the protocol"""
    def __init__(self, task_id, complexity, data):
        self.task_id = task_id
        # Complexity level directly influences the total minted value
        self.complexity = complexity
        self.data = data
        self.status = "Pending"

class QistProtocol:
    def __init__(self):
        # Global ledger for unit (QU) tracking
        self.ledger = {}
        # Sovereign administrative and stakeholder wallets
        self.innovator_wallet = "0x_INNOVATOR_ADDR"
        self.developer_wallet = "0x_DEVELOPER_ADDR"
        self.marketer_wallet  = "0x_MARKETER_ADDR"
        self.funder_wallet    = "0x_FUNDER_ADDR"

    def calculate_and_mint(self, task, executor, overseers):
        """
        Distributes value based on the Sovereign Qist Charter:
        1. Administrative Fees: 2% each for Innovator, Developer, Marketer (6% total).
        2. Funding Fee: 4% for the Funder.
        3. Total Governance Deductions = 10%.
        4. Net Reward (90%) Distribution: 80% to the Executor, 20% split among Overseers.
        """
        
        # Calculate total minted value based on task complexity
        total_value = task.complexity * 100 
        
        # Calculate individual administrative fees
        innovator_fee = total_value * 0.02
        developer_fee = total_value * 0.02
        marketer_fee  = total_value * 0.02
        funder_fee    = total_value * 0.04
        
        total_admin_fees = innovator_fee + developer_fee + marketer_fee + funder_fee
        
        # Net reward for resource providers (90% of total)
        net_reward = total_value - total_admin_fees
        
        # Split net reward based on the 80/20 equity rule
        executor_share = net_reward * 0.80
        overseer_total_share = net_reward * 0.20
        per_overseer_share = overseer_total_share / len(overseers)

        # Update the global ledger with newly minted units (Minting)
        self._mint(executor.wallet, executor_share)
        self._mint(self.innovator_wallet, innovator_fee)
        self._mint(self.developer_wallet, developer_fee)
        self._mint(self.marketer_wallet, marketer_fee)
        self._mint(self.funder_wallet, funder_fee)
        
        for ov in overseers:
            self._mint(ov.wallet, per_overseer_share)

        task.status = "Completed"
        
        return {
            "total_minted": total_value,
            "net_reward_pool": net_reward,
            "executor_payout": executor_share,
            "overseer_payout_each": per_overseer_share,
            "fees": {
                "innovator": innovator_fee,
                "developer": developer_fee,
                "marketer": marketer_fee,
                "funder": funder_fee
            }
        }

    def _mint(self, wallet, amount):
        """Internal helper to add units to a specific wallet in the ledger"""
        self.ledger[wallet] = self.ledger.get(wallet, 0) + amount

# --- Simulation Logic ---
if __name__ == "__main__":
    protocol = QistProtocol()
    
    # Initialize a high-performance node (Executor) and low-power nodes (Overseers)
    exec_node = QistNode("High_Power_GPU_01", 100, "0x_EXEC_USER_WALLET")
    ov_nodes = [QistNode(f"Observer_Node_{i}", 10, f"0x_OV_{i}_WALLET") for i in range(3)]
    
    # Define an AI task for processing
    ai_job = Task("AI_LAYER_VERIFICATION_77", 10, "QuantumLatticeData")

    # Execute the minting and distribution cycle
    distribution = protocol.calculate_and_mint(ai_job, exec_node, ov_nodes)
    
    print("--- Qist Protocol: Final Payout Simulation ---")
    print(f"Total Task Value: {distribution['total_minted']} QU")
    print(f"Net Resource Pool (90%): {distribution['net_reward_pool']} QU")
    print(f"  - Executor Reward: {distribution['executor_payout']} QU")
    print(f"  - Each Overseer Reward: {distribution['overseer_payout_each']} QU")
    print("Administrative Fees (10% Total):")
    print(f"  - Innovator (2%): {distribution['fees']['innovator']} QU")
    print(f"  - Developer (2%): {distribution['fees']['developer']} QU")
    print(f"  - Marketer (2%): {distribution['fees']['marketer']} QU")
    print(f"  - Funder (4%): {distribution['fees']['funder']} QU")
    print("\n[Protocol Status] Ledger updated successfully.")
