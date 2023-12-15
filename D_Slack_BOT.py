class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.eow = (False,-1)
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, ind,word: str) -> None:
        node = self.root
        c = 0
        for ch in word:
            indx = ord(ch) - 97
            if node.children[indx] == None:
                node.children[indx] = TrieNode()   
            node = node.children[indx]
        node.eow = (True,ind)
    def search(self, ind,word: str) -> bool:
        node = self.root
        count = 0
        for ch in word:
            indx = ord(ch) - 97
            if node.children[indx] != None:
                node = node.children[indx]
                count += 1
            else:
                return count
        return count
n = int(input())
strs = []
for j in range(n):
    s = input()
    strs.append(s)
for i in range(len(strs)):
    t = Trie()
    for j in range(len(strs)):
        if i == j:
            continue
        t.insert(j,strs[j])
    print(t.search(i,strs[i]))
        
    
