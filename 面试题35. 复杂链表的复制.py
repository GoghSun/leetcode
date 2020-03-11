"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummyNode = Node('100000',None,None)
        NewHead = dummyNode
        cur = head
        datadic = {}
        olddic = {}
        count = 0
        while(cur):
            NewNode = Node(cur.val,None,None)
            datadic[cur]  = NewNode
            count +=1
            cur = cur.next
            dummyNode.next = NewNode
            dummyNode = dummyNode.next
        dummyNode.next = None
        cur = head
        datadic[None]  = None
        NewHead = NewHead.next
        temp = NewHead
        count = 0
        while(cur):
            temp.random = datadic[cur.random]
            temp = temp.next
            cur  = cur.next
        return NewHead
		
关键是random 和listnode的对应关系，建立成哈希表