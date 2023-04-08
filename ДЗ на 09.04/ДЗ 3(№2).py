# Сложность O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ptr = head
        s = ''
        while ptr != None:
            s += str(ptr.val)
            ptr = ptr.next
        return int(s, 2)