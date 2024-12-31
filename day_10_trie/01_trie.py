class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def visualize(self, node=None, prefix="", level=0):
        if node is None:
            node = self.root
        for char, child_node in node.children.items():
            print("    " * level + f"└── {char}")
            if child_node.is_end_of_word:
                print("    " * (level + 1) + "(End of word)")
            self.visualize(child_node, prefix + char, level + 1)

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def start_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):
        def _delete(node, word, depth):
            if not node:
                return False
            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char in node.children:
                should_delete_child = _delete(node.children[char], word, depth + 1)
                if should_delete_child:
                    del node.children[char]
                return not node.is_end_of_word and len(node.children) == 0
            return False
        _delete(self.root, word, 0)


trie = Trie()

trie.insert("ali")
trie.insert("alp")
trie.insert("alperen")

trie.visualize()

result = trie.search("alp")
print(result)

result = trie.start_with("alper")
print(result)

# trie.delete("ali")
# trie.delete("alp")
trie.delete("alperen")
trie.visualize()

