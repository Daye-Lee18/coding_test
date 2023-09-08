from heapq import heappop, heappush, heapify 

'''
1. heapify, heappop, heappush 
2. dictionary <-> list <-> heapify 
3. class 만들어서, customer comparator 생성 및 비교 대상 정하기 

'''

#####################################################  1   ############################################

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

#####################################################  2    ############################################
'''
dictionary as heap 

'''

dict_1 = {11: 121, 2: 4, 5:25, 3:9}

#convert dict to list of tuples 

di = list(dict_1.items())

print("dictionary into list :", di) # dictionary into list : [(11, 121), (2, 4), (5, 25), (3, 9)]

#converting into heap 
heapify(di) 
print("Heapified list of tuples :", di) # Heapified list of tuples : [(2, 4), (3, 9), (5, 25), (11, 121)]

#converting heap to dictionary
di = dict(di) 
print("Dictionary as heap :", di) # Dictionary as heap : {2: 4, 3: 9, 5: 25, 11: 121}

'''
tuple안에 여러개의 원소가 있어도 맨 앞의 원소로 min-heap으로 정렬된다. 

'''
list1 = [('a', 1, 3), ('z', 1,25), ('b', 3 , 5), ('d', 1, 8) ]

heapify(list1)

print(list1) # [('a', 1, 3), ('d', 1, 8), ('b', 3, 5), ('z', 1, 25)]

#####################################################  3  ############################################

class node:
    def __init__(self, A, B):
        self.A = A
        self.B = B 

    def __lt__(self, other):
        if self.A < other.A: # 오름차순 
            return True 
        elif self.B == other.B: # 첫번째 변수가 같으면 두번째 변수로 내림차순 
            return self.B >  other.B
        else:
            return False 
    
    def __str__(self):
        return 'A: {}, B: {}'.format(self.A, self.B)
    

l = []
heappush(l, node(1,1))
heappush(l, node(1,2))
heappush(l, node(2,1))
heappush(l, node(2,2))
heappush(l, node(3,1))
heappush(l, node(3,2))

while l:
    print(heappop(l))

'''
A: 1, B: 1
A: 1, B: 2
A: 2, B: 1
A: 2, B: 2
A: 3, B: 2
A: 3, B: 1
> 
'''