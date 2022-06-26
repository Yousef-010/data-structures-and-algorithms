import pytest
from challengs.stack_queue_pseudo.stack_queue_pseudo import PseudoQueue


def test_exists():
    assert PseudoQueue


def test_enqueue_single():
    pq = PseudoQueue()
    pq.enqueue(20)
    actual = pq.dequeue()
    expected = 20
    assert actual == expected


def test_enqueue_multi(pq):

    pq.enqueue(5)
    actual = pq.__str__()
    expected = '[5]->[10]->[15]->[20]->'
    actual2 = pq.stack1.top.value
    expected2 = 5
    assert actual == expected
    assert actual2 == expected2


def test_dequeue_tewnty(pq):
    actual = pq.dequeue()
    expected = 20
    assert actual == expected


def test_dequeue_fifteen(pq):
    pq.dequeue()
    actual = pq.dequeue()
    expected = 15
    assert actual == expected


#############
# fixture
#############
@pytest.fixture
def pq():
    pq = PseudoQueue()
    pq.enqueue(20)
    pq.enqueue(15)
    pq.enqueue(10)
    return pq

