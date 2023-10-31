
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False
        
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    # prefix search
    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):
        
        def _delete(node, word, index):
            if index == len(word): # reached at the end
                if node.is_end_of_word:
                    node.is_end_word = False
                    return not bool(node.children)
                return False
            
            char = word[index] # finding the character
            
            if char not in node.children: # if character is not present in the childrens
                return False
            
            should_delete = _delete(node.children[char], word, index+1) # recursively check all
            
            if should_delete:
                del node.children[char]
                return not bool(node.children)
            
            return False
        
        _delete(self.root, word, 0)
        
    def _find_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            words.extend(self._find_words(child, prefix + char))
        return words
    
    def get_all_words(self):
        return self._find_words(self.root, "")
    
    def __str__(self) -> str:
        return str(self.get_all_words())
    
    
    
if __name__ == "__main__":
    a = Trie()
    ls = ['abs', 'ahd', 'aherowfo', 'hola']
    for i in ls:
        a.insert(word=i)
    print(a)
    a.delete('hola')
    print(a)
    
    
    
        
    
    
    
    