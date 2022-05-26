class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_leaves_of_binary_tree(root: TreeNode) -> list[list[int]]:
    pass


def test_case(lst: list[int]):
    if len(lst) <= 1:
        return [[]] if len(lst) < 1 else [[lst[0]]]
    root = TreeNode(lst[0])
    res = find_leaves_of_binary_tree(root)
    print(res)


def construct_tree(lst, head):
    queue = []
    while len(lst) > 0:
        queue.append(lst.pop(0))


def main():
    test_case([1, 2, 3, 4, 5])  # [[4, 5, 3], [2], [1]]


if __name__ == "__main__":
    main()
