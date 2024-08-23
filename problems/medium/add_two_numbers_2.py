from typing import Optional


class ListNode(object):
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt

    def __str__(self):
        return str(self.val)


class AddTwoNumbers(object):

    @staticmethod
    def add_two_numbers(l1, l2) -> Optional[ListNode]:
        """
        Calculate values of two linked lists and return new linked list with sum of values

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # curr1, curr2 = l1, l2
        # summ = curr1.val + curr2.val
        # tmp = summ // 10
        # l3 = ListNode(summ % 10 + tmp)
        # curr3 = l3
        #
        # while (curr1 is not None) or (curr2 is not None):
        #
        #
        #
        #     curr1, curr2 = curr1.nxt, curr2.nxt
        #     summ = curr1.val + curr2.val
        #     curr3.nxt = ListNode(summ % 10 + tmp)
        #     curr3 = curr3.nxt
        #     tmp = summ // 10
        # curr3.nxt = ListNode(tmp)
        # return l3

        curr1, curr2 = l1, l2
        summ = curr1.val + curr2.val
        tmp = summ // 10
        l3 = ListNode(val=summ % 10, nxt=None)
        curr3 = l3

        while curr1 is not None or curr2 is not None:
            curr1 = curr1.nxt if curr1 else None
            curr2 = curr2.nxt if curr2 else None
            if not any((curr1, curr2)):
                break
            x = curr1.val if curr1 else 0
            y = curr2.val if curr2 else 0
            summ = x + y + tmp
            curr3.nxt = ListNode(summ % 10)
            curr3 = curr3.nxt
            tmp = summ // 10
        if tmp > 0:
            curr3.nxt = ListNode(tmp)
        return l3
