class Tree:
    def __init__(self, val=None):
        self.value = val
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def isempty(self):
        return (self.value == None)
    
    def insert(self, data):
        if self.isempty():
            self.value = data
            self.left = Tree()
            self.right = Tree()
            print("{} is inserted successfully.".format(self.value))
        elif data < self.value:
            self.left.insert(data)
            return
        elif data > self.value:
            self.right.insert(data)
        elif data == self.value:
            return

t = Tree(15)
t.insert(10)
t.insert(18)
t.insert(4)
t.insert(4)
t.insert(11)
t.insert(16)
t.insert(20)
        