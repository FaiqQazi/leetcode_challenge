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
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(root==nullptr){
            TreeNode *t=new TreeNode(val);
            return t;
        }
        if(root != nullptr && root->left==nullptr && root->val>val){
            root->left=new TreeNode(val);
        }
        if(root != nullptr && root->right==nullptr && root->val<val){
            root->right=new TreeNode(val);
        }
        if(root != nullptr && val>root->val){
            insertIntoBST(root->right,val);
        }
        else if(root!=nullptr){
            insertIntoBST(root->left,val);
        }
        return root;

    }
};