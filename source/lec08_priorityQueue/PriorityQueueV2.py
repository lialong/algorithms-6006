from common import ListUtil
from common.Item import Item


class PriorityQueue:
    def __init__(self, A):
        self.n, self.A = 0, A

    def insert(self):
        if not self.n < len(self.A):
            raise IndexError('insert into full priority queue')
        self.n += 1

    def delete_max(self):
        if self.n < 1:
            raise IndexError('pop from empty priority queue')
        self.n -= 1

    @classmethod
    def sort(Queue, A):
        pq = Queue(A)
        for i in range(len(A)):
            pq.insert()
        for i in range(len(A)):
            pq.delete_max()
        return pq.A


class PQ_Heap(PriorityQueue):
    def insert(self, *args):
        super().insert(*args)
        n, A = self.n, self.A
        max_heapify_up(A, n, n - 1)

    def delete_max(self):
        n, A = self.n, self.A
        A[0], A[n - 1] = A[n - 1], A[0]
        max_heapify_down(A, n - 1, 0)
        super().delete_max()


def parent(i):
    p = (i - 1) // 2
    return p if 0 < i else i


def left(i, n):
    l = 2 * i + 1
    return l if l < n else i


def right(i, n):
    r = 2 * i + 2
    return r if r < n else i


def max_heapify_up(A, n, c):
    p = parent(c)
    if A[p].key < A[c].key:
        A[c], A[p] = A[p], A[c]
        max_heapify_up(A, n, p)


def max_heapify_down(A, n, p):
    l, r = left(p, n), right(p, n)
    c = l if A[r].key < A[l].key else r
    if A[p].key < A[c].key:
        A[c], A[p] = A[p], A[c]
        max_heapify_down(A, n, c)


if __name__ == '__main__':
    list1 = [Item(2, "2"), Item(1, "1"), Item(3, "3")]
    print("pq_binary_heap")
    ListUtil.print_list(PQ_Heap.sort(list1))
