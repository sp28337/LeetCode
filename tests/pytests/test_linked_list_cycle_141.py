from tests.pytests import ListNode, has_cycle


def test_has_cycle_true():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert has_cycle(head) is True


def test_has_cycle_false():
    head = ListNode(1)
    head.next = ListNode(2)
    assert has_cycle(head) is False


def test_has_cycle_empty():
    assert has_cycle(ListNode()) is False


def test_has_cycle_one():
    assert has_cycle(ListNode(1)) is False


def test_has_cycle_two():
    assert has_cycle(ListNode(1, ListNode(2))) is False


def test_has_cycle_none():
    assert has_cycle(None) is False
