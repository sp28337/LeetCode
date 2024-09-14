from typing import Optional


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


def get_intersection_node(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    """
    Return the intersection node of two linked lists

    :type headA: Optional[ListNode]
    :type headB: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    if not headA or not headB:
        return

    curr_a = headA
    curr_b = headB

    tmp = {}
    while curr_a or curr_b:
        if curr_a:
            if curr_a in tmp:
                return curr_a
            tmp[curr_a] = None
            curr_a = curr_a.next

        if curr_b:
            if curr_b in tmp:
                return curr_b
            tmp[curr_b] = None
            curr_b = curr_b.next
    return
