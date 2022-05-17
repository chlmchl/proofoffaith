import hashlib
from itertools import chain
import json
from time import time, sleep
import random
# import pynput

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash='Do you believe in blockchain?', proof=100)
    
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block
    
    @property
    def last_block(self):

        return self.chain[-1]

    def new_transaction(self, txt):
        transaction = {
            'timestamp': time(),
            'txt': txt
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1
    
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash
    
    
blockchain = Blockchain()

t1 = blockchain.new_transaction("Hello world")
t2 = blockchain.new_transaction("blabla")
t3 = blockchain.new_transaction("yoyoyoyo")
blockchain.new_block(12345)

t4 = blockchain.new_transaction("blockchain")
t5 = blockchain.new_transaction("is the")
t6 = blockchain.new_transaction("future")
blockchain.new_block(6789)

with open('blockchain.json', 'w') as fp:
    json.dump(blockchain.chain, fp)

while True:
    with open('blockchain.json', 'r') as fp:
        listBlock = json.load(fp)

    blockchain.new_transaction(input('Blockchain is :'))
    sleep(0.5)
    print('new pending belief')
    sleep(1)
    print('mining...')
    sleep(1)
    proof = random.randint(1000,9999)
    new_block = blockchain.new_block(proof)
    listBlock.append(new_block)

    with open('blockchain.json', 'r+') as json_file:
        json.dump(listBlock, json_file)

    sleep(1)
    print(blockchain.chain)
    sleep(3)



 