class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: ListNode) -> bool:
    """
    Return True if linked list has cycle, else return False

    :type head: ListNode
    :rtype: bool
    """

    if not head:
        return False

    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
