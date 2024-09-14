import pytest


from tests.pytests import get_intersection_node, ListNode


def test_get_intersection_node():
    tail = ListNode(8)
    curr = tail
    for node in [4, 5]:
        curr.next = ListNode(node)
        curr = curr.next

    head1 = ListNode(4)
    curr = head1
    for node in [1]:
        curr.next = ListNode(node)
        curr = curr.next
    curr.next = tail

    head2 = ListNode(5)
    curr = head2
    for node in [6, 1]:
        curr.next = ListNode(node)
        curr = curr.next
    curr.next = tail
    assert get_intersection_node(headA=head1, headB=head2) == tail


def test_get_intersection_node_none():
    assert get_intersection_node(None, None) is None


def test_get_intersection_node_1_none():
    assert get_intersection_node(None, ListNode(2)) is None


def test_get_intersection_node_2_none():
    assert get_intersection_node(ListNode(1), None) is None


if __name__ == "__main__":
    pytest.main()
