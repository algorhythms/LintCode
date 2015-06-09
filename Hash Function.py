"""
In data structure Hash, hash function is used to convert a string(or any other type) into an integer smaller than hash
size and bigger or equal to zero. The objective of designing a hash function is to "hash" the key as unreasonable as
possible. A good hash function can avoid collision as less as possible. A widely used hash function algorithm is using
a magic number 33
"""
__author__ = 'Danyang'


class Solution:
    def hashCode(self, key, HASH_SIZE):
        """
        :param key: A String you should hash
        :param HASH_SIZE: An integer
        :return an integer
        """
        w = 1
        ret = 0
        for i in xrange(len(key)-1, -1, -1):
            ret = (ret+ord(key[i])*w)%HASH_SIZE
            w = (w*33)%HASH_SIZE
        return ret


if __name__ == "__main__":
    assert Solution().hashCode("abcd", 100) == 78

