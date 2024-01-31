import itertools

class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def add_left(self, node):
        """Adds node as the left child"""    
        self.left = node

    def add_right(self, node):
        """Adds node as the right child"""
        self.right = node
        
    def evaluate(self):
        """Reeeursively evalute the subtree rooted at BETNode"""
        # Base case - If self.value is an integer, return it
        if self.value in BETNode.CARD_VAL_DICT:
            return BETNode.CARD_VAL_DICT[self.value]
        
        # Recursively evaluate left side
        left_val = self.left.evaluate()
        
        # Recursively evaluate right side
        right_val = self.right.evaluate()
        if self.value == '+':
            return left_val + right_val
        elif self.value == '-':
            return left_val - right_val
        elif self.value == '*':
            return left_val * right_val
        elif self.value == '/':
            # If dividing by zero, returns None
            if right_val == 0:
                return None
            else:
                return left_val / right_val
    
    def __repr__(self):
        """String representation for the expression"""
        # Base case - If self.value is an integer, return it
        if self.value in BETNode.CARD_VAL_DICT:
            return self.value
        
        # Recursively evaluate left side
        left_val = self.left.__repr__()

        # Recursively evaluate right side
        right_val = self.right.__repr__()
        if self.value == '+':
            return f'({left_val}+{right_val})'
        elif self.value == '-':
            return f'({left_val}-{right_val})'
        elif self.value == '*':
            return f'({left_val}*{right_val})'
        elif self.value == '/':
            # If dividing by zero, returns None
            if right_val == 0:
                return None
            else:
                return f'({left_val}/{right_val})'


def create_trees(cards):
    """Return a set of every valid tree for a given collection of 4 cards."""
    # Base case - if length of cards = 1
    if len(cards) == 1: return [BETNode(cards[0])]
    trees = set()
    for i in range(1, len(cards)):
        for left_cards in itertools.combinations(cards, i):
            right_cards = tuple(c for c in cards if c not in left_cards)

            # Recursively follow left side of tree
            left_trees = create_trees(left_cards)
            # Recusively follow right side of tree
            right_trees = create_trees(right_cards)

            for operator in BETNode.OPERATORS:
                for left_tree, right_tree in itertools.product(left_trees, right_trees):
                    tree = BETNode(operator, left_tree, right_tree)

                    trees.add(tree)
    return trees
    

def find_solutions(cards):
    """Calls create_trees(cards) to get all valid trees for a passed in 4-card hand, then evaluates each tree and
        returns a set of all the ways to get 24."""
    solutions = set()
    for tree in create_trees(cards):
        # Adds tree to solution set if = 24
        if tree.evaluate() == 24:
            solutions.add(repr(tree))
    return solutions