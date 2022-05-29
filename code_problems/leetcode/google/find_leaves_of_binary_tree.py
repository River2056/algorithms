class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"[val:{self.val}, left:{self.left}, right:{self.right}]"


def find_leaves_of_binary_tree(root: TreeNode):
    ref = {}

    def dfs(node, layer):
        if not node:
            return layer

        left = dfs(node.left, layer)
        right = dfs(node.right, layer)

        layer = max(left, right)

        if not layer in ref:
            ref[layer] = [node.val]
        else:
            ref[layer].append(node.val)

        return layer + 1

    dfs(root, 0)

    return ref.values()


def test_case(lst):
    if len(lst) <= 1:
        return [[]] if len(lst) < 1 else [[lst[0]]]
    root = construct_tree(lst)
    print_tree(root)
    res = find_leaves_of_binary_tree(root)  # type: ignore
    print(res)


def construct_tree(lst):
    queue = []
    root = None
    curr = None

    while len(lst) > 0:
        elem = lst.pop(0)
        node = TreeNode(elem)
        if not root:
            root = node
        if not curr:
            curr = node
        elif not curr.left:
            curr.left = node
        elif not curr.right:
            curr.right = node

        if curr and curr.left and curr.right:
            queue.append(curr.left)
            queue.append(curr.right)

        if curr.left and curr.right:
            tmp = queue.pop(0)
            curr = tmp

    return root


def print_tree(root):
    print(root)
    res = []
    queue = []
    curr = root
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        res.append(node.val)

    print(res)


def main():
    test_case([1, 2, 3, 4, 5])  # [[4, 5, 3], [2], [1]]


if __name__ == "__main__":
    main()
