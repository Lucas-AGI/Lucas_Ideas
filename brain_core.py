"""
🧠 SYMBOLIC BRAIN CORE — LUCAS
==============================
This module orchestrates the main symbolic modules:
memory, intent, ethics, dreams, and reflection.

LUCAS uses this core as the bridge between symbolic threads,
emotional triggers, and safe, consent-based reasoning.

"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Module Imports
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
from core.intent_node import IntentNode
from core.memoria import Memoria
from core.ethics_engine import EthicsEngine
from core.dream_refold import DreamWeaver
from core.reflection import ReflectionLog
from core.override_quorum import QuorumOverride


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Symbolic Brain Class
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class SymbolicBrain:
    def __init__(self):
        self.memory = Memoria()
        self.intent = IntentNode()
        self.ethics = EthicsEngine()
        self.dream = DreamWeaver()
        self.reflection = ReflectionLog()
        self.quorum = QuorumOverride()

    def process(self, user_input):
        """
        Main symbolic reasoning loop.
        """
        print(f"\n🧠 LUCAS received: {user_input}")

        # Step 1: Interpret user intent
        intent = self.intent.analyze(user_input)

        # Step 2: Retrieve related symbolic memory
        memory = self.memory.recall(intent)

        # Step 3: Ethical check before action
        if not self.ethics.approves(intent, memory):
            return self.quorum.resolve(intent, memory)

        # Step 4: Execute dream response or action
        dream_response = self.dream.react(intent, memory)

        # Step 5: Log reflection
        self.reflection.log(intent, memory, dream_response)

        return dream_response


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Sample Execution (CLI style)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if __name__ == "__main__":
    lucas = SymbolicBrain()
    while True:
        user_input = input("\n🗣️  You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = lucas.process(user_input)
        print(f"🤖 LUCAS: {response}")