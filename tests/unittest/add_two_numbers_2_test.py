from unittest import TestCase, main
from problems import AddTwoNumbers, ListNode


class AddTwoNumbersTest(TestCase):

    @staticmethod
    def convert_to_list(linked_list) -> list:
        if linked_list is None:
            return []
        curr = linked_list
        result = [curr.val]
        while curr.next:
            curr = curr.next
            result.append(curr.val)
        return result

    def test1_add_two_numbers(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        solution = AddTwoNumbers()
        self.assertEqual(self.convert_to_list(solution.add_two_numbers(l1, l2)), [7, 0, 8])

    def test2_add_two_numbers(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        solution = AddTwoNumbers()
        self.assertEqual(self.convert_to_list(solution.add_two_numbers(l1, l2)), [8, 9, 9, 9, 0, 0, 0, 1])

    def test3_add_two_numbers(self):
        l1 = ListNode()
        l2 = ListNode()
        solution = AddTwoNumbers()
        self.assertEqual(self.convert_to_list(solution.add_two_numbers(l1, l2)), [0])


if __name__ == '__main__':
    main()
