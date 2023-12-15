def heappush(heap,value):
    heap.append(value)
    current = len(heap) - 1
    heapify_up(heap,current)
def heappop(heap):
    if not heap:
        return None
    min_value = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    current = 0
    heapify_down(heap,len(heap),current)
    return min_value
def heapify_down(heap, n, current):
    child = current
    left = 2 * current + 1
    right = 2 * current + 2
    if left < n and heap[left] > heap[child]:
        child = left
    if right < n and heap[right] > heap[child]:
        child = right
    if child != current:
        heap[current],heap[child] = heap[child],heap[current]
    heapify_down(heap,n,child)
def heapify_up(heap,current):
    parent = (current - 1) // 2
    if parent < 0:
        return
    if heap[current] < heap[parent]:
        heap[current], heap[parent] = heap[parent], heap[current]
        heapify_up(heap,parent)
def test():
    heap = [2, 4, 5, 7, 9, 10]
    heappush(heap, 3)
    assert heap == [2, 4, 3, 7, 9, 10, 5], f"Error: expected [2, 4, 3, 7, 9, 10, 5], but got {heap}"

    heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    heappush(heap, 0)
    assert heap == [0, 1, 3, 4, 2, 6, 7, 8, 9, 5], f"Error: expected [0, 2, 1, 4, 5, 6, 7, 8, 9, 3], but got {heap}"

    print("Great Job !!!")
test()