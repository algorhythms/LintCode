"""
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A
word can start from any position in the matrix and go left/right/up/down to the adjacent position.


Example
Given matrix:
doaf
agai
dcan
and dictionary:
{"dog", "dad", "dgdg", "can", "again"}

return {"dog", "dad", "can", "again"}
"""
__author__ = 'Danyang'


class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.word = None
        self.children = {}  # map from char to TrieNode

    def __repr__(self):
        return repr(self.char)


class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    def add(self, word):
        word = word.lower()
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.word = word


class Solution:
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def wordSearchII_TLE(self, board, words):
        """
        Trie+dfs
        pure Trie solution

        :param board: a list of lists of 1 length string
        :param words: a list of string
        :return: a list of string
        """
        trie = Trie()
        for word in words:
            trie.add(word)

        ret = set()
        visited = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, trie.root, visited, ret)

        return list(ret)

    def dfs(self, board, i, j, parent, visited, ret):
        """
        :type parent: TrieNode
        """
        c = board[i][j]
        visited.add((i, j))
        if c in parent.children:
            cur = parent.children[c]
            if cur.word:
                ret.add(cur.word)
            for direction in Solution.directions:
                row = i+direction[0]
                col = j+direction[1]
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and (row, col) not in visited:
                    self.dfs(board, row, col, cur, visited, ret)
        visited.remove((i, j))

    def wordSearchII(self, board, words):
        """
        Trie+dfs

        prune by words, but degenerate to the solution which does not require trie

        :param board: a list of lists of 1 length string
        :param words: a list of string
        :return: a list of string
        """
        ret = []
        for word in words:
            trie = Trie()
            trie.add(word)
            visited = set()
            r = set()
            found = False
            for i in xrange(len(board)):
                if not found:
                    for j in xrange(len(board[0])):
                        self.dfs2(board, i, j, trie.root, visited, r)
                        if len(r) == 1:  # prune when found a result
                            ret.append(r.pop())
                            found = True
                            break

        return ret

    def dfs2(self, board, i, j, parent, visited, ret):
        """
        prune when found a result

        :type parent: TrieNode
        """
        c = board[i][j]
        visited.add((i, j))
        if c in parent.children:
            cur = parent.children[c]
            if cur.word:
                ret.add(cur.word)
            for direction in Solution.directions:
                row = i+direction[0]
                col = j+direction[1]
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and (row, col) not in visited and not ret:
                    self.dfs2(board, row, col, cur, visited, ret)
        visited.remove((i, j))


if __name__ == "__main__":
    board = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaab"]
    words = {"baaaaaaaaaaaaa", "a", "aa", "aaaa", "aaaax", "abaaabbaz"}
    assert Solution().wordSearchII(board, words) == ['a', 'aa', 'aaaa', 'baaaaaaaaaaaaa']
