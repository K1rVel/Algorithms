# Сложность O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(self, head: ListNode) -> bool:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals == vals[::-1]
