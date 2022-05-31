import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:
    print_bfs(root)

    def check_tree(node, upper_limit=math.inf, lower_limit=-math.inf):
        if not node:
            return True
        if node.val <= lower_limit or node.val >= upper_limit:
            return False
        return check_tree(node.left, node.val, lower_limit) and check_tree(
            node.right, upper_limit, node.val
        )

    return check_tree(root)


def create_tree(lst: list[int]):
    root = None
    curr = None
    queue = []
    while len(lst) > 0:
        elem = lst.pop(0)
        if not elem is None:
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
    head_node = create_tree(lst)
    res = isValidBST(head_node)
    print(res)


def main():
    test_case([2, 1, 3])  # True
    test_case([5, 1, 4, None, None, 3, 6])  # False
    test_case([0, None, -1])  # False


if __name__ == "__main__":
    main()
