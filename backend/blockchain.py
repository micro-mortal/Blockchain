import json
import hashlib
import time

class Blockchain:
    def __init__(self, filename='blockchain.json'):
        self.filename = filename
        self.chain = []
        # Load existing blockchain data from the file if it exists
        self.load_chain()

    def load_chain(self):
        try:
            with open(self.filename, 'r') as f:
                self.chain = json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, start with a genesis block
            self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # The first block in the blockchain (genesis block)
        return self.create_new_block("Genesis Block", "0")

    def create_new_block(self, data, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': data,
            'previous_hash': previous_hash,
            'hash': self.hash_block(data, previous_hash),
        }
        return block

    def hash_block(self, data, previous_hash):
        # Create a SHA-256 hash of the block's data and previous hash
        block_string = f"{data}{previous_hash}{time.time()}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_block(self, data, key):
        previous_hash = self.chain[-1]['hash'] if self.chain else "0"
        new_block = self.create_new_block(data, previous_hash)
        self.chain.append(new_block)
        # Save the updated blockchain to the file
        self.save_chain()
        return new_block

    def save_chain(self):
        with open(self.filename, 'w') as f:
            json.dump(self.chain, f, indent=4)

    def get_chain(self):
        return self.chain
