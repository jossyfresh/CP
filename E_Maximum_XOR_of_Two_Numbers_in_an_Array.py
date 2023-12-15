class TrieNode :
	def __init__(self):
		self.children = {}

class Trie :
	def __init__(self) :
		self.root = TrieNode()

	def insert(self, n) :
		temp = self.root
		i = 31
		while i >= 0 :
			bit = (n >> i) & 1
			if bit not in temp.children:
				temp.children[bit] = TrieNode()
			temp = temp.children[bit]
			i -= 1
	def xor(self, value) :
		temp = self.root
		current_ans = 0
		i = 31
		while i >= 0:
			bit = (value >> i) & 1
			if bit^1 in temp.children:
				temp = temp.children[bit^1]
				current_ans += (1 << i)
			else:
				temp = temp.children[bit]
			i -= 1
		return current_ans

t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    trie = Trie()
    max_val = 0
    trie.insert(num[0])
    for n in num[1:]:
        max_val = max(trie.xor(n),max_val)
        trie.insert(n)
    print(max_val)


