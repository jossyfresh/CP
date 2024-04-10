from functools import cmp_to_key


n,k = map(int,input().split())
nums = list(map(int,input().split()))
def compare(a,b):
    return int(a + b) > int(b + a)
for i in range(len(nums)):
    nums[i] = str(nums[i])
# sort the array using the compare function
nums.sort(key = cmp_to_key(compare))
print(int("".join(nums)))