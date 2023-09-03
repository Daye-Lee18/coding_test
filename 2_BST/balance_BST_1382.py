'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST 
'''

#############################################c++
'''c++ 
#include <vector>
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
 
class Solution{
    public:
    TreeNode* sortedArrayToBST(vector<int>& nums){
        return _sortedArrayToBST(nums, 0, nums.size());
    }
    private:
    TreeNode* _sortedArrayToBST(vector<int> & nums, int left, int right){
            if (left == right) {
                return nullptr;
            } 
            
            int mid = (left + right) / 2 ;
            TreeNode* root = new TreeNode;
            root -> val = nums[mid];
            root -> left = _sortedArrayToBST(nums, left , mid);
            root -> right = _sortedArrayToBST(nums, mid+1, right);
            
            return root ;
    }
};

'''

#################################################c 
'''c
#include <stdio.h>
#include <stdlib.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* sortedArrayToBST(int* nums, int left, int right) {
    if (left == right) {
        return NULL;
    }
    
    int mid = (left + right) / 2;
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = nums[mid];
    root->left = sortedArrayToBST(nums, left, mid);
    root->right = sortedArrayToBST(nums, mid + 1, right);
    
    return root;
}
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self._sortedArrayToBST(nums, 0, len(nums))

    def _sortedArrayToBST(self, nums, left, right):
        if left == right:
            return None
        mid = (left + right) >> 1 # = // 2  
        root = TreeNode(nums[mid])
        root.left = self._sortedArrayToBST(nums, left, mid)
        root.right = self._sortedArrayToBST(nums, mid + 1, right)
        return root


if __name__ == "__main__":
    None