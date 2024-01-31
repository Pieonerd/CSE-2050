import hashmap

class Transaction():
    def __init__(self, from_user, to_user, amount):
        "Initializes a new transaction object"
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount

    def __repr__(self):
        "Returns a string representation of the Transaction object"
        return f'Transaction Details: Sender: {self.from_user}, Recipient: {self.to_user}, Amount: {self.amount}'
    
class Block():
    def __init__(self, transactions=None, previous_block_hash=None):
        "Initializes a new block object"
        self.transactions = transactions or []
        self.previous_block_hash = previous_block_hash

    def add_transaction(self, transaction):
        "Adds a transaction to the block"
        self.transactions.append(transaction)

class Ledger():
    def __init__(self):
        "Initializes a new Ledger object"
        self._hashmap = hashmap.HashMapping()

    # def has_funds(self, user, amount):
    #     if user not in self._hashmap:
    #         return False
    #     balance = self._hashmap.get(user)
    #     return balance >= amount
    
    def has_funds(self, user, amount):
        "Checks if a user has enough funds for a given amount"
        # If user is not found in hashmap returns false
        if user not in self._hashmap:
            return False
        # Determine if user's balance is greater than amount asked
        balance = self._hashmap.__getitem__(user)
        return balance >= amount

    def deposit(self, user, amount):
        "Deposits funds into a user's account"
        # If user is not found in hashmap, adds the user and sets respective amount
        if user not in self._hashmap:
            self._hashmap[user] = amount
        # If user is in hashmap, adds amount to existing balance
        else:
            self._hashmap[user] += amount

    def transfer(self, from_user, to_user, amount):
        "Transfers funds from one user to another"
        # If user does not have funds, returns false
        if not self.has_funds(from_user, amount):
            return False
        # If from_user has funds, subtract amount from balance
        self._hashmap[from_user] -= amount
        # Deposite amount to to_user
        self.deposit(to_user, amount)
        return True

class Blockchain():
    '''Contains the chain of blocks.'''

    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################

    def __init__(self):
        self._blockchain = list()     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        '''
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to 
        provide initial balances to one or more users.'''
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)

    # TODO - add the rest of the code for the class here
    def add_block(self, block):
        "Adds a block to the blockchain"
        # Check if the block being added has the correct hash of the previous block
        previous_block = self._blockchain[-1]
        if previous_block.previous_block_hash != block.previous_block_hash:
            return False
        
        # Iterate through transactions in the block
        for transaction in block.transactions:
            # Check if the user transferring HuskyCoin has the required balance
            if not self._bc_ledger.has_funds(transaction.from_user, transaction.amount):
                return False
            # Update the ledger of balances
            self._bc_ledger.transfer(transaction.from_user, transaction.to_user, transaction.amount)
        
        # Add the block to the blockchain
        self._blockchain.append(block)
        return True


    def validate_chain(self):
        '''
        Validates the integrity of the blockchain by checking if any blocks have been tampered with.
        Returns a list of blocks that have been tampered with.
        '''
        tampered_blocks = []  # list to store tampered blocks
        previous_block_hash = None

        # Iterate through each block in the blockchain
        for block in self._blockchain:
            # Check if the hash of the previous block matches the previous_block_hash of the current block
            if block.previous_block_hash != previous_block_hash:
                # If not, add the current block to tampered_blocks list
                tampered_blocks.append(block)

            # Calculate the hash of the current block and compare it with the stored hash
            if hash(block) != block.previous_block_hash:
                # If the calculated hash doesn't match the stored hash, add the current block to tampered_blocks list
                tampered_blocks.append(block)

            previous_block_hash = block.previous_block_hash

        return tampered_blocks