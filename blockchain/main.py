from block1 import Block

blockchain = []

genesis_block = Block('Chancellor on the brink...', ['Satoshi sent 1 BTC to ME',
                                                     'Me sent 3 BTC to Jenny',
                                                     'Satoshi sent 1 BTC to Finney'])

second_block = Block(genesis_block.block_hash, ['some more BTC'])
third_block = Block(genesis_block.block_hash, ['A lot more more BTC'])


print(genesis_block.block_hash)
print(second_block.block_hash)
print(third_block.block_hash)