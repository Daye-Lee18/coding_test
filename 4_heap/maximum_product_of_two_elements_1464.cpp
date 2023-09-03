#include <queue>
#include <iostream>

using namespace std;

class Solution {
    public:
        int maxProduct(vector<int>& nums) {
            
            //default = max_heap, less<int> 
            priority_queue<int, vector<int>, less<int>> pq;


            for (int i = 0 ; i < nums.size() -1 ; i++){
                for (int j = i+1; j < nums.size() ; j++){
                    int cur_product = (nums[i] -1 )*(nums[j] -1);
                    pq.push(cur_product);
                }
            }

            return pq.top();
        }
};