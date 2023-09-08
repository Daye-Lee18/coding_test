#include "max_heap.h"

using namespace std;

void Maxheap::maxHeapify(int pos, int heapSize){
    int largest = pos; // Initialize largest as root
    int l = 2 * pos ; // left = 2*i + 1
    int r = 2 * pos +1; // right = 2*i + 2
 
    // If left child is larger than root, equal 표시 반드시 있어야 함. 
    if (l <= heapSize && Heap[l] > Heap[largest])
        largest = l;
 
    // If right child is larger than largest so far
    if (r <= heapSize && Heap[r] > Heap[largest])
        largest = r;
 
    // If largest is not root
    if (largest != pos) {
        swap(Heap[pos], Heap[largest]);
 
        // Recursively heapify the affected sub-tree
        maxHeapify(largest, heapSize -1);
    }
}

void Maxheap::insert(int element){
    if (size >= maxsize){
        return ;
    }

    size++;
    Heap[size] = element;

    int current = size;

    //     // 내가 오른쪽 노드인 경우, 부모의 왼쪽/오른쪽 node와도 비교 필요 
    // if (isLeaf(current) && Heap[leftChild(parent(current))] < Heap[current]){
    //     swap(Heap[leftChild(parent(size))], Heap[current]);
    // }

    //bottom-up approach 
    while (Heap[current] > Heap[parent(current)]){
        swap(Heap[current], Heap[parent(current)]);
        current = parent(current);
    }


}

int Maxheap::extractMax(){
    if (size == 0){
        return -1; // Handle empty heap case 
    }

    int popped = Heap[FRONT];

    Heap[FRONT] = Heap[size];
    size--;
    maxHeapify(FRONT, size);

    return popped;
}

void Maxheap::Print(){
    if (Heap.empty()){
        cout << "Heap is empty." << endl;
        return;
    }

    for (int i =1 ; i <= size/2; i++){
        if (i <= size)
            cout << "PARENT : " << Heap[i];
        if (2*i <= size)
            cout << " LEFT CHILD : " << Heap[2*i];
        if (2*i + 1 <= size) 
            cout << " RIGHT CHILD : " << Heap[2*i +1] << endl; }

}

void Maxheap::increaseKey(int i, int new_val){
    //assume that new_val is greater than than Heap[i]
    if (new_val < Heap[i]){
        cout << "new value is smaller than the original one";
    }
    else {
        Heap[i] = new_val;
        while ( i != 0 && Heap[parent(i)] < Heap[i]){
            swap(Heap[i], Heap[parent(i)]);
            i = parent(i);
        }
    }
}

// This function deletes key at index i. It first reduced value to minus
// infinite, then calls extractMax()
void Maxheap::deleteKey(int i){
    if (size == 0){
        return ; // Handle empty heap case 
    }
    
    increaseKey(i, INT_MAX);
    extractMax(); // extractMax()에서 size도 하나 줄여줌

}

void Maxheap::heapSort(){
    build_max_heap(size);
    int heapSize = size; 
    for (int i = size ;i>=2; --i){ //Heap.size()를 size랑 헷갈려서는 안됨. Heap.size()는 max_size이고 size는 현재 Heap에 있는 element 개수 
        swap(Heap[FRONT], Heap[i]); //Move current root to end 
        // heapifyDown(FRONT, i-1); // Restore max hepa property on the reduced heap  
        // heapifyDown(0, i-1); // Restore max hepa property on the reduced heap  
        heapSize -= 1 ;
        maxHeapify(FRONT, heapSize);
    }

}

void Maxheap::build_max_heap(int heapSize){
    if (heapSize >= 2){
        for (int i = heapSize/2; i != 0 ; --i){
            maxHeapify(i, heapSize);
        }
    }
}

int main() {
    Maxheap maxHeap(10);
    // 15 10 7 5 3 
    maxHeap.insert(5);
    maxHeap.insert(10);
    maxHeap.insert(7);
    maxHeap.insert(3);
    maxHeap.insert(15);
    maxHeap.insert(36);
    maxHeap.insert(1);
    maxHeap.insert(40);

    std::cout << "Max element: " << maxHeap.getMax() << std::endl;

    maxHeap.Print(); 
    std::cout << '\n';

    std::cout << "Extracting max element: " << maxHeap.extractMax() << '\n';
    std::cout << "After extractin max element: \n";
    maxHeap.Print();    
    std::cout << '\n';

    maxHeap.increaseKey(2, 20);

    std::cout << "After increase element's key: \n";
    maxHeap.Print();
    std::cout << '\n';

    std::cout << "Max element after increasing key: " << maxHeap.getMax() << '\n';
    std::cout << '\n';

    maxHeap.deleteKey(1);

    std::cout << "After deleting a key: \n" << std::endl;
    maxHeap.Print();
    std::cout << '\n';

    maxHeap.heapSort();
    cout << "Sorted elements using HeapSort: \n";
    maxHeap.Print();
    
    return 0;
}