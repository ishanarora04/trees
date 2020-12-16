import enum

class REDBLACK(enum.Enum):
    BLACK = 1
    RED = 0
    
class RedBlackTree:
    def __init__(self, value):
        self.value = value
        self.color = REDBLACK.BLACK
        self.left = None
        self.right = None

