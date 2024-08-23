from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class AddTwoNumbers(object):

    def add_two_numbers(self, l1, l2) -> Optional[ListNode]:
        """
        Calculate values of two linked lists and return new linked list with sum of values

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = 0
        l3 = ListNode()
        curr3 = l3

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            summ = x + y + tmp
            tmp = summ // 10

            curr3.next = ListNode(summ % 10)
            curr3 = curr3.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if tmp:
            curr3.next = ListNode(tmp)
        return l3.next
