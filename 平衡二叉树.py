```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
// 自上而下的 暴力方法
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if(root == None):
            return True
        return abs(self.deepth(root.left) - self.deepth(root.right)) <2 \
            and self.isBalanced(root.left) and self.isBalanced(root.right)       
    def deepth(self,root:TreeNode):
        if root == None: 
            return 0
        else:
            return max(self.deepth(root.left),self.deepth(root.right)) +1

// 自下而上的 快速方法


class Solution:
    # Return whether or not the tree at root is balanced while also returning
    # the tree's height
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1
        
        # Check subtrees to see if they are balanced. 
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        
        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]

作者：LeetCode
链接：https://leetcode-cn.com/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return -1
        right = self.depth(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

作者：jyd
链接：https://leetcode-cn.com/problems/balanced-binary-tree/solution/balanced-binary-tree-di-gui-fang-fa-by-jin40789108/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。