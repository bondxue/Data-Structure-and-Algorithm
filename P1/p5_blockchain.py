import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        if data is None:
            return

        self.size += 1
        node = self.head
        if node is None:
            block = Block(datetime.datetime.now, data, None)
            self.head = block
        else:
            while node.next:
                node = node.next
            node.next = Block(datetime.datetime.now(), data, node.hash)


# Test Case
chain = BlockChain()
chain.add('block1')
chain.add('block2')
chain.add('block3')
chain.add(None)

print(chain.head.data)  # print block1

block2 = chain.head.next
block3 = chain.head.next.next
print('Pass' if block2.hash == block3.previous_hash else 'Fail')  # print Pass

print(block3.data)  # print block3
