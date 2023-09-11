//use heaps (max-heap) to implement it 
#include "max_heap.h"
#include <string>
#include <utility> // pair

using namespace std;


// insert(S, x, k)
// int maximum(S){
//     if S.heap
// } // return the element of S with the largest key (highest priority)
// extract_max(S) // remove and return the element of S with the largest key 
// increase_key(S, x, k) // increase the value of element x's key to the new value k, which is assumed to be at least as large as x's current key value 

#include<iostream>
#include<queue> // FIFO 
#include<vector>

class Mountain {

    public:
        string name;
        int height;
    // Initialization list 사용 : 뒤에 name = arg_name, height = arg_height으로 사용 
    // constructor body 전에 call된다. 
    Mountain ( std :: string arg_name, int arg_height) : name(arg_name), height(arg_height){}
    
    //this pointer는 자동으로 생성되며 public이 아닌 methods 내에서만 사용가능하다. 자기 자신 (object)를 가리키는 포인터  
    bool operator < (const Mountain& obj) const {
        if (this->name.size() < obj.name.size()) {
            return true;
        }
        return false;
    }
};

class CompareName {

    public:
    bool operator() (const Mountain& a, const Mountain& b) const {
        // Mountain with smaller name goes below
        if (a.name.size() < b.name.size())
            return true;
        return false;
    }
};

int main() {

    //std :: priority_queue<Mountain, std :: vector<Mountain>, CompareName> pq_mountains;
    std :: priority_queue<Mountain> pq_mountains;

    Mountain m1("K2", 8611);
    Mountain m2("Kangchenjunga", 8586);
    Mountain m3("Everest", 8848);
    Mountain m4("Annapurna", 8091);

    pq_mountains.push(m1);
    pq_mountains.push(m2);
    pq_mountains.push(m3);
    pq_mountains.push(m4);

    std :: cout << "Max heap using priority_queue." << std :: endl;
    std :: cout << "Arranging mountain name(s) based on the length (max_heap) of the names." << std :: endl;
    std :: cout << "Mountain with longest name comes at the top.\n" << std :: endl;
    while (!pq_mountains.empty()) {
        Mountain mount = pq_mountains.top();
        pq_mountains.pop();
        std :: cout << mount.name << " " << mount.height << std :: endl;
    }


    std :: vector<int> vec_nums { 5, 2, 7, 13, 11 };
    std :: priority_queue<int> pq_maxheap (vec_nums.begin(), vec_nums.end());

    std :: cout << "\nElements in vector : ";
    for (const auto& num : vec_nums) {
         std :: cout << num << " ";
    }

    std :: cout << "\nElements in max heap (created from vector) : ";
    while (!pq_maxheap.empty()) {
        std :: cout << pq_maxheap.top() << " ";
        pq_maxheap.pop();
    }

    std :: priority_queue<int, std :: vector<int>, std :: greater<int>> pq_minheap;
    pq_minheap.push(5);
    pq_minheap.push(2);
    pq_minheap.push(7);
    pq_minheap.push(13);
    pq_minheap.push(11);

    std :: cout << "\nElements in min heap (created from vector) : ";
    while (!pq_minheap.empty()) {
        std :: cout << pq_minheap.top() << " ";
        pq_minheap.pop();
    }
    return 0;
}
