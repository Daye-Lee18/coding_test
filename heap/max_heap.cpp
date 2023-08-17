#include <iostream>
#include <vector> 
using namespace std;

#define MAX 1000 //MAX SIZE OF HEAP

class Maxheap{
    private:
        int maxsize;
        int size;
        vector<int> Heap;
        const int FRONT = 1;
        
        int parent(int pos) {
            return pos /2;
        }

        int leftChild(int pos){
            return pos * 2;
        }

        int rightChild(int pos){
            return 2*pos + 1;
        }

        bool isLeaf(int pos){
            if (pos >= (size/2) && pos <= size){
                return true;
            }
            return false;
        }
        // call by reference 
        void swap(int &a, int &b){
            int temp = a; // 하나의 값을 temp에 저장 
            a = b;  // 위에서 저장한 variable을 다른 값으로 치환 
            b = temp;   // 나머지 variable에 temp 값 저장 
        }

        void maxHeapify(int pos);

    public:
        //Constructor 
        Maxheap(int maxSize){
            maxsize = maxSize;
            size = 0;
            Heap.resize(maxsize +1); // vector member function 
            Heap[0] = INT_MAX;
        }
        
        void insert(int element);
        int extractMax();
        void Print();

};

void Maxheap::maxHeapify(int pos){
    if (!isLeaf(pos)){
        if (Heap[pos] < Heap[leftChild(pos)] ||
            Heap[pos] < Heap[rightChild(pos)]
        ){
            if ( Heap[leftChild(pos)] > Heap[rightChild(pos)]){
                swap(Heap[pos], Heap[leftChild(pos)]);
                maxHeapify(leftChild(pos));
            } else {
                swap(Heap[pos], Heap[rightChild(pos)]);
                maxHeapify(rightChild(pos));
            }
        }
    }
}

void Maxheap::insert(int element){
    if (size >= maxsize){
        return ;
    }

    size++;
    Heap[size] = element;

    int current = size;

    //bottom-up approach 
    while (Heap[current] > Heap[parent(current)]){
        swap(Heap[current], Heap[parent(current)]);
        current = parent(current);
    }
}

int Maxheap::extractMax(){
    int popped = Heap[FRONT];

    Heap[FRONT] = Heap[size];
    size--;
    maxHeapify(FRONT);

    return popped;
}

void Maxheap::Print(){
    for (int i =1 ; i <= size/2; i++){
        cout << "PARENT : " << Heap[i]
            << " LEFT CHILD : " << Heap[2*i]
            << " RIGHT CHILD : " << Heap[2*i +1] << endl;    }

}

int main(){

    Maxheap maxHeap(15);
    maxHeap.insert(5);
    maxHeap.insert(3);
    maxHeap.insert(17);
    maxHeap.insert(10);
    maxHeap.insert(84);
    maxHeap.insert(19);
    maxHeap.insert(6);
    maxHeap.insert(22);
    maxHeap.insert(9);

    std::cout << "Max Heap elements: " << std::endl;
    maxHeap.Print();

    std::cout << "Extracted max element: " << maxHeap.extractMax() << std::endl;

    std::cout << "Max Heap after extraction: " << std::endl;
    maxHeap.Print();

    return 0;


}