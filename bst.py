class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_elem(self, value):

        if self.value is None:
            self.value = value
        elif self.left is None and self.value > value:
            self.left = BST(value)
        elif self.right is None and self.value < value:
            self.right = BST(value)
        else:
            if self.value > value:
                self.left.add_elem(value)
            else:
                self.right.add_elem(value)


    def transverse(self):
        print(self.value)
        if self.left is not None:
            self.left.transverse()
        if self.right is not None:
            self.right.transverse()


    def search(self, value):
        if self.value == value:
            return True
        elif self.value > value and self.left is not None:
            return self.left.search(value)
        elif self.value < value and self.right is not None:
            return self.right.search(value) 
        else:
            return False 
