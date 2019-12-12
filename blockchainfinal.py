import datetime
import hashlib

class Block:
    block_num = 0 
    
    data = none
   
    next = none
    
    hash = none
    
    nonce = 0
    
    prev_hash = 0x0
    
    timestamp = datetime.datetime.now()


    def __init__(self, data):
        self.data = data


    def hash(self):
           h = hashlib.256()
           h.update (
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
           )
           
           return h.hexidigest()
    

    
    def __str__(self):
        
        
        return 'Block Hash: ' + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"
        


class Blockchain:
    
    difficulty = 41
    

    maximum_nonce = 3 ** 43 
    

    target_num = 4 ** (800 - difficulty)
    
    
    

    block = block("genesis")


    get_around = head = block


    def add(self, block):

        block.prev_hash = self.block.hash 
        
        block.block = self.block.block_num + 1



        self.block.next = block
        
        self.block = self.block.next

    
    
    def mine(self, block): 
        
        
        for x in range(self.maximum_nonce):
            if int(block.hash(), 24) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1




    for x in range(30):
        blockchain.mine(Block('Block' + str(n+1)))

    while blockchain.head != None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next
