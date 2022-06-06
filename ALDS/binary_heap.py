#binary heap implementation
#
#implemnt min heap, of which parent value is smaller than children
#code from geeksforgeeks

import sys
class Min_heap:

    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [0]*(self.max_size + 1)
        self.heap[0] = -1 * sys.maxsize
        self.front = 1

    def insert(self, element):
        if self.size >= self.max_size:
            return
        self.size+=1
        self.heap[self.size] = element

        current = self.size
        if self.heap[current] < self.heap[current//2]:
            self.swap(current, current//2)
            current = current//2

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def remove(self):
        popped = self.heap[self.front]
        self.heap[self.front] = self.heap[self.size]
        self.size -=1
        self.min_heapify(self.front)
        return popped

    def min_heapify(self, pos):

        if pos*2 <= self.size:
            if (self.heap[pos] > self.heap[pos*2] or self.heap[pos] > self.heap[(pos*2)+1]):
                if self.heap[pos] < self.heap[(pos*2)+1]:
                    self.swap(pos, pos*2)
                    self.min_heapify(pos*2)
                else:
                    self.swap(pos, (pos*2)+1)
                    self.min_heapify((pos*2)+1)

    def print(self):
        for i in range(1, (self.size//2)+1):
            print("parent : " + str(self.heap[i]) + " left :" +
                                str(self.heap[i*2]) + " right :"+
                                str(self.heap[i*2+1]))

    def min_heap(self):
        for pos in range(self.size//2, 0, -1):
            self.min_heapify(pos)

if __name__ == '__main__':
    print("minheap:")
    min_heap = Min_heap(15)
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(17)
    min_heap.insert(10)
    min_heap.insert(84)
    min_heap.insert(19)
    min_heap.insert(6)
    min_heap.insert(22)
    min_heap.insert(9)
    min_heap.min_heap

    min_heap.print()
    print("min val : " + str(min_heap.remove()))
