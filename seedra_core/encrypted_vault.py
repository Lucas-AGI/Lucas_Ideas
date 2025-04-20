# ===============================================================
# 📂 FILE: encrypted_vault.py
# 📍 RECOMMENDED PATH: /Users/grdm_admin/Downloads/oxn/seedra_core/
# ===============================================================
# 🧠 PURPOSE:
# This file defines the symbolic encrypted vault for SEEDRA.
# It securely stores entries using AES encryption (Fernet) and supports
# future extensions like quorum unlocking, environmental triggers, and
# multi-fragment symbolic access layers.
#
# 🛡️ KEY FUNCTIONS:
# - 🔐 Store encrypted data entries
# - 🔓 Retrieve stored entries
# - 🧬 Import/export encryption keys
# - 🧱 Foundation for symbolic quorum-based decryption
#
# 💬 Symbolic Design:
# The vault acts as a symbolic memory root, only unlocking when the right
# keys, contexts, and symbolic environmental anchors align.
# ===============================================================

from cryptography.fernet import Fernet
import os

class EncryptedVault:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.entries = []

    def store_entry(self, plaintext: str):
        """🔐 Encrypt and store a new plaintext entry"""
        encrypted = self.cipher.encrypt(plaintext.encode())
        self.entries.append(encrypted)
        return encrypted

    def retrieve_entry(self, index=-1):
        """🔓 Retrieve and decrypt a stored entry by index (default: latest)"""
        if not self.entries:
            return None
        encrypted = self.entries[index]
        return self.cipher.decrypt(encrypted).decode()

    def export_key(self):
        """📤 Export the current encryption key as a string"""
        return self.key.decode()

    def import_key(self, key_str):
        """📥 Import an encryption key from a string"""
        self.key = key_str.encode()
        self.cipher = Fernet(self.key)

    def get_all_entries(self):
        """📚 Retrieve and decrypt all stored entries"""
        return [self.cipher.decrypt(e).decode() for e in self.entries]

# ===============================================================
# 💾 HOW TO USE
# ===============================================================
# ▶️ CREATE A VAULT:
#     vault = EncryptedVault()
#
# 🔐 STORE A MESSAGE:
#     vault.store_entry("My encrypted dream.")
#
# 🔓 RETRIEVE LAST ENTRY:
#     vault.retrieve_entry()
#
# 📤 EXPORT KEY:
#     vault.export_key()
#
# 📥 IMPORT KEY:
#     vault.import_key(existing_key_string)
#
# 🧠 GOOD FOR:
# - Storing symbolic thoughts, logs, memory events
# - Future quorum-based unlocking logic
# - Consent-based cognitive chain encryption
# ===============================================================
