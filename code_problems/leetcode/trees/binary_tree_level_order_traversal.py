class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_level_order_traversal_self_not_correct(root: TreeNode):
    res = []
    level_nodes = []
    queue = []
    queue.append(root)

    level = 0
    level_track = 2**level
    while len(queue) > 0:
        node = queue.pop(0)
        if node and node.left:
            queue.append(node.left)
        if node and node.right:
            queue.append(node.right)
        if node:
            level_nodes.append(node.val)
        level_track -= 1
        if level_track <= 0:
            level += 1
            level_track = 2**level
            res.append(level_nodes)
            level_nodes = []

    return res


def binary_tree_level_order_traversal(root: TreeNode):
    res = []
    queue = []
    queue.append(root)

    while len(queue) > 0:
        length = len(queue)
        level = []
        for _ in range(length):
            node = queue.pop(0)
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            res.append(level)

    return res


def create_tree(lst: list[int]):
    root = None
    curr = None
    queue = []
    while len(lst) > 0:
        elem = lst.pop(0)
        if elem:
            node = TreeNode(elem)
        else:
            node = None
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


def print_bfs(root: TreeNode):
    res = []
    queue = []
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        if node and node.left:
            queue.append(node.left)
        if node and node.right:
            queue.append(node.right)
        res.append(node.val if node else node)

    print(res)


def test_case(lst):
    root = create_tree(lst)
    res = binary_tree_level_order_traversal(root)
    print(res)


def main():
    test_case([3, 9, 20, None, None, 15, 7])  # [[3], [9, 20], [15, 7]]
    test_case([1])  # [[1]]
    test_case([])  # []


if __name__ == "__main__":
    main()
