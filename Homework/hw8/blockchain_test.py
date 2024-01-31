import unittest
from blockchain import Transaction, Block, Ledger, Blockchain

class TestTransaction(unittest.TestCase):
    "A test case for the Transaction class"
    def test_transaction(self):
        "Test the string representation of a Transaction object"
        t = Transaction('user1', 'user2', 50)
        self.assertEqual(str(t), 'Transaction Details: Sender: user1, Recipient: user2, Amount: 50')
    
class TestBlock(unittest.TestCase):
    "A test case for the Block class"
    def setUp(self):
        "Set up the test case by creating a blok object and some Transaction objects"
        self.t1 = Transaction('user1', 'user2', 50)
        self.t2 = Transaction('user2', 'user3', 20)
        self.block = Block([self.t1, self.t2], previous_block_hash='123')

    def test_add_transaction(self):
        "Test adding a Transaction object to a Block object"
        t3 = Transaction('user3', 'user1', 10)
        self.block.add_transaction(t3)
        # Asserts that the length of transactions is 3
        self.assertEqual(len(self.block.transactions), 3)
        # Asserts whether the block has been added to transaction list
        self.assertIn(t3, self.block.transactions)
    
class TestLedger(unittest.TestCase):
    "A test case for the Ledger class"
    def setUp(self):
        "Set up the test case by creating a Ledger object"
        self.ledger = Ledger()

    def test_has_funds(self):
        "Test the has_funds method of a Ledger class"
        # Asserts false if user1 does not have funds
        self.assertFalse(self.ledger.has_funds('user1', 50))
        self.ledger.deposit('user1', 100)
        # Asserts true if user1 has funds
        self.assertTrue(self.ledger.has_funds('user1', 50))
        # Asserts false if user2 does not have funds
        self.assertFalse(self.ledger.has_funds('user1', 150))

    def test_deposit(self):
        "Test the deposit and transfer methods of the Ledger class"
        self.ledger.deposit('user1', 100)
        self.ledger.transfer('user1', 'user2', 50)
        # Assert that user1 has a balance of 50
        self.assertEqual(self.ledger._hashmap.__getitem__('user1'), 50)
        # Assert that user2 has a balance of 50
        self.assertEqual(self.ledger._hashmap.__getitem__('user2'), 50)
        # Assert that user1 does not have sufficient funds for a transfer of an amount 100
        self.assertFalse(self.ledger.transfer('user1', 'user2', 100))

class TestBlockchain(unittest.TestCase):
    "A test for the Blockchain class"
    def setUp(self):
        "Set up the test case by creating a Blockchain object"
        self.blockchain = Blockchain()

    def test_create_genesis_block(self):
        "Test creating the gensis block of the blockchain"
        # Asserts that length of block chain is 1
        self.assertEqual(len(self.blockchain._blockchain), 1)
        # Asserts that length of transaction is 1
        self.assertEqual(len(self.blockchain._blockchain[0].transactions), 1)

    def test_distribute_mining_reward(self):
        "Test distributing a mining reward in the blockchain"
        self.blockchain.distribute_mining_reward('user1')
        # Asserts that the length of the blockchain is 2
        self.assertEqual(len(self.blockchain._blockchain), 2)
        self.assertEqual(self.blockchain._blockchain[1].transactions[0].from_user, "ROOT")
        self.assertEqual(self.blockchain._blockchain[1].transactions[0].to_user, 'user1')
        # Asserts if distribute mining reward initializes an initial balance
        self.assertEqual(self.blockchain._blockchain[1].transactions[0].amount, 1000)

    def test_add_block1(self):
        "Create a block with a valid previous_block_hash and a valid transaction"
        transaction = Transaction("user1", "user2", 10)
        self.blockchain.distribute_mining_reward('user1')
        block = Block([transaction], self.blockchain._blockchain[-1].previous_block_hash)
        
        # Add the block to the blockchain
        result = self.blockchain.add_block(block)
        
        # Check if the block was added successfully
        self.assertTrue(result)
        self.assertEqual(len(self.blockchain._blockchain), 3)  # Check if the blockchain has 2 blocks now
    
    def test_add_block2(self):
        "Create a block with an invalid previous_block_hash and a valid transaction"
        transaction = Transaction("user1", "user2", 10)
        block = Block([transaction], "invalid_hash")
        
        # Add the block to the blockchain
        result = self.blockchain.add_block(block)
        
        # Check if the block was not added due to invalid previous_block_hash
        self.assertFalse(result)
        self.assertEqual(len(self.blockchain._blockchain), 1)  # Check if the blockchain still has only 1 block
        
    def test_add_block3(self):
        "Create a block with a valid previous_block_hash and a transaction with insufficient funds"
        transaction = Transaction("user1", "user2", 1000)
        block = Block([transaction], self.blockchain._blockchain[-1].previous_block_hash)
        
        # Add the block to the blockchain
        result = self.blockchain.add_block(block)
        
        # Check if the block was not added due to insufficient funds in the ledger
        self.assertFalse(result)
        self.assertEqual(len(self.blockchain._blockchain), 1)  # Check if the blockchain still has only 1 block

    def test_validate_chain(self):
        "Tests a valid chain"
        # Create a sample blockchain with one block and one transaction
        self.blockchain = Blockchain()
        self.transaction = Transaction('user1', 'user2', 10)
        self.block = Block([self.transaction])
        # Add the block to the blockchain
        self.blockchain.add_block(self.block)
        # Validate the blockchain
        result = self.blockchain.validate_chain()
        # Assert that the result is True
        self.assertTrue(result)
 
unittest.main()