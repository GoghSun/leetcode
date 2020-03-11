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



哈希的做法，在大多数公司的面试官面前并不是一个满意的答案，所以需要知道原地修改的解法才能够从容面对面试。 原地修改解法流程：
复制一个新的节点在原有节点之后，如 1 -> 2 -> 3 -> null 复制完就是 1 -> 1 -> 2 -> 2 -> 3 - > 3 -> null
从头开始遍历链表，通过 cur.next.random = cur.random.next 可以将复制节点的随机指针串起来，当然需要判断 cur.random 是否存在
将复制完的链表一分为二 根据以上信息，我们不难写出以下代码
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return head;
        }
        // 完成链表节点的复制
        Node cur = head;
        while (cur != null) {
            Node copyNode = new Node(cur.val);
            copyNode.next = cur.next;
            cur.next = copyNode;
            cur = cur.next.next;
        }

        // 完成链表复制节点的随机指针复制
        cur = head;
        while (cur != null) {
            if (cur.random != null) { // 注意判断原来的节点有没有random指针
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }

        // 将链表一分为二
        Node copyHead = head.next;
        cur = head;
        Node curCopy = head.next;
        while (cur != null) {
            cur.next = cur.next.next;
            cur = cur.next;
            if (curCopy.next != null) {
                curCopy.next = curCopy.next.next;
                curCopy = curCopy.next;
            }
        }
        return copyHead;