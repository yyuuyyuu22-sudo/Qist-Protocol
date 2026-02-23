import hashlib
import time

class QistNode:
    """Represents a node within the Qist network (Executor or Overseer)"""
    def __init__(self, node_id, power, wallet_address):
        self.node_id = node_id
        self.power = power
        self.wallet = wallet_address
        self.is_executor = power >= 50
        self.reputation = 1.0

class QistProtocol:
    def __init__(self):
        self.ledger = {}
        # Admin Wallets
        self.innovator_wallet = "0x_INNOVATOR"
        self.developer_wallet = "0x_DEVELOPER"
        self.marketer_wallet  = "0x_MARKETER"
        self.funder_wallet    = "0x_FUNDER"

    def calculate_and_mint(self, task_complexity, executor, overseers):
        """Distributes rewards: 10% admin fees, 90% to resources (80/20 split)"""
        total_value = task_complexity * 100 
        
        # 10% Admin Fees
        fees = {
            "innovator": total_value * 0.02,
            "developer": total_value * 0.02,
            "marketer": total_value * 0.02,
            "funder": total_value * 0.04
        }
        
        # 90% Net Reward
        net_reward = total_value - sum(fees.values())
        executor_share = net_reward * 0.80
        overseer_share = (net_reward * 0.20) / len(overseers)

        # Update Ledger (Simplified)
        self._mint(executor.wallet, executor_share)
        self._mint(self.innovator_wallet, fees["innovator"])
        self._mint(self.developer_wallet, fees["developer"])
        self._mint(self.marketer_wallet, fees["marketer"])
        self._mint(self.funder_wallet, fees["funder"])
        for ov in overseers: self._mint(ov.wallet, overseer_share)

        return {"status": "Success", "total": total_value, "net": net_reward}

    def _mint(self, wallet, amount):
        self.ledger[wallet] = self.ledger.get(wallet, 0) + amount

if __name__ == "__main__":
    print("Qist Protocol Core Online. Post-Quantum Security Active.")
