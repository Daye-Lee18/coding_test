import sys 

# heappush, heapify, heappop 
class maxheap:
    def __init__(self, max_size):
        self.max_size = max_size 
        self.FRONT = 1 
        self.size = 1
        self.heap = [sys.maxsize]

    def heappop(self, heap):
        if self.size < 1:
            return 
        
        popped = heap[self.FRONT]
        heap[self.FRONT] = heap[self.size]
        self.size -= 1
        self.heapify(heap)

        return popped 
    def IsLeaf(self, pos):
        if pos <= self.size and pos >= self.size // 2 :
            return True 
        return False 
    
    def leftchild(self, pos):
        return pos *2
    
    def rightchild(self, pos):
        return pos*2 + 1 
    
    #use recursion 
    def heapify(self, pos):
        if not self.IsLeaf(pos):
            # if the first element is smaller than the child 
            if self.heap[pos] < self.heap[self.leftchild(pos)] or self.heap[pos] < self.heap[self.rightchild(pos)]:
                # swap the leftchild with current pos 
                if self.heap[self.leftchild(pos)] > self.heap[self.rightchild(pos)]:
                    self.swap(pos, self.leftchild(pos))
                    self.heapify(self.leftchild(pos))
        return 
    
    def swap(self, spos, fpos):
        self.heap[spos], self.heap[fpos] = self.heap[fpos], self.heap[spos]
        return 
    
    def parent(self, pos):
        return pos//2

    def heappush(self, value):
        self.size += 1 
        self.heap[self.size+1] = value 

        cur = self.size 
        # bottom-up approach to make the new array into max-heap 
        while cur != self.FRONT:
            if self.heap[self.parent(cur)] < self.heap[cur]:
                self.swap(cur, self.parent(cur))
                cur = self.parent(cur)
        return 



