from heapq import heappop, heappush, heapify 

# creating empty heap 
heap = []
heapify(heap)

# Adding items to the heap using heappush 
# function by multiplying them with -1 
'''
By default Min Heap is implemented by this class.
But we multiply each value by -1 so that we can use it as MaxHeap

'''


heappush(heap, -1*10)
heappush(heap, -1*30)
heappush(heap, -1*20)
heappush(heap, -1*400)

# Printing the value of maximum element 
# access the element in the same way we do in a list (slicing) 
print("Head value of heap: " + str(-1*heap[0]))

# printing the elements of the heap 
print("The heap elements : ")
for i in heap:
    print((-1*i), end = " ")

print("\n")

# pop 
element = heappop(heap)