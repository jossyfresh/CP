def merge(arr1,arr2):
    l = 0
    r = 0
    new = []
    while l < len(arr1) or r < len(arr2):
        if r < len(arr2) and ( l == len(arr1) or arr1[l] > arr2[r]):
            new.append(arr2[r])
            r += 1
        elif l < len(arr1) and  (r == len(arr2) or arr2[r] > arr1[l]):
            new.append(arr1[l])
            l+=1
    return new   
print(merge([1,2],[0,5]))         