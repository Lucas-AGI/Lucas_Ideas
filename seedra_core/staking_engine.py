# ===============================================================
# 📂 FILE: staking_engine.py
# 📍 RECOMMENDED PATH: /Users/grdm_admin/Downloads/oxn/seedra_core/
# ===============================================================
# 🧠 PURPOSE:
# This file defines the symbolic staking and participation engine
# for SEEDRA. It manages voluntary staking, calculates symbolic
# participation scores, and supports reward/slash logic based on
# ethical or behavioral context.
#
# 🧰 KEY FEATURES:
# - 🪙 Stake and slash token balances
# - 📈 Track participation scores
# - 🧠 Reward symbolic behavior via proof signals
#
# 💬 Symbolic Design:
# Participation is not passive. Each action is bonded with intent.
# Scores reflect symbolic alignment and system health.
# ===============================================================

from datetime import datetime
from seedra_core.token_engine import TokenEngine

class StakingEngine:
    def __init__(self, token_engine: TokenEngine):
        self.token_engine = token_engine
        self.participation_log = {}
        self.staked_tokens = {}

    def stake_tokens(self, node_id, amount):
        balance = self.token_engine.get_balance(node_id)
        if balance >= amount:
            self.token_engine.deduct_tokens(node_id, amount, reason="symbolic_stake")
            self.staked_tokens[node_id] = self.staked_tokens.get(node_id, 0) + amount
            self._log_participation(node_id, "stake")
        else:
            raise ValueError("Insufficient balance to stake")

    def slash_tokens(self, node_id, amount, reason="policy_violation"):
        staked = self.staked_tokens.get(node_id, 0)
        slash_amt = min(amount, staked)
        self.staked_tokens[node_id] = staked - slash_amt
        self.token_engine.deduct_tokens(node_id, slash_amt, reason=f"slashed:{reason}")

    def _log_participation(self, node_id, action):
        if node_id not in self.participation_log:
            self.participation_log[node_id] = []
        self.participation_log[node_id].append({
            "action": action,
            "timestamp": datetime.utcnow().isoformat()
        })

    def calculate_score(self, node_id):
        count = len(self.participation_log.get(node_id, []))
        staked = self.staked_tokens.get(node_id, 0)
        return (count * staked) / 100

    def reward_for_participation(self, node_id, base=10):
        score = self.calculate_score(node_id)
        reward = int(score * base)
        if reward > 0:
            self.token_engine.award_tokens(node_id, reward, reason="symbolic_participation_reward")

# ===============================================================
# 💾 HOW TO USE
# ===============================================================
# ▶️ INIT:
#     staking = StakingEngine(token_engine)
#
# 🪙 STAKE TOKENS:
#     staking.stake_tokens("node_01", 10)
#
# ⚖️ SLASH:
#     staking.slash_tokens("node_01", 5, reason="failed_zk_proof")
#
# 📈 REWARD:
#     staking.reward_for_participation("node_01")
#
# 🧠 GOOD FOR:
# - Symbolic governance participation
# - Incentivizing contribution via proof-of-action
# - Trust-based staking linked to consent systems
# ===============================================================