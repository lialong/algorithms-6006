from common import ListUtil
from common.Item import Item

class PriorityQueue:
    def __init__(self):
        self.A = []

    def insert(self, x):
        self.A.append(x)

    def delete_max(self):
        if len(self.A) < 1:
            raise IndexError('pop from empty priority queue')
        return self.A.pop()

    @classmethod
    def sort(Queue, A):
        pq = Queue()
        for x in A:
            pq.insert(x)
        out = [pq.delete_max() for _ in A]
        out.reverse()
        return out

class PQ_Array(PriorityQueue):
    # PriorityQueue.insert already correct: appends to end of self.A
    def delete_max(self):
        n, A, m = len(self.A), self.A, 0
        for i in range(1, n):
            if A[m].key < A[i].key:
                m = i
        A[m], A[n-1] = A[n-1], A[m]
        return super().delete_max()


class PQ_SortedArray(PriorityQueue):
    # PriorityQueue.delete_max already correct: pop from end of self.A
    def insert(self, *args):
        super().insert(*args)
        i, A = len(self.A) - 1, self.A
        while 0 < i and A[i].key < A[i-1].key:
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1

if __name__ == '__main__':
    list1 = [Item(2, "2"), Item(1, "1"), Item(3, "3")]

    print("origin sort")
    ListUtil.print_list(list1)

    print("pq_array")
    pqArray = PQ_Array()
    ListUtil.print_list(pqArray.sort(list1))

    print("pq_sorted_array")
    pqSortedArray = PQ_SortedArray()
    ListUtil.print_list(pqSortedArray.sort(list1))
