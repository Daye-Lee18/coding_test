#pragma once 

#include <iostream>
#include <vector> 
#include <climits> // INT_MAX, INT_MIN
using namespace std;

#define MAX 1000 //MAX SIZE OF HEAP

// member function 
// public: constructor, insert, extractMax, increaseKey, deleteKey, getMax, heapSort, build_max_heap 
// private: maxHeapify, swap

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

        void maxHeapify(int pos, int heapSize); // size는 private에 있지만 자유자재로 사이즈를 임의로 지정해야할 때가 있어서 변수로 있어야 편함. 

    public:
        //Constructor 
        Maxheap(int maxSize){
            maxsize = maxSize;
            size = 0;
            Heap.resize(maxsize +1); // vector member function 
            Heap[0] = INT_MAX;
        }
        
        int getMax(){
            return Heap[1];
        }

        void insert(int element);
        int extractMax();
        void Print();
        void increaseKey(int i, int new_val); // increase key value of key at index i to new_val 
        
        // c++에는 dynamically allocated 된 메모리를 지워주는 delete operator가 있어서 deletekey로 이름을 대신함. 
        void deleteKey(int i); // deletes a key stored at index i 

        void heapSort();
        // void heapifyDown(int index, int heapSize);
        void build_max_heap(int heapSize);
        // void delete_help_heapify(int pos);
};