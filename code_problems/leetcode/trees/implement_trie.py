class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if not letter in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if not letter in curr.children:
                return False
            curr = curr.children[letter]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if not letter in curr.children:
                return False
            curr = curr.children[letter]
        return True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


# self implement(not correct)
class Trie_self:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = None
        l = list(map(lambda trienode: trienode.val, self.root.children))
        for i, letter in enumerate(word):
            if letter in l:
                idx = l.index(letter)
                curr = curr.children[idx] if curr else self.root.children[idx]
            else:
                if not curr:
                    curr = TrieNode(letter)
                    self.root.children.append(curr)
                else:
                    node = TrieNode(letter)
                    curr.children.append(node)
                    curr = node

            if curr:
                l = list(map(lambda node: node.val, curr.children))

            if i == len(word) - 1:
                curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = None
        l = list(map(lambda trienode: trienode.val, self.root.children))
        for i, letter in enumerate(word):
            if letter in l:
                idx = l.index(letter)
                curr = curr.children[idx] if curr else self.root.children[idx]
            elif (not letter in l) and (i < len(word) - 1):
                return False

            if curr:
                l = list(map(lambda node: node.val, curr.children))

            if i == len(word) - 1:
                return curr.end_of_word if curr else False

    def startsWith(self, prefix: str) -> bool:
        curr = None
        l = list(map(lambda trienode: trienode.val, self.root.children))
        for i, letter in enumerate(prefix):
            if letter in l:
                idx = l.index(letter)
                curr = self.root.children[idx]
            elif not letter in l and i < len(prefix) - 1:
                return False

            if curr:
                l = list(map(lambda node: node.val, curr.children))

        return not curr is None


class TrieNode_self:
    def __init__(self, val=None):
        self.val = val
        self.children = []
        self.end_of_word = False

    def __str__(self):
        return f"[val: {self.val}, children: {[child.__str__() for child in self.children]}, end_of_word: {self.end_of_word}]"


def test1():
    t = Trie()
    t.insert("apple")
    print(t.search("apple"))  # return True
    print(t.search("app"))  # return False
    print(t.startsWith("app"))  # return True
    t.insert("app")
    print(t.search("app"))  # return True


def main():
    test1()


if __name__ == "__main__":
    main()
