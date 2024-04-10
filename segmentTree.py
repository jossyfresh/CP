class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.tree[self.n:] = nums
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 0:
            left = right = i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i - 1
            self.tree[i // 2] = self.tree[left] + self.tree[right]
            i //= 2

    def sumRange(self, i, j):
        i += self.n
        j += self.n
        total = 0
        while i <= j:
            if i % 2 == 1:
                total += self.tree[i]
                i += 1
            if j % 2 == 0:
                total += self.tree[j]
                j -= 1
            i //= 2
            j //= 2
        return total