# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#题目要求的二叉树的 从上至下 打印（即按层打印），又称为二叉树的 广度优先搜索（BFS）。
#BFS 通常借助 队列 的先入先出特性来实现。
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root == None :
            return []
        l = [root]
        val = []
        while (l) :
            tempnode = l.pop(0)
            val +=[tempnode.val]
            if (tempnode.left) :
                l.append(tempnode.left)
            if (tempnode.right) :
                l.append(tempnode.right)
        return val
