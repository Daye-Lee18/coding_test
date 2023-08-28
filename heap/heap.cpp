#include <iostream>
using namespace std;

//A class for Heap 

class Heap{
    // default = private 
    // constructor는 default가 public이었나...? 기억이 안나네 

    int *harr; //pointer to array of elements in heap 
    int capacity; //maximum possible size of heap 
    int heap_size; //Current number of elements in heap 
    
    public: 
        //Constructor 
        Heap(int capacity);

        //Inserts a new key 'k'
        void insertKey(int k);

        //to get index of parent node at index i 
        int parent(int i) {return i-1/2;}

        //to get index of left child of node at index i 
        int left(int i ) {return (2*i +1);}

        //to get index of right child of node at index i 
        int right(int i) {return (2*i + 2);}

};

//Inserts a new key 'k' 
void Heap::insertKey(int k){
    if (heap_size == capacity){
        cout << "\nOverflow: Could not insertKey\n";
        return ;
    }

    //First insert the new key at the end 
    heap_size++;
    int i = heap_size -1;
    harr[i] = k;


}