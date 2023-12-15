t = int(input())
for a in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    let = num.copy()
    let.sort()
    count = [0]
    def mergesort(l,r,arr):
        if l == r:
            return [arr[l]]
        mid = l + (r-l)//2
        le = mergesort(l,mid,arr)
        ri = mergesort(mid+1,r,arr)
        return merge(le,ri)
    def merge(left,right):
        new = []
        if left[0] < right[0]:
            new.extend(left)
            new.extend(right)
        else:
            new.extend(right)
            new.extend(left)
            count[0]+=1
        return new
    if mergesort(0,len(num)-1,num) == let:
        print(count[0])
    else:
        print(-1)
        
    