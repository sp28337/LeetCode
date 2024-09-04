from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.next == other.next


class Solution24(object):
    def swap_pairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursively swap nodes in pairs inside linked list

        :type head: ListNode
        :rtype: ListNode
        """
        if not isinstance(head, (ListNode, type(None))):
            raise TypeError('head must be an instance of ListNode')
        if not head:
            return
        prev = head
        curr = head.next

        if curr:
            curr.next = self.swap_pairs(curr.next)
        else:
            return head

        curr.next, prev.next = prev, curr.next
        return curr


if __name__ == "__main__":
    test = Solution24()

    assert (test.swap_pairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))) ==
            ListNode(2, ListNode(1, ListNode(4, ListNode(3)))))
    assert (test.swap_pairs(ListNode(1)) == ListNode(1))
    assert (test.swap_pairs(ListNode()) == ListNode(0))
    assert test.swap_pairs(None) is None
