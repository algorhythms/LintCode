"""
The size of the hash table is not determinate at the very beginning. If the total size of keys is too large (e.g. size
>= capacity / 10), we should double the size of the hash table and rehash every keys. Say you have a hash table looks
like below:

size=3, capacity=4
[null, 21->9->null, 14->null, null]

The hash function is:

int hashcode(int key, int capacity) {
    return key % capacity;
}

here we have three numbers, 9, 14 and 21, where 21 and 9 share the same position as they all have the same hashcode 1
(21 % 4 = 9 % 4 = 1). We store them in the hash table by linked list.

rehashing this hash table, double the capacity, you will get:

size=3, capacity=8
index:      0    1    2     3      4    5     6    7
hash table: [null, 9, null, null, null, 21, 14, null]

Given the original hash table, return the new hash table after rehashing .
"""
__author__ = 'Danyang'


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return repr(self.val)


class Solution:
    def rehashing(self, hashTable):
        """

        :param hashTable: A list of The first node of linked list
        :return: A list of The first node of linked list which have twice size
        """
        cap = len(hashTable)
        cap *= 2
        ht = [None for _ in xrange(cap)]
        for node in hashTable:
            while node:
                self.__rehash(ht, ListNode(node.val))  # need a new copy
                node = node.next
        return ht

    def __rehash(self, ht, node):
        code = self.__hashcode(node.val, len(ht))
        if ht[code] is None:
            ht[code] = node
        else:
            cur = ht[code]
            while cur.next:
                cur = cur.next
            cur.next = node

    def __hashcode(self, key, capacity):
        return key%capacity


if __name__ == "__main__":
    hashTable = [None for _ in xrange(3)]
    n0 = ListNode(29)
    n1 = ListNode(5)
    n0.next = n1
    hashTable[2] = n0

    print Solution().rehashing(hashTable)